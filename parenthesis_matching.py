s = input().strip()
balance = 0

for ch in s:
    if ch == '{':
        balance += 1
    elif ch == '}':
        balance -= 1
        if balance < 0:
            print("Not Matching")
            break
else:
    if balance == 0:
        print("Matching")
    else:
        print("Not Matching")
