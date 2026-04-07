import sys


def main():

    n, m, k = map(int, input().split())
    w = [""] * n
    cur = 0
    paste = ""
    
    for _ in range(m):
        com = input().strip()

        if len(com) == 1:
            w[cur] += com
        
        elif com == "Backspace":
            if w[cur] != "":
                w[cur] = w[cur][:-1]
        
        elif com == "Copy":
            paste = w[cur][-k:]

        elif com == "Paste":
            w[cur] += paste

        elif com == "Next":
            cur = (cur + 1) % n
    ans = w[cur][-k:]
    if ans != "":
        print(ans)
    else: 
        print("Empty")


if __name__ == '__main__':
    main()
