import sys


def main():

    n = int(input().strip())
    a = list(map(int, input().split()))

    b = []
    b.append(0)
    for i in range(1, n + 1):
        b.append(b[i - 1] + a[i - 1])

    print(*b[1:])

if __name__ == '__main__':
    main()


# n = int(input())
# a = list(map(int, input().split()))

# b = []
# current_sum = 0

# for x in a:
#     current_sum += x
#     b.append(current_sum)

# print(*b)