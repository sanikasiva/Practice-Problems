n, m = map(int, input().strip().split())

matrix1 = [list(map(int, input().strip().split())) for _ in range(n)]

matrix2 = [list(map(int, input().strip().split())) for _ in range(n)]

print("First Matrix:")
for row in matrix1:
    print(*row)

print("Second Matrix:")
for row in matrix2:
    print(*row)

sum_matrix = []
for i in range(n):
    row = []
    for j in range(m):
        row.append(matrix1[i][j] + matrix2[i][j])
    sum_matrix.append(row)

print("Sum of the two matrices is:")
for row in sum_matrix:
    print(*row)
