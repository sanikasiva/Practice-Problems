#Sieving Method
n=int(input("Enter the limit: "))
size=(n-3)//2 +1
isPrime = [True]*size
primes=[2]

def markmultiplesFalse(a):
    p = 2*a + 3
    for j in range (2*a**2 + 6*a + 3, size, p):
        isPrime[j]=False
        
for i in range(size):
    if isPrime[i]:
        primes.append(2*i+3)
        markmultiplesFalse(i)
print(len(primes))


'''
val=    0 1 2 3 4 5 6 7
idx=    0 1 2 3 4 5 6 7
idx1=   3 5 7 9 11 13 15
'''
    