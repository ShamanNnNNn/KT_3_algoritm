import sys
from collections import deque

def six():
    data = sys.stdin.buffer.read().split()
    n = int(data[0])
    nums = list(map(int, data[1:2 + n]))

    slow = nums[0]
    fast = nums[0]
    while True:
        slow = nums[slow]
        fast = nums[nums[fast]]
        if slow == fast:
            break

    slow = nums[0]
    while slow != fast:
        slow = nums[slow]
        fast = nums[fast]

    print(slow)

six()