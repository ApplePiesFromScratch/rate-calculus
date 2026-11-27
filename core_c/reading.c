#include "reading.h"

static int64_t gcd64(int64_t a, int64_t b) { if (a < 0) a = -a; if (b < 0) b = -b; while (b) { int64_t t = a % b; a = b; b = t; } return a ? a : 1; }
static int mul_ok(int64_t a, int64_t b, int64_t *out) { return !__builtin_mul_overflow(a, b, out); }
static int add_ok(int64_t a, int64_t b, int64_t *out) { return !__builtin_add_overflow(a, b, out); }

rc_frac rc_f(int64_t num, int64_t den) {
  rc_frac f; int64_t g = gcd64(num, den);
  if (den < 0) { num = -num; den = -den; }
  f.num = num / g; f.den = den / g; return f;
}
rc_reading rc_isolate(int64_t value, int64_t rate) { rc_reading r; r.value = rc_f(value, 1); r.rate = rc_f(rate, 1); return r; }
rc_reading rc_R(rc_frac value, rc_frac rate) { rc_reading r; r.value = value; r.rate = rate; return r; }

static rc_status fmul(rc_frac a, rc_frac b, rc_frac *o) {
  int64_t g1 = gcd64(a.num, b.den), g2 = gcd64(b.num, a.den), n, d;   /* cross-reduce first, so fewer products overflow */
  if (!mul_ok(a.num / g1, b.num / g2, &n) || !mul_ok(a.den / g2, b.den / g1, &d)) return RC_OVERFLOW;
  *o = rc_f(n, d); return RC_OK;
}
static rc_status fadd(rc_frac a, rc_frac b, rc_frac *o) {
  int64_t g = gcd64(a.den, b.den), x, y, n, d;
  if (!mul_ok(a.num, b.den / g, &x) || !mul_ok(b.num, a.den / g, &y) || !add_ok(x, y, &n) || !mul_ok(a.den, b.den / g, &d)) return RC_OVERFLOW;
  *o = rc_f(n, d); return RC_OK;
}
static rc_frac fneg(rc_frac a) { a.num = -a.num; return a; }
static rc_status fdiv(rc_frac a, rc_frac b, rc_frac *o) {
  rc_frac inv; if (b.num == 0) return RC_NO_QUOTIENT;
  inv = rc_f(b.den, b.num); return fmul(a, inv, o);
}

rc_status rc_mix(rc_reading a, rc_reading b, rc_reading *out) {
  rc_frac v, s1, s2, r; rc_status e;
  if ((e = fmul(a.value, b.value, &v)) || (e = fmul(a.rate, b.value, &s1)) || (e = fmul(a.value, b.rate, &s2)) || (e = fadd(s1, s2, &r))) return e;
  out->value = v; out->rate = r; return RC_OK;
}
rc_status rc_add(rc_reading a, rc_reading b, rc_reading *out) {
  rc_frac v, r; rc_status e;
  if ((e = fadd(a.value, b.value, &v)) || (e = fadd(a.rate, b.rate, &r))) return e;
  out->value = v; out->rate = r; return RC_OK;
}
rc_status rc_sub(rc_reading a, rc_reading b, rc_reading *out) { return rc_add(a, rc_R(fneg(b.value), fneg(b.rate)), out); }
rc_status rc_div(rc_reading a, rc_reading b, rc_reading *out) {
  rc_frac q, x, y, top, v2sq, s; rc_status e;
  if (b.value.num == 0) return RC_NO_QUOTIENT;
  if ((e = fdiv(a.value, b.value, &q)) || (e = fmul(a.rate, b.value, &x)) || (e = fmul(b.rate, a.value, &y)) ||
      (e = fadd(x, fneg(y), &top)) || (e = fmul(b.value, b.value, &v2sq)) || (e = fdiv(top, v2sq, &s))) return e;
  out->value = q; out->rate = s; return RC_OK;
}
rc_status rc_rate(rc_reading a, rc_reading b, rc_frac *out) {
  if (b.rate.num == 0) return RC_THETA;
  return fdiv(a.rate, b.rate, out);
}
int rc_feq(rc_frac a, rc_frac b) { return a.num == b.num && a.den == b.den; }
int rc_req(rc_reading a, rc_reading b) { return rc_feq(a.value, b.value) && rc_feq(a.rate, b.rate); }

int64_t rc_mouth(int64_t n, int64_t d) {
  int neg = n < 0; int64_t m = neg ? -n : n, q = m / d, r = m % d;
  if (2 * r > d || (2 * r == d && (q & 1))) q++;
  return neg ? -q : q;
}

void rc_carry_init(rc_carry *c, int64_t n, int64_t d) { c->n = n; c->d = d; c->acc = 0; c->count = 0; c->ticks = 0; }
int64_t rc_carry_tick(rc_carry *c) {
  int64_t out = 0; c->acc += c->n;
  while (c->acc >= c->d) { c->acc -= c->d; out++; }   /* while, not if: one tick can owe several pulses */
  c->count += out; c->ticks++; return out;
}
int rc_carry_books(const rc_carry *c) { return c->d * c->count + c->acc == c->n * c->ticks && c->acc >= 0 && c->acc < c->d; }
