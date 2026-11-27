#!/usr/bin/env python3
"""ledger.py: an append-only ledger, one JSON line per event, each line chained to the one before by its hash.

  python3 tools/ledger.py add <kind> "<text>" [--file PATH ...] [--ledger PATH]
  python3 tools/ledger.py verify [--ledger PATH]
  python3 tools/ledger.py show [--ledger PATH]

Kinds this repo uses: claim, killline, seal, amend, predict, run, result, witness, fail, intervene, reconfigure, self, read.
A correction is a new event that names the old one ("supersedes": n). Nothing is edited or deleted.
Default ledger: ledger/ledger.jsonl at the repo root. The chain catches a partial edit; a full rewrite of a local file
is not caught (no outside anchor). Push the ledger, or paste its last hash somewhere you don't control, to anchor it.
"""
import hashlib, json, os, sys, time

REPO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DEFAULT = os.path.join(REPO, "ledger", "ledger.jsonl")


def sha(path):
    h = hashlib.sha256()
    with open(path, "rb") as f:
        h.update(f.read())
    return h.hexdigest()


def lines(path):
    if not os.path.exists(path):
        return []
    with open(path) as f:
        return [l.rstrip("\n") for l in f if l.strip()]


def add(kind, text, files=(), ledger=DEFAULT, extra=None):
    os.makedirs(os.path.dirname(os.path.abspath(ledger)), exist_ok=True)
    prev = lines(ledger)
    ev = {"n": len(prev) + 1, "t": time.strftime("%Y-%m-%dT%H:%M:%S%z"), "kind": kind, "text": text,
          "files": {os.path.relpath(os.path.abspath(p), REPO): sha(p) for p in files},
          "prev": hashlib.sha256(prev[-1].encode()).hexdigest() if prev else ""}
    if extra:
        ev.update(extra)
    line = json.dumps(ev, sort_keys=True)
    with open(ledger, "a") as f:
        f.write(line + "\n")
    return ev, hashlib.sha256(line.encode()).hexdigest()


def verify(ledger=DEFAULT):
    ls = lines(ledger)
    bad = []
    for i, l in enumerate(ls):
        ev = json.loads(l)
        want = hashlib.sha256(ls[i - 1].encode()).hexdigest() if i else ""
        if ev.get("prev") != want or ev.get("n") != i + 1:
            bad.append(i + 1)
    return ls, bad


if __name__ == "__main__":
    a = sys.argv[1:]
    led = DEFAULT
    if "--ledger" in a:
        k = a.index("--ledger"); led = a[k + 1]; del a[k:k + 2]
    if not a or a[0] not in ("add", "verify", "show"):
        print(__doc__); sys.exit(2)
    if a[0] == "add":
        files = []
        while "--file" in a:
            k = a.index("--file"); files.append(a[k + 1]); del a[k:k + 2]
        ev, h = add(a[1], " ".join(a[2:]), files, led)
        print(f"event {ev['n']} ({ev['kind']}) appended; line hash {h[:16]}")
    else:
        ls, bad = verify(led)
        if a[0] == "show":
            for l in ls:
                ev = json.loads(l); print(f"{ev.get('n', 0):4d} {ev.get('t', '?')} {ev.get('kind', '?'):11s} {str(ev.get('text', ''))[:90]}")
        kinds = {}
        for l in ls:
            k = json.loads(l).get("kind", "?"); kinds[k] = kinds.get(k, 0) + 1
        print(f"{len(ls)} events, chain {'unbroken' if not bad else 'BROKEN at ' + str(bad)}; " + ", ".join(f"{k} {v}" for k, v in sorted(kinds.items())))
        print("last line hash:", hashlib.sha256(ls[-1].encode()).hexdigest()[:16] if ls else "-")
        sys.exit(1 if bad else 0)
