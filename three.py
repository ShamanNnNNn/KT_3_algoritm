import sys
from collections import deque

def three():
    data = sys.stdin.buffer.read().split()
    n = int(data[0]); start = int(data[1])
    nxt = [0] * (n + 1)
    for i in range(1, n + 1):
        v = int(data[1 + i])
        nxt[i] = v

    def step(x):
        return nxt[x] if x != -1 else -1

    slow = start
    fast = start
    while True:
        slow = step(slow)
        fast = step(step(fast))
        if slow == -1 or fast == -1:
            print("NO")
            return
        if slow == fast:
            print("YES")
            return

three()

