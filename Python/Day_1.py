##Leanings of the Day 1: Python Basics##
# 1. replicating C++ for(int i = 0; i < n; i++) in Python
n = 10
for i in range(n):
    print(i)
# 2. Wanting to print from 1 to n instead of 0 to n-1
for i in range(1, n + 1):
    print(i)
# 3. If you want to print without using string tools, something like 1234567...n
for i in range(1, n + 1):
    print(i, end='')

# 4. Taking input from user and printing al 2-letter word permutations(or combinations)
#    of that word lexicographically
# Enter your code here. Read input from STDIN. Print output to STDOUT
from itertools import permutations
S,k = input().split() # Remove any extra whitespace/newlines

k = int(k)
S = sorted(S)
permutations_list = list(permutations((S),k))
for permutation in permutations_list:
    print(''.join(permutation))

# 5. Crazyyy Discovery - extend vs append for lists
list1 = [1, 2, 3]
list2 = [4, 5, 6]
list1.append(list2)
#print(list1)  # Output: [1, 2, 3, [4, 5, 6]]
list1 = [1, 2, 3]   # Resetting list1
list1.extend(list2)
#print(list1)  # Output: [1, 2, 3, 4, 5, 6]


