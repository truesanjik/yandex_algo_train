import sys


def main():

    data = input().split()
    ans = []
    for w in data:
        
        i = 0
        j = 0
        chars = []
        p = 0
        l = len(w)
        while p < l and w[p] == "'":
            i += 1
            p += 1
        while p < l and w[p].islower():
            chars.append(w[p])
            p += 1
        while p < l and w[p] == "'":
            j += 1
            p += 1
        s = ''.join(chars)
        subs = s[i:len(s)-j]
        ans.append(subs)
    result = ''.join(ans)
    print(result)


if __name__ == '__main__':
    main()
