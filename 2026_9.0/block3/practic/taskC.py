import sys


def main():


    n = int(input())
    a = list(map(int, input().split()))
    cur = a[0]
    ans = a[0]

    for i in range(1, n):
        cur = max(a[i], cur + a[i])
        ans = max(ans, cur)

    print(ans)

if __name__ == '__main__':
    main()
