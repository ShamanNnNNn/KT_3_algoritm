import sys
from collections import deque

def one():
    data = sys.stdin.buffer.read().split()
    n = int(data[0])
    prices = list(map(int, data[1:1 + n]))
    ans = [0] * n
    stack = []
    for i in range(n):
        while stack and prices[stack[-1]] < prices[i]:
            j = stack.pop()
            ans[j] = i - j
        stack.append(i)
    sys.stdout.write(' '.join(map(str, ans)))

one()

