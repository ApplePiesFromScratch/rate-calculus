/* test_core.c: the C core against the book's numbers, each beside a planted wrong answer that must be refused. */
#include <stdio.h>
#include "reading.h"

static int good, bad;
static void check(const char *name, int right, int planted_wrong) {
  if (right && !planted_wrong) good++; else { bad++; printf("FAIL %s\n", name); }
}

int main(void) {
  rc_reading x = rc_isolate(4, 1), y, z, one = rc_isolate(1, 0); rc_frac f; rc_status s; rc_carry c; int i, held = 1; int64_t sum = 0;
  rc_mix(x, x, &y);
  check("mix (4,1)*(4,1) = (16,8)", rc_req(y, rc_isolate(16, 8)), rc_req(y, rc_isolate(16, 1)));
  s = rc_rate(y, x, &f);
  check("rate(x*x, x) = 8", s == RC_OK && rc_feq(f, rc_f(8, 1)), rc_feq(f, rc_f(1, 8)));
  s = rc_rate(rc_isolate(8, 2), rc_isolate(15, 0), &f);
  check("rate against a still reading refuses: theta", s == RC_THETA, s == RC_OK);
  s = rc_div(one, rc_isolate(3, 1), &z);
  check("1/x at 3 = (1/3, -1/9)", s == RC_OK && rc_req(z, rc_R(rc_f(1, 3), rc_f(-1, 9))), rc_req(z, rc_R(rc_f(1, 3), rc_f(1, 9))));
  s = rc_div(one, rc_isolate(0, 1), &z);
  check("1/x at 0 refuses: no quotient", s == RC_NO_QUOTIENT, s == RC_OK);
  rc_mix(rc_isolate(3, 1), rc_isolate(3, 1), &y); rc_add(y, one, &y); rc_sub(rc_isolate(3, 1), one, &z); rc_div(y, z, &z);
  check("(x*x+1)/(x-1) at 3 = (5, 1/2)", rc_req(z, rc_R(rc_f(5, 1), rc_f(1, 2))), rc_req(z, rc_R(rc_f(5, 1), rc_f(2, 1))));
  s = rc_mix(rc_isolate(INT64_MAX / 2, 1), rc_isolate(4, 1), &z);
  check("a product past int64 refuses: overflow", s == RC_OVERFLOW, s == RC_OK);
  check("mouth 5/2 = 2, -7/2 = -4, -1/2 = 0", rc_mouth(5, 2) == 2 && rc_mouth(-7, 2) == -4 && rc_mouth(-1, 2) == 0, rc_mouth(-7, 2) == -3);
  rc_carry_init(&c, 4, 3);
  for (i = 0; i < 100000; i++) { sum += rc_carry_tick(&c); held = held && rc_carry_books(&c); }
  check("carry 4/3 for 100000 ticks: count 133333, books held every tick", sum == 133333 && held, sum == 133334);
  printf("C core: %d passed, %d failed (each with a planted wrong answer refused)\n", good, bad);
  return bad ? 1 : 0;
}
