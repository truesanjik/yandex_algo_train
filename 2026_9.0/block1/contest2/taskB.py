import sys

def folds(a: int, b: int):
    if a <= b:
        return 0
    cnt = 0
    while a > b:
        b *= 2
        cnt += 1
    return cnt

def main():

    data = input().split()
    n = int(data[0])
    m = int(data[1])
    h = int(data[2])
    w = int(data[3])

    ans = min(
        folds(n, h) + folds(m, w),
        folds(n, w) + folds(m, h)
    )
    print(ans)

if __name__ == '__main__':
    main()
