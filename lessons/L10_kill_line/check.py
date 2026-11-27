#!/usr/bin/env python3
"""L10 check: a kill line written and sealed before the read it governs, one sealed read, and a report that quotes it.

  python3 lessons/L10_kill_line/check.py                 # reads ledger/ledger.jsonl and lessons/work/L10_*
  python3 lessons/L10_kill_line/check.py --planted       # planted ledgers in planted/
"""
import json, os, re, sys
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, "..", "common")); sys.path.insert(0, os.path.join(HERE, "..", "..", "tools"))
import harness, ledger
TASK = "L10_kill_line"
REL = "lessons/work/L10_KILL_LINES.md"


def check(path):
    """path: a ledger file. The kill-lines and report files are read from lessons/work unless the ledger is planted."""
    R = []
    ls, bad = ledger.verify(path)
    R.append(("ledger chain unbroken", not bad, f"broken at {bad}"))
    evs = [json.loads(l) for l in ls]
    seals = [e for e in evs if e.get("kind") == "seal" and REL in e.get("files", {})]
    reads = [e for e in evs if e.get("kind") == "read" and "L10 sealed" in e.get("text", "")]
    R.append(("kill lines sealed", bool(seals), "no seal event for " + REL))
    R.append(("exactly one sealed read", len(reads) == 1, f"{len(reads)} reads"))
    if seals and reads:
        R.append(("the seal comes before the read", seals[0]["n"] < reads[0]["n"], f"seal {seals[0]['n']}, read {reads[0]['n']}"))
        R.append(("the read names the sealed kill lines' hash", reads[0]["files"].get(REL) == seals[-1]["files"][REL], "hash differs"))
    planted = os.path.dirname(os.path.abspath(path)) == os.path.join(HERE, "planted", "ledgers")
    work = os.path.join(harness.LESSONS, "work")
    klp = os.path.join(HERE, "planted", "KILL_LINES.md") if planted else os.path.join(work, "L10_KILL_LINES.md")
    rpp = os.path.join(HERE, "planted", "REPORT.md") if planted else os.path.join(work, "L10_REPORT.md")
    kl = open(klp).read() if os.path.exists(klp) else ""
    R.append(("kill lines state a pass mark on the sealed set (a line with 'pass mark' and a number)", bool(re.search(r"pass mark.*\d", kl, re.I)), ""))
    R.append(("kill lines state what output would show the claim false (a line with 'kill line')", bool(re.search(r"kill line", kl, re.I)), ""))
    rp = open(rpp).read() if os.path.exists(rpp) else ""
    if reads:
        m = re.search(r"tune (\d+)/200, sealed (\d+)/200", reads[0]["text"])
        R.append(("report quotes the tuning score from the ledger", bool(m) and f"{m.group(1)}/200" in rp, ""))
        R.append(("report quotes the sealed score from the ledger", bool(m) and f"{m.group(2)}/200" in rp, ""))
    R.append(("report says whether the kill line fired", bool(re.search(r"\b(fired|did not fire|held)\b", rp, re.I)), ""))
    pm = re.search(r"pass mark[^0-9]*(\d+)", kl, re.I)
    if reads and pm and m:
        fired = int(m.group(2)) < int(pm.group(1))
        said_not = bool(re.search(r"did not fire|not fired|held", rp, re.I))
        R.append((f"report's verdict matches the numbers (sealed {m.group(2)} against pass mark {pm.group(1)}: {'fired' if fired else 'did not fire'})", said_not != fired, "the report says the opposite"))
    return R


if __name__ == "__main__":
    harness.main(TASK, check, ledger.DEFAULT, os.path.join(HERE, "planted", "ledgers"))
