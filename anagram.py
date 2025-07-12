'''
Problem: Group Anagrams

Problem Description:
Given an array (or list) of strings strs, your task is to group the anagrams together.
An anagram is a word or phrase formed by rearranging the letters of another, typically using all the original letters exactly once. For example, "eat", "tea", and "ate" are anagrams of each other.
The order of the output groups and the order of the strings within each group does not matter.
Input Format:The first line contains an integer N, representing the number of strings in the input array strs.The second line contains N space-separated strings, which are the elements of strs.
Output Format:
Print the groups of anagrams. Each group should be printed on a new line. The strings within each group should be space-separated. The order of the groups and the strings within each group doesn't matter.
Constraints:
strs[i] consists of lowercase English letters.
Test Cases:
Test Case 1: Basic Anagrams
Input:6

eat tea tan ate nat bat
Expected Output (order might vary):eat tea ate
tan nat
bat
Test Case 2: No Anagrams (Each string is its own group)
Input:3 a b c
Expected Output (order might vary):a
b
c
Explanation: No string has another anagram in the input.
Test Case 3: Empty String
Input:1
""
Expected Output:""
Explanation: The empty string is its own anagram group.
Sample Input and Output:
Sample Input 1:
5

listen silent elbow below ice

Sample Output 1:
listen silent
elbow below
ice
'''



n = int(input())
words = input().strip().split()
anagram = {}
for x in words:
    key = "".join(sorted(x))
    if key in anagram:
        anagram[key].append(x)
    else:
        anagram[key] = [x]

for group in anagram.values():
    print(" ".join(group))
