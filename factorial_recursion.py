def factorial(n):
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)

n=int(input())
if n < 0:
    print("Factorial is not defined for negative numbers.")
else:
    print(factorial(n))