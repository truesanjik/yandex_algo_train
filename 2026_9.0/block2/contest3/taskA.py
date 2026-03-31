import sys


def main():

    s = input().strip()


    digs = list(map(int, s))
    digs.sort()

    m1 = []
    m2 = []

    for i, d in enumerate(digs):
        if d % 3 == 1:
            m1.append(i)
        elif d % 3 == 2:
            m2.append(i)

    fullsum = sum(digs)
    r = fullsum % 3

    if r == 1:
        if len(m1) >= 1:
            for i in m1[:1]:
                digs[i] = -1
        elif len(m2) >= 2:
            for i in m2[:2]:
                digs[i] = -1
    elif r == 2:
        if len(m2) >= 1:
            for i in m2[:1]:
                digs[i] = -1
        elif len(m1) >=2:
            for i in m1[:2]:
                digs[i] = -1

    ans = [d for d in digs if d != -1]
    ans.sort(reverse=True)
    print("".join(map(str, ans)))


if __name__ == '__main__':
    main()
