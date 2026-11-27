"""Planted faults. Set RC_PLANT to one name below and the matching rule breaks on purpose.

tools/check_all.py runs every check once clean (all must pass) and once per plant (at least one check must fail).
A check that no plant can turn red is not a witness of anything. Never set RC_PLANT outside that test.
"""
import os

PLANT = os.environ.get("RC_PLANT", "")
NAMES = {
    "mix-rate-product": "mix multiplies the two rate slots instead of adding the two strips",
    "div-sign": "derived division subtracts the strips the wrong way round",
    "mouth-floor": "the mouth lands toward the more negative number (a floor)",
    "carry-if": "the carry sends at most one pulse a tick (if, not while)",
    "heading-sign": "the heading's c is built as P*P - Q*Q",
    "meet-sign": "when drops the minus sign",
    "theta-zero": "rate against a still reading returns 0 instead of refusing",
}
if PLANT and PLANT not in NAMES:
    raise SystemExit(f"RC_PLANT={PLANT!r} is not a known plant: {sorted(NAMES)}")
