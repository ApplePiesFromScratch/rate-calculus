/* reading.h: the book's alphabet and moves in C99, whole numbers only (no float anywhere).
 * A fraction is (num, den) with den > 0, kept in lowest terms. A Reading is (value, rate), two fractions.
 * Moves: rc_isolate, rc_mix, rc_add, rc_sub, rc_div (derived), rc_rate. Refusals are named flags, never host errors:
 *   RC_THETA        rate() against a reading whose rate is 0
 *   RC_NO_QUOTIENT  division by a reading whose value is 0
 *   RC_OVERFLOW     a product left the int64 alphabet (the machine refuses rather than wrap)
 * Whole-number tools: rc_mouth (nearest, half to even, mirror-true) and rc_carry (n/d as whole pulses with books). */
#ifndef READING_H
#define READING_H
#include <stdint.h>

typedef struct { int64_t num, den; } rc_frac;
typedef struct { rc_frac value, rate; } rc_reading;
typedef enum { RC_OK = 0, RC_THETA, RC_NO_QUOTIENT, RC_OVERFLOW } rc_status;

rc_frac rc_f(int64_t num, int64_t den);              /* den != 0; reduced, den > 0 */
rc_reading rc_isolate(int64_t value, int64_t rate);  /* isolate(v, r) for whole v, r */
rc_reading rc_R(rc_frac value, rc_frac rate);
rc_status rc_mix(rc_reading a, rc_reading b, rc_reading *out);   /* (v1*v2, r1*v2 + v1*r2) */
rc_status rc_add(rc_reading a, rc_reading b, rc_reading *out);
rc_status rc_sub(rc_reading a, rc_reading b, rc_reading *out);
rc_status rc_div(rc_reading a, rc_reading b, rc_reading *out);   /* (v1/v2, (r1*v2 - r2*v1)/v2^2) */
rc_status rc_rate(rc_reading a, rc_reading b, rc_frac *out);     /* r_a / r_b */
int rc_feq(rc_frac a, rc_frac b);
int rc_req(rc_reading a, rc_reading b);
int64_t rc_mouth(int64_t n, int64_t d);              /* d > 0 */

typedef struct { int64_t n, d, acc, count, ticks; } rc_carry;
void rc_carry_init(rc_carry *c, int64_t n, int64_t d);   /* n >= 0, d > 0 */
int64_t rc_carry_tick(rc_carry *c);                      /* pulses leaving this tick */
int rc_carry_books(const rc_carry *c);                   /* d*count + acc == n*ticks and 0 <= acc < d */
#endif
