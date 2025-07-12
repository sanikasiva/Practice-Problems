prices = list(map(int, input().strip().split(',')))

minp = prices[0]
max_profit = 0

for price in prices[1:]:
    if price < minp:
        minp = price
    else:
        profit = price - minp
        max_profit = max(max_profit, profit)

print(max_profit)
