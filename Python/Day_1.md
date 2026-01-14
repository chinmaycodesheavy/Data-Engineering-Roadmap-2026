# RULE 1: Always convert an iterator into some data type before printing it 
# INPUTTING DATA FROM UER

numbers = list(map(int, input().split()))
input() - reads a line from input as a string

> Example: "5 10 15 20"

### .split() - splits the string by spaces into a list of strings

Result: ['5', '10', '15', '20']

### map(int, ...) - applies int() function to each element

Converts each string to an integer
Result: map object with 5, 10, 15, 20

### list(...) - converts the map object to a list

Final result: [5, 10, 15, 20]

# extend() vs append()

extend() adds each element of a list as a separate element to another list
append() adds the entire new list as a separate element in the old list

# SLICE NOTATION
s = "HELLO"

s[1:4]     # "ELL"  - from index 1 to 3
s[:3]      # "HEL"  - from start to index 2
s[2:]      # "LLO"  - from index 2 to end
s[:]       # "HELLO" - entire string (copy)
s[-1]      # "O"    - last element
s[-2:]     # "LO"   - last 2 elements
s[::2]     # "HLO"  - every 2nd character
s[::-1]    # "OLLEH" - reversed!

If we say 
s[a:] -> ath index onwards including ath index 
but 
s[:a] -> everything till ath index excluding ath index

# range vs enumerate
range(len(list)) - gives you only indices
pythonfruits = ['apple', 'banana', 'cherry']

for i in range(len(fruits)):
    print(i, fruits[i])
## Output:
## 0 apple
## 1 banana
## 2 cherry
enumerate(list) - gives you both index AND value
pythonfruits = ['apple', 'banana', 'cherry']

for i, fruit in enumerate(fruits):
    print(i, fruit)
## Output:
## 0 apple
## 1 banana
## 2 cherry

# groupby() - Not similar to sql groupby()
Purpose: Groups only CONSECUTIVE identical elements (unlike SQL wehere positioning doesn't matter)

from itertools import groupby

## Consecutive duplicates
word = "HHEELLOO"
for char, group in groupby(word):
    print(char, len(list(group)))

## Output:
## H 2
## E 2
## L 2
## O 2
