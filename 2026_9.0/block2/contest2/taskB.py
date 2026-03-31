import sys


def main():

    with open('2026_9.0/block2/contest2/input.txt', 'r') as f:
        s = f.readline().strip()
    n = len(s)

    freq = [0] * 26
    for ch in s:
        freq[ord(ch) - ord('a')] += 1
    max_freq = max(freq)
    if max_freq >= n // 2 + 1: ans = 1
    else:
        m = []
        for i in range(26):
            if freq[i] == max_freq:
                m.append(chr(i + ord('a')))
        
    
    print(*m)


if __name__ == '__main__':
    main()
