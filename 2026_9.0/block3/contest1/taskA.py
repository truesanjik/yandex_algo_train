import sys


def main():

    n = int(input().strip())
    s = input().strip()

    ans = 0
    dic = {0: 1}
    pre_s = 0

    for c in s:
        if c  == 'a':
            pre_s += 1
        else:
            pre_s -= 1
        
        if pre_s in dic:
            ans += dic[pre_s]
            dic[pre_s] += 1
        else:
            dic[pre_s] = 1
    print(ans)



if __name__ == '__main__':
    main()
