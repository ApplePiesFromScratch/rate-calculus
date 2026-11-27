#!/usr/bin/env python3
"""seal.py FILE [--ledger PATH]: hash a file (kill lines, a sealed set's manifest, an amendment) into the ledger
before the run or read it governs. Prints the first 16 hex digits of its sha256 to quote in your README."""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import ledger
a = sys.argv[1:]
led = ledger.DEFAULT
if "--ledger" in a:
    k = a.index("--ledger"); led = a[k + 1]; del a[k:k + 2]
if not a:
    print(__doc__); sys.exit(2)
for p in a:
    h = ledger.sha(p)
    ev, _ = ledger.add("seal", f"sealed {os.path.basename(p)} {h[:16]}", [p], led)
    print(f"{p}: sha256 {h[:16]}  (ledger event {ev['n']})")
