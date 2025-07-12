n = int(input().strip())
nums = list(map(int, input().strip().split()))
target = int(input().strip())

l = 0
r = n-1
found = False

while l<r:
    current_sum = nums[l] + nums[r]
    if current_sum == target:
        found = True
        break
    elif current_sum < target:
        l+=1
    else:
        r-=1

if found:
    print("Yes")
else:
    print("No")
