# Problem: F - Covered Points Count - https://codeforces.com/gym/589822/problem/F

n = int(input())
events = []

# Read the segments and create events for the sweep line
for _ in range(n):
    l, r = map(int, input().split())
    events.append((l, 1))  
    events.append((r + 1, -1))  

# Sort events: first by coordinate, then by type (end before start if same coordinate)
events.sort()

# To count the number of points covered by exactly k segments
cnt = [0] * (n + 1)

current_coverage = 0
last_position = -1

# Sweep through the events
for position, type in events:
    if last_position != -1 and current_coverage > 0:
        # Count the number of integer points between last_position and current position
        cnt[current_coverage] += position - last_position

    # Update the current coverage
    current_coverage += type
    last_position = position

# print(cnt)

print(*cnt[1:])
