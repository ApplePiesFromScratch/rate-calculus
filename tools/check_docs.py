#!/usr/bin/env python3
"""check_docs.py: every number in this repo's guides and examples is run, not trusted.

1. Every ```check block in guide/*.md and examples/*/README.md is run line by line, with `from ratecalc import *`:
     - a line like `x = isolate(4)` (a name, then ' = '), or a one-line `def`, `import` or `from`, is run as code and
       kept for the rest of the block; a line starting `do ` runs the rest as a statement (a call whose result
       is not a claim);
     - every other line must evaluate to True.
     - lines starting with # are notes.
2. Every examples/*/README.md that has an ```output block: `python3 example.py` is run in that folder and its printed
   output must equal the block, line for line.
Exit 0 only if every check passed. Usage: python3 tools/check_docs.py [-q]
"""
import glob, os, re, subprocess, sys

REPO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, REPO)
ASSIGN = re.compile(r"^[A-Za-z_][A-Za-z_0-9.\[\]]*(\s*,\s*[A-Za-z_][A-Za-z_0-9.\[\]]*)*\s=\s")


def blocks(path, kind):
    out, cur, start = [], None, 0
    for i, line in enumerate(open(path, encoding="utf-8"), 1):
        s = line.rstrip("\n")
        if cur is None and s.strip() == "```" + kind:
            cur, start = [], i + 1
        elif cur is not None and s.strip() == "```":
            out.append((start, cur)); cur = None
        elif cur is not None:
            cur.append(s)
    return out


def run_checks(path, quiet):
    import ratecalc
    good = bad = 0
    for start, lines in blocks(path, "check"):
        ns = {}
        exec("from ratecalc import *", ns)
        for k, line in enumerate(lines):
            t = line.strip()
            if not t or t.startswith("#"):
                continue
            where = f"{os.path.relpath(path, REPO)}:{start + k}"
            try:
                if t.startswith("do "):
                    exec(t[3:], ns); continue
                if ASSIGN.match(t) or t.startswith(("def ", "import ", "from ")):
                    exec(t, ns); continue
                ok = eval(t, ns) is True
            except Exception as e:
                ok = False; t = f"{t}   [raised {type(e).__name__}: {e}]"
            if ok:
                good += 1
            else:
                bad += 1; print(f"FAIL {where}: {t}")
    return good, bad


def run_outputs(path, quiet):
    good = bad = 0
    d = os.path.dirname(path)
    for start, lines in blocks(path, "output"):
        script = os.path.join(d, "example.py")
        env = dict(os.environ, PYTHONPATH=REPO)
        p = subprocess.run([sys.executable, "example.py"], cwd=d, env=env, capture_output=True, text=True, timeout=600)
        got = p.stdout.rstrip("\n").split("\n")
        want = [l for l in lines]
        while want and not want[-1].strip():
            want.pop()
        if got == want and p.returncode == 0:
            good += 1
        else:
            bad += 1
            print(f"FAIL {os.path.relpath(path, REPO)}:{start}: output of example.py differs (exit {p.returncode})")
            for i in range(max(len(got), len(want))):
                g = got[i] if i < len(got) else "<none>"; w = want[i] if i < len(want) else "<none>"
                if g != w:
                    print(f"   line {i + 1}: want {w!r}\n   line {i + 1}: got  {g!r}"); break
            if p.stderr.strip():
                print("   stderr: " + p.stderr.strip().splitlines()[-1])
    return good, bad


NO_CLAIMS_NEEDED = {"README.md", "21_claims_and_reports.md", "23_mistakes_and_presumptions.md", "24_glossary.md", "25_questions.md"}


def main():
    quiet = "-q" in sys.argv
    files = sorted(glob.glob(os.path.join(REPO, "guide", "*.md")) + glob.glob(os.path.join(REPO, "examples", "*", "README.md"))
                   + glob.glob(os.path.join(REPO, "*.md")))
    G = B = O = OB = 0
    for f in files:
        g, b = run_checks(f, quiet); G += g; B += b
        rel = os.path.relpath(f, REPO)
        # an empty grid proves nothing: all([]) is True, so a guide with no claims, or an example with no output block,
        # would pass by checking nothing. Those are failures here.
        if rel.startswith("guide" + os.sep) and os.path.basename(f) not in NO_CLAIMS_NEEDED and g + b == 0:
            B += 1; print(f"FAIL {rel}: no checked claims (a guide that teaches numbers must carry at least one)")
        if "examples" in f:
            g, b = run_outputs(f, quiet); O += g; OB += b
            if g + b == 0:
                OB += 1; print(f"FAIL {rel}: no ```output block to compare")
    plant = os.environ.get("RC_PLANT", "")
    print(f"check_docs{' [RC_PLANT=' + plant + ']' if plant else ''}: claims {G} passed, {B} failed; example outputs {O} matched, {OB} differed")
    sys.exit(1 if (B or OB) else 0)


if __name__ == "__main__":
    main()
