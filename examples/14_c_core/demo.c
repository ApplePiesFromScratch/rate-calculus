/* demo.c: the book's first moves in C, whole numbers only, with every refusal named. */
#include <stdio.h>
#include "reading.h"

static void show(const char *label, rc_reading r) {
  printf("%s(%lld/%lld, %lld/%lld)\n", label, (long long)r.value.num, (long long)r.value.den, (long long)r.rate.num, (long long)r.rate.den);
}

int main(void) {
  rc_reading x = rc_isolate(4, 1), y, q; rc_frac f; rc_status s; rc_carry c; int i;
  rc_mix(x, x, &y); show("mix((4,1),(4,1)) = ", y);
  rc_rate(y, x, &f); printf("rate(x*x, x) = %lld/%lld\n", (long long)f.num, (long long)f.den);
  s = rc_rate(rc_isolate(8, 2), rc_isolate(15, 0), &f); printf("rate(tub, candle): %s\n", s == RC_THETA ? "theta (isolator r=0)" : "answer");
  rc_div(rc_isolate(1, 0), rc_isolate(3, 1), &q); show("1/x at 3 = ", q);
  s = rc_div(rc_isolate(1, 0), rc_isolate(0, 1), &q); printf("1/x at 0: %s\n", s == RC_NO_QUOTIENT ? "no quotient" : "answer");
  s = rc_mix(rc_isolate(INT64_MAX / 2, 1), rc_isolate(4, 1), &q); printf("a product past int64: %s\n", s == RC_OVERFLOW ? "refused (overflow)" : "wrapped");
  printf("mouth: 5/2 -> %lld, -7/2 -> %lld, 7/2 -> %lld\n", (long long)rc_mouth(5, 2), (long long)rc_mouth(-7, 2), (long long)rc_mouth(7, 2));
  rc_carry_init(&c, 7, 3); printf("carry 7/3:");
  for (i = 0; i < 6; i++) printf(" %lld", (long long)rc_carry_tick(&c));
  printf(" | books %s\n", rc_carry_books(&c) ? "held" : "BROKEN");
  return 0;
}
