n = int(input())
shows = []
for _ in range(n):
    start, end = map(int, input().split())
    shows.append((end, start))
shows.sort()
count = 0
last_end = 0

for end, start in shows:
    if start >= last_end:
        count += 1
        last_end = end

print(count)
