import sys


def main():



    cases = int(input())
    for _ in range(cases):
        n, d = map(int, input().split())
        
        t = [0] * (n)
        k = [0] * (n)
        
        for i in range(n):
            t[i], k[i] = map(int, input().split())
        w_s = [0] * (n + 1)
        for i in range(n):
            w_s[i + 1] = w_s[i] + k[i]

        ans = n + 1
        lim = sys.maxsize

        for i in range(n - 1, -1, -1):
            temp = t[i] - w_s[i]
            lim = min(lim, temp)
            if lim >= d:
                ans = i + 1 
    
        print(ans)

if __name__ == '__main__':
    main()
