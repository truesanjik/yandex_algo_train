import sys


def main():


    n = int(input())
    a = list(map(int, input().split()))

    if n == 1:
        print(-1)
        exit()

    a = [x - 1 for x in a]

    bad = [False] * n

    for i in range(n):
        k = (a[i] - i) % n
        bad[k] = True

    for k in range(n):
        if not bad[k]:
            print(k)
            break
    else:
        print(-1)



if __name__ == '__main__':
    main()
