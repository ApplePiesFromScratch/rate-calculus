"""harness.py: shared by every lesson checker.

A checker is a list of named checks. Each check returns (ok, detail). The checker prints one line per check,
then PASS or FAIL with counts, and exits 0 or 1. With --planted it runs itself against every file in the task's
planted/ folder instead of your work, and passes only if it FAILS on every planted fault: the checker checked.
"""
import importlib.util, os, subprocess, sys, tempfile, hashlib, json, time
sys.dont_write_bytecode = True

HERE = os.path.dirname(os.path.abspath(__file__))
LESSONS = os.path.dirname(HERE)
REPO = os.path.dirname(LESSONS)


def load_module(path, name="work"):
    spec = importlib.util.spec_from_file_location(name, path)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


def compile_c(sources, out, extra=()):
    cc = os.environ.get("CC", "gcc")
    cmd = [cc, "-O2", "-std=c99", "-Wall", "-Wno-unused-function", "-o", out, *sources, *extra]
    r = subprocess.run(cmd, capture_output=True, text=True)
    return r.returncode == 0, (r.stderr or "").strip()


def run(cmd, timeout=120, input_text=None):
    r = subprocess.run(cmd, capture_output=True, text=True, timeout=timeout, input=input_text)
    return r.returncode, r.stdout, r.stderr


def report(task, results, quiet=False):
    fails = [(n, d) for n, ok, d in results if not ok]
    if not quiet:
        for n, ok, d in results:
            print(f"  {'ok  ' if ok else 'FAIL'} {n}" + (f": {d[:160]}" if d and not ok else ""))
        print(f"{task}: {'PASS' if not fails else 'FAIL'} ({len(results) - len(fails)} of {len(results)} checks held)")
    return not fails


def main(task, check_fn, work_default, planted_dir):
    """check_fn(path) -> list of (name, ok, detail). Wraps the --planted mode."""
    args = sys.argv[1:]
    if args and args[0] == "--planted":
        files = sorted(f for f in os.listdir(planted_dir) if not f.startswith(".") and os.path.isfile(os.path.join(planted_dir, f)))
        caught = 0
        for f in files:
            p = os.path.join(planted_dir, f)
            try:
                res = check_fn(p)
                ok = report(task, res, quiet=True)
            except Exception as e:  # a crash on a planted fault counts as caught; say so
                ok, res = False, [("crash", False, repr(e)[:120])]
            first = next((n for n, o, d in res if not o), "-")
            print(f"  planted {f}: {'CAUGHT (first failing check: ' + first + ')' if not ok else 'MISSED'}")
            caught += (not ok)
        print(f"{task} --planted: {'PASS' if caught == len(files) else 'FAIL'} (caught {caught} of {len(files)} planted faults)")
        sys.exit(0 if caught == len(files) else 1)
    path = args[0] if args else work_default
    if not os.path.exists(path):
        print(f"{task}: no work at {path}. Write it first (see the task's README).")
        sys.exit(2)
    ok = report(task, check_fn(path))
    sys.exit(0 if ok else 1)
