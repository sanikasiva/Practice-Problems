N, D = list(map(int, input().strip().split()))
weight = list(map(int, input().strip().split()))
weight.sort()
add = sum(weight[-D:])
print(add)