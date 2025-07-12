n=int(input("Enter the limit: "))
isPrime=[True]*(n+1)

def markmultiplesFalse(a):
    for j in range (a,n+1,a):
        isPrime[j]=False

isPrime[0]=isPrime[1]=False
for i in range(2,n+1):
    if isPrime[i]:
        print(i)
        markmultiplesFalse(i)


    