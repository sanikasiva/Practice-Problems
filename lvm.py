n = int(input())
instructions = [input().strip() for _ in range(n)]

def lvm(instructions):
    stack = []
    register = 0
    pc = 0  

    while pc < len(instructions):
        step = instructions[pc].split()
        op = step[0]

        if op == "PUSH":
            stack.insert(0, int(step[1]))
        elif op == "STORE":
            register = stack.pop(0)
        elif op == "LOAD":
            stack.insert(0, register)
        elif op == "PLUS":
            a = stack.pop(0)
            b = stack.pop(0)
            stack.insert(0, a + b)
        elif op == "TIMES":
            a = stack.pop(0)
            b = stack.pop(0)
            stack.insert(0, a * b)
        elif op == "IFZERO":
            value = stack.pop(0)
            if value == 0:
                pc = int(step[1])
                continue
        elif op == "DONE":
            print(stack[0])
            return
        pc += 1

lvm(instructions)

