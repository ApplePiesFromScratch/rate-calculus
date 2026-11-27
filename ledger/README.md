# Ledger

`ledger.jsonl` (created on first use) is append-only: one JSON line per event, each chained to the one before by its hash. Add events with `python3 tools/ledger.py add <kind> "<text>" [--file PATH]`, check the chain with `python3 tools/ledger.py verify`, seal a file before a read with `python3 tools/seal.py PATH`.

Kinds: claim, killline, seal, amend, predict, run, result, witness, fail, intervene, reconfigure, self, read. A correction is a new event that names the old one; nothing is edited or deleted.
