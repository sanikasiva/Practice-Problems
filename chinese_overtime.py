n = int(input())
days = list(map(int, input().strip().split()))
nights = list(map(int, input().strip().split()))
x = int(input())

def overtime(n, days, nights, x):
    days.sort()
    nights.sort(reverse=True)

    total_overtime = 0

    for i in range(n):
        total_minutes = days[i] + nights[i]
        if total_minutes > x:
            total_overtime += (total_minutes - x) * 100

    return total_overtime

print(overtime(n, days, nights, x))
