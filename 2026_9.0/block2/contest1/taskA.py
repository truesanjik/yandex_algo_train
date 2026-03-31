import sys

def main():
    data = sys.stdin.read().strip().splitlines()
    if not data:
        return
    n = int(data[0].strip())
    if n < 0:
        print(-2)
        return
    players = []
    idx = 1
    for i in range(n):
        players.append(data[idx].strip())
        idx += 1
    m = int(data[idx].strip())
    idx += 1
    scores = {name: 0 for name in players}
    curr_a, curr_b = 0, 0
    for i in range(m):
        line = data[idx].strip()
        idx += 1
        if not line:
            continue
        # формат "a:b name"
        parts = line.split()
        if len(parts) != 2:
            continue
        score_part, name = parts
        a_str, b_str = score_part.split(':')
        a = int(a_str)
        b = int(b_str)
        delta_a = a - curr_a
        delta_b = b - curr_b
        scores[name] += delta_a + delta_b
        curr_a, curr_b = a, b
    # найти максимальную сумму
    max_score = max(scores.values())
    # найти любого с таким счетом
    for name, sc in scores.items():
        if sc == max_score:
            print(f"{name} {max_score}")
            break

if __name__ == "__main__":
    main()