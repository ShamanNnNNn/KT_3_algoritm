import sys
from collections import deque

def four():
    data = sys.stdin.buffer.read().split()
    n = int(data[0]); m = int(data[1])
    rows = [data[2 + i].decode() for i in range(n)]

    heights = [0] * m
    best = 0
    for i in range(n):
        for j in range(m):
            if rows[i][j] == '1':
                heights[j] += 1
            else:
                heights[j] = 0
        stack = []
        for j in range(m + 1):
            h = heights[j] if j < m else 0
            while stack and heights[stack[-1]] > h:
                top = stack.pop()
                left = stack[-1] + 1 if stack else 0
                area = heights[top] * (j - left)
                if area > best:
                    best = area
            stack.append(j)
    print(best)

four()


