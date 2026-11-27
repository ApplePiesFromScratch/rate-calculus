#!/usr/bin/env python3
"""check_all.py: the one command. Runs, in order:
  1. tools/check_docs.py clean: every claim and every example output must pass.
  2. tools/check_docs.py once per planted fault (ratecalc/_plant.py): each must make at least one check FAIL.
     A plant that nothing catches means the checks do not cover that rule: that is reported as a failure.
  3. tools/wordlint.py over every .md file.
  4. tests/test_core.py (the core's own tests, each with a planted twin).
  5. The C core (core_c/): built and tested with gcc or cc if one is installed; reported SKIPPED (not passed) otherwise.
  6. Every lesson's checker: it must PASS the reference solution and catch every planted fault (--planted).
Exit 0 only if everything that ran passed. Usage: python3 tools/check_all.py
"""
import os, shutil, subprocess, sys

REPO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, REPO)
from ratecalc._plant import NAMES


def run(cmd, env_extra=None, cwd=REPO):
    env = dict(os.environ, PYTHONPATH=REPO, **(env_extra or {}))
    env.pop("RC_PLANT", None) if not env_extra or "RC_PLANT" not in env_extra else None
    p = subprocess.run(cmd, cwd=cwd, env=env, capture_output=True, text=True)
    return p.returncode, (p.stdout + p.stderr).strip()


results = []
code, out = run([sys.executable, "tools/check_docs.py"])
print(out.splitlines()[-1]); results.append(("docs clean", code == 0))
if code:
    print(out)
for name, why in NAMES.items():
    code, out = run([sys.executable, "tools/check_docs.py"], {"RC_PLANT": name})
    caught = code != 0
    n_fail = sum(1 for l in out.splitlines() if l.startswith("FAIL"))
    print(f"plant {name:18s} ({why}): {'caught by ' + str(n_fail) + ' checks' if caught else 'NOT CAUGHT'}")
    results.append((f"plant {name}", caught))
code, out = run([sys.executable, "tools/wordlint.py"])
print(out.splitlines()[-1]); results.append(("wordlint", code == 0))
if code:
    print(out)
code, out = run([sys.executable, "tests/test_core.py"])
print(out.splitlines()[-1]); results.append(("core tests", code == 0))
if code:
    print(out)
cc = shutil.which("gcc") or shutil.which("cc")
if cc and os.path.isdir(os.path.join(REPO, "core_c")):
    code, out = run(["sh", "-c", f"{cc} -std=c99 -O2 -Wall -Wextra -Werror -o /tmp/rc_core_test core_c/test_core.c core_c/reading.c && /tmp/rc_core_test"])
    print(out.splitlines()[-1] if out else "C core: no output"); results.append(("C core", code == 0))
    if code:
        print(out)
else:
    print("C core: SKIPPED (no gcc or cc found). Not a pass.")
LESSONS = [("L01_readings", "L01_readings.py"), ("L02_two_cuts", "L02_cuts.json"), ("L03_rules", "L03_rules.py"),
           ("L04_heading", "L04_heading.py"), ("L05_transfer", "L05_transfer.py"), ("L06_lever", "L06_lever.py"),
           ("L07_alphabet", "L07_alphabet.py"), ("L08_fluid", "L08_fluid.py"), ("L09_pattern", "L09_pattern.py"),
           ("L11_dereify", "L11_MAP.md")]
for task, ref in LESSONS:
    c1, o1 = run([sys.executable, f"lessons/{task}/check.py", f"lessons/reference/{ref}"])
    c2, o2 = run([sys.executable, f"lessons/{task}/check.py", "--planted"])
    print(f"lesson {task}: reference {'PASS' if c1 == 0 else 'FAIL'}; {o2.splitlines()[-1].split(': ', 1)[-1]}")
    results.append((f"lesson {task}", c1 == 0 and c2 == 0))
    if c1:
        print(o1)
c3, o3 = run([sys.executable, "lessons/L10_kill_line/check.py", "--planted"])
print(f"lesson L10_kill_line: {o3.splitlines()[-1].split(': ', 1)[-1]} (its reference run needs your own sealed read, so only --planted runs here)")
results.append(("lesson L10_kill_line planted", c3 == 0))
bad = [n for n, ok in results if not ok]
print(f"\ncheck_all: {len(results) - len(bad)} passed, {len(bad)} failed" + (": " + ", ".join(bad) if bad else ""))
sys.exit(1 if bad else 0)
