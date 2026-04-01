import sys


def main():

    n = int(input())
    a = list(map(int, input().split()))
    q = int(input())
    x0 = int(input())
    mod = 10**9 + 7
    pref = [0] * (n + 1)
    for i in range(n):
        pref[i + 1] = pref[i] + a[i]

    x = x0
    ans = 0


    for i in range(q):
        x1 = (11173 * x + 1) % mod
        l = min(x % n, x1 % n)
        r = max(x % n, x1 % n)
        ans += pref[r + 1] - pref[l]
        ans %= mod
        x = (11173 * x1 + 1) % mod

    print(ans % mod)


if __name__ == '__main__':
    main()
