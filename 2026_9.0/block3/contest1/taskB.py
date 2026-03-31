import sys


def main():

    n = int(input().strip())
    s = input().strip().split()
    a = list(map(int, s))
    l = 0 
    ans = 0
    count = {}

    for r in range(n):
        count[a[r]] = count.get(a[r], 0) + 1

        while (len(count) > 2):
            count[a[l]] -= 1
            if count[a[l]] == 0:
                del count[a[l]]
            l += 1
        
        if len(count) == 2:
            ans = max(ans, r - l + 1)

    print(ans)



if __name__ == '__main__':
    main()
