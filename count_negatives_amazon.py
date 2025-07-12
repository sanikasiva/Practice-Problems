n = int(input().strip())
m = int(input().strip())

data = [list(map(int, input().strip().split())) for _ in range(n)]

count = 0
row = 0
col = m - 1

while row < n and col >= 0:
    if data[row][col] < 0:
        count += (col + 1)  
        row += 1
    else:
        col -= 1

print(count)
