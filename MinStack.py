stack = []
min_stack = []

q = int(input())
for i in range(q):
    query = input().strip().split()
    if query[0] == '0':
        x = int(query[1])
        stack.append(x)
        if not min_stack or x <= min_stack[-1]:
            min_stack.append(x)
    elif query[0] == '1':
        popped = stack.pop()
        if popped == min_stack[-1]:
            min_stack.pop()
    elif query[0] == '2':
        print(stack[-1])
    elif query[0] == '3':
        print(min_stack[-1])
