N, K = map(int, input().split())
kick_power = list(map(int, input().split()))

def max_kick_in_windows(arr, k):
    result = []
    for i in range(len(arr) - k + 1):
        window = arr[i:i + k]
        result.append(max(window))
    return result

output = max_kick_in_windows(kick_power, K)
print(*output)