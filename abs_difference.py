'''
Problem Description:
You are given an array of integers, arr, and a non-negative integer K. Your task is to find the number of unique pairs (a, b) from the array such that the absolute difference between a and b is exactly K.
A pair (a, b) is considered unique if the values a and b are distinct. The order of elements in a pair does not matter (i.e., (a, b) is the same as (b, a)). If the array contains duplicate numbers, each unique pair of values should be counted only once.
Example:
If arr = [1, 5, 1, 6] and K = 4:
The unique values in the array are 1, 5, 6.
The pair (1, 5) has an absolute difference of |1 - 5| = 4. This is one unique pair.
Even though 1 appears twice, the pair (1, 5) is counted only once.
If arr = [1, 1, 2, 2] and K = 0:
The unique pairs (a, b) where |a - b| = 0 means a = b.
The distinct value 1 forms the pair (1, 1).
The distinct value 2 forms the pair (2, 2).
So, there are 2 such unique pairs.
Input Format:
The input will consist of three lines:The first line contains an integer N, representing the number of elements in the array arr.The second line contains N space-separated integers, representing the elements of arr.The third line contains a single integer K.
Output Format:
Print a single integer, the total count of unique pairs (a, b) satisfying the condition.

Sample Input and Output:
Sample Input 1:
6
1 5 3 4 2 8
2

Sample Output 1:
3

Explanation:
Unique elements: 1, 2, 3, 4, 5, 8.
Pairs with absolute difference 2: (1,3), (2,4), (3,5). Total 3 pairs.
'''

from collections import Counter

n = int(input())
arr = list(map(int, input().strip().split()))
k = int(input())

unique_values = set(arr)
count = 0

if k == 0:
    freq = Counter(arr)
    for value in freq:
        if freq[value] > 1:
            count += 1
else:
    for val in unique_values:
        if val + k in unique_values:
            count += 1

print(count)
