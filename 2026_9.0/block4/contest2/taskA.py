import sys


def main():


    s = input().strip()
    n = len(s)

    if n == 0:
        print("YES")
        return
    
    brackets = {
        ')': '(',
        ']': '[',
        '}': '{'
    } 

    for i in range(n):
        st = []
        shift = s[i:] + s[:i]
        for c in shift:
            if c in '([{':
                st.append(c)
            else:
                if not st or st[-1] != brackets[c]:
                    break
                st.pop()
        
        else:
            if not st:
                print("YES")
                return
    print("NO")



if __name__ == '__main__':
    main()
