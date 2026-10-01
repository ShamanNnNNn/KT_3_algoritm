import sys
from collections import deque

def two():
    data = sys.stdin.buffer.read().split()
    n = int(data[0]); m = int(data[1])
    grid = [data[2 + i].decode() for i in range(n)]
    sr = sc = tr = tc = -1
    for i in range(n):
        for j in range(m):
            c = grid[i][j]
            if c == 'S':
                sr, sc = i, j
            elif c == 'T':
                tr, tc = i, j
    dist = [[-1] * m for _ in range(n)]
    dist[sr][sc] = 0
    q = deque([(sr, sc)])
    while q:
        r, c = q.popleft()
        if (r, c) == (tr, tc):
            break
        for dr, dc in ((1,0),(-1,0),(0,1),(0,-1)):
            nr, nc = r + dr, c + dc
            if 0 <= nr < n and 0 <= nc < m and dist[nr][nc] == -1 and grid[nr][nc] != '#':
                dist[nr][nc] = dist[r][c] + 1
                q.append((nr, nc))
    print(dist[tr][tc])

two()


