MOD = 10**9 + 7

n = int(input())
a = list(map(int, input().split()))

total = sum(a) % MOD
left_sum = 0
ans = 0

for j in range(n):
    right_sum = (total - left_sum - a[j]) % MOD
    ans = (ans + a[j] * left_sum % MOD * right_sum) % MOD
    left_sum = (left_sum + a[j]) % MOD

print(ans)