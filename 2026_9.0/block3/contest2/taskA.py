import sys


def main():


    s = input().strip()
    x, y = 0, 0 
    cells = {(x, y): 1}
        
    for c in s:
        if c == 'U':
            y += 1
        elif c == 'D':
            y -= 1
        elif c == 'L':
            x -= 1
        elif c == 'R':
            x += 1
        cells[(x, y)] = cells.get((x, y), 0) + 1

    ans = 0
    for c in cells.values():
        if c > 1:
            ans += 1
    print(ans)
    


if __name__ == '__main__':
    main()
