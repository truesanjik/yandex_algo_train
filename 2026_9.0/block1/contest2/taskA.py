import sys

def main():
    n = int(input().strip())
    s = input().strip()
    # хотя n можно не использовать, но для проверки
    max_l = 0
    cur = 0
    prev = None
    for ch in s:
        if ch not in ('a', 'h'):
            cur = 0
            prev = None
        else:
            if prev is None:
                cur = 1
            elif ch != prev:
                cur += 1
            else:
                cur = 1
            prev = ch
        if cur > max_l:
            max_l = cur
    print(max_l)

if __name__ == "__main__":
    main()