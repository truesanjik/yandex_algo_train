import sys


def main():

    n, m = map(int, input().split())
    a = [input() for _ in range(n)]
    vis = [[0]*m for _ in range(n)]
    ans = 0


    for i in range(n):
        for j in range(m):
            if a[i][j] == '#' and not vis[i][j]:
                st = [(i, j)]
                vis[i][j] = 1
                cells = []
            
                while st:
                    x, y = st.pop()
                    cells.append((x, y))
                
                    for dx, dy in ((1,0),(-1,0),(0,1),(0,-1)):
                        qx, qy = x + dx, y + dy
                        if 0 <= qx < n and 0 <= qy < m and a[qx][qy] == '#' and not vis[qx][qy]:
                            vis[qx][qy] = 1
                            st.append((qx, qy))
            
                xs = [x for x, _ in cells]
                ys = [y for _, y in cells]
            
                h = max(xs) - min(xs) + 1
                w = max(ys) - min(ys) + 1
            
                if h == w and len(cells) == h*w:
                    ans += 1

    print(ans)

if __name__ == '__main__':
    main()
