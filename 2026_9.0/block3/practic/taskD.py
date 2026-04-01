import sys


def main():

    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    l = 0
    current_sum = 0
    answer = 0

    for r in range(n):
        current_sum += a[r]
    
        while current_sum > k:
            current_sum -= a[l]
            l += 1
    
        if current_sum == k:
            answer += 1

    print(answer)


if __name__ == '__main__':
    main()
