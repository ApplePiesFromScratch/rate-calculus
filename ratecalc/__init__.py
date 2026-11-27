"""ratecalc: the machine from 'Every Number Is A Rule' (James Pugmire), in exact Python. Standard library only."""
from fractions import Fraction
from .reading import (F, Reading, R, Refusal, THETA, NO_QUOTIENT, isolate, const, mix, rate, power, lift, show)
from .triple import Triple, isolate3
from .lever import Lever, source
from .whole import mouth, mouth_of, toward_negative, toward_zero, Carry
from .heading import heading, unit, combine, turn_point_shears, turn_point_rounded
from .rules import (sqrt2_halving, halving_steps_for, sqrt2_averaging, E_poly, E_tail_bound, S_poly, C_poly, stage_for)
from .meet import gap, when, grow, closest
from .steps import step_forward, step_back, run_forward, run_back, collisions, transfer_step, assign_blur_step
from .witness import standing
from .certify import certify, Certificate
from .alphabet import scan_closure, scan_closure2, morphism, drop_rate, LIVE_RATE
from .flow import Box
from .pattern import Flux, Pattern
from ._plant import PLANT
