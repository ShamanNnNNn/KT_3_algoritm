import sys
from collections import deque

def five():
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

    INF = -1
    dist = [[[-1] * 1024 for _ in range(m)] for _ in range(n)]
    dist[sr][sc][0] = 0
    q = deque([(sr, sc, 0)])

    def key_bit(ch):
        return 1 << (ord(ch) - ord('a'))

    def door_bit(ch):
        return 1 << (ord(ch) - ord('A'))

    while q:
        r, c, mask = q.popleft()
        d = dist[r][c][mask]
        if r == tr and c == tc:
            print(d)
            return
        for dr, dc in ((1,0),(-1,0),(0,1),(0,-1)):
            nr, nc = r + dr, c + dc
            if 0 <= nr < n and 0 <= nc < m:
                ch = grid[nr][nc]
                if ch == '#':
                    continue
                nmask = mask
                if 'a' <= ch <= 'j':
                    nmask |= key_bit(ch)
                elif 'A' <= ch <= 'J':
                    if not (mask & door_bit(ch)):
                        continue
                if dist[nr][nc][nmask] == -1:
                    dist[nr][nc][nmask] = d + 1
                    q.append((nr, nc, nmask))

    print(-1)

five()

