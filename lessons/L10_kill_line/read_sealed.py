#!/usr/bin/env python3
"""read_sealed.py THRESHOLD: reads the sealed set once and writes the result into the ledger.

Refuses unless lessons/work/L10_KILL_LINES.md was sealed (tools/seal.py) before this read and is unchanged since.
Refuses a second read. The ledger records the order; it cannot stop anyone opening data/sealed.csv by hand.
If that happened, log it as a self event: the sealed set is then one more tuning set, and the claim needs a new one.
"""
import json, os, sys
HERE = os.path.dirname(os.path.abspath(__file__))
REPO = os.path.dirname(os.path.dirname(HERE))
sys.path.insert(0, os.path.join(REPO, "tools")); sys.path.insert(0, HERE)
import ledger
from score import score
led = os.environ.get("P07_LEDGER", ledger.DEFAULT)
kl = os.path.join(REPO, "lessons", "work", "L10_KILL_LINES.md")
rel = os.path.relpath(kl, REPO)
evs = [json.loads(l) for l in ledger.lines(led)]
seals = [e for e in evs if e["kind"] == "seal" and rel in e.get("files", {})]
reads = [e for e in evs if e["kind"] == "read" and "L10 sealed" in e["text"]]
if not os.path.exists(kl) or not seals:
    sys.exit("refused: seal lessons/work/L10_KILL_LINES.md first (python3 tools/seal.py lessons/work/L10_KILL_LINES.md)")
if seals[-1]["files"][rel] != ledger.sha(kl):
    sys.exit("refused: the kill lines changed after the seal. Log an amendment (tools/seal.py again, with a reason in an amend event) before the read.")
if reads:
    sys.exit(f"refused: the sealed set was already read (ledger event {reads[0]['n']}).")
t = int(sys.argv[1]); tr, tn = score(t, "tune"); sr, sn = score(t, "sealed")
ev, _ = ledger.add("read", f"L10 sealed read: threshold {t}: tune {tr}/{tn}, sealed {sr}/{sn}", [kl], led)
print(f"threshold {t}: right on the tuning set {tr}/{tn}, on the sealed set {sr}/{sn}  (ledger event {ev['n']})")
