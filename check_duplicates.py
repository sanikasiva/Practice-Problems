n = int(input().strip())

nums = list(map(int, input().strip().split()))


if len(set(nums)) < n:
    print("true")
else:
    print("false")

