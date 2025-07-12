n = int(input("Enter the number of snack packets: "))
k = int(input("Enter the break time: "))
ts = list(map(int, input("Enter the snack scores: ").strip().split()))

window_sum = sum(ts[:k])
max_score = window_sum

for i in range(k, n):
    window_sum += ts[i] - ts[i - k]
    max_score = max(max_score, window_sum)

print(max_score)
