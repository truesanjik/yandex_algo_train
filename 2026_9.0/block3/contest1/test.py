import sys

n = int(sys.stdin.readline())

if n < 0:
    print(-2)
    sys.exit()

s = sys.stdin.readline().strip()

prefix_sum = 0
count = {0: 1}  # сумма 0 уже встречалась (пустой префикс)
answer = 0

for c in s:
    if c == 'a':
        prefix_sum += 1
    else:
        prefix_sum -= 1

    if prefix_sum in count:
        answer += count[prefix_sum]
        count[prefix_sum] += 1
    else:
        count[prefix_sum] = 1

print(answer)