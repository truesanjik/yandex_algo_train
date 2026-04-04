import sys


def main():


    s = input().strip()

    n = [ord(c) - ord('A') for c in s]
    l = len(n)
    avg = (2 * sum(n) + l - 1) // (2 * l)
    best_p = max(0, max(n) - 1)  
    ans = max(best_p, avg)

    print(chr(ans + ord('A')))
    


if __name__ == '__main__':
    main()
