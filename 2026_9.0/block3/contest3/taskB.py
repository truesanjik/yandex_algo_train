import sys
input = sys.stdin.readline

n, k = map(int, input().split())

if n < 0 or k < 0:
    print(-2)
    exit()

a = list(map(int, input().split()))

prefix = 0
ans = 0

# для каждого остатка — минимальный prefix
from collections import defaultdict
best = dict()

# глобальные минимумы
min1 = (0, 0)  # (prefix, mod)
min2 = (float('inf'), -1)

best[0] = 0

for x in a:
    prefix += x
    mod = prefix % k

    # ищем лучший кандидат
    candidate = None

    if min1[1] != mod:
        candidate = min1[0]
    elif min2[0] != float('inf'):
        candidate = min2[0]

    if candidate is not None:
        ans = max(ans, prefix - candidate)

    # обновляем best
    if mod not in best or prefix < best[mod]:
        best[mod] = prefix

        # обновляем min1/min2
        if prefix < min1[0]:
            if min1[1] != mod:
                min2 = min1
            min1 = (prefix, mod)
        elif prefix < min2[0] and mod != min1[1]:
            min2 = (prefix, mod)

print(ans)