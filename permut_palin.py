from collections import Counter
n=input("Enter the string: ")
c=Counter(n)
oldChar = 0

for i in c.values():
    if i%2==1:
        oldChar +=1

if oldChar >1:
    print("No permutation of can form a palindrome")
else:
    print("Yes can form a palindrome.")



