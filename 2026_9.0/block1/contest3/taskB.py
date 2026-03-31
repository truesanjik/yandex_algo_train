import sys
import math

def main():
    n = int(input())
    limit = 2 * math.isqrt(n)
    if limit > n:
        limit = n

    best = n 

    for r in range(1, limit + 1):
        q = n // r
        rem = n % r
        if rem == 0 or rem == r or abs(2 * rem - r) <= 1:
            max_students = q if rem == 0 else q + 1
            diff = abs(r - max_students)
            if diff < best:
                best = diff

    print(best)

if __name__ == "__main__":
    main()

