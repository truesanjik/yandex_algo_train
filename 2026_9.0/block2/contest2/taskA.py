import sys


def main():

    n = int(input())
    
    max_l = -10**9
    min_r = 10**18

    for _ in range(n):
        x, d = map(int, input().split())
        l = x - d
        r = x + d
        if l > max_l:
            max_l = l
        if r < min_r:
            min_r = r

    if max_l <= min_r:
        print(min_r)
    else:
        print(-1)




if __name__ == '__main__':
    main()
