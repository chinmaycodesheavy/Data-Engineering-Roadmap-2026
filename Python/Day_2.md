# SOLVED 3 DSA PROBLEMS
## Tuple is immutable and List is mutable but when List is inside a tuple - that list is also mutable making tuble shallow immutable
## 1. Two sum
Learnings - You are bothered with the index. Always check for index of (target - nums[i])
At any index, if (target-nums[i]) is already seen by you, it would be there in your hashmap as a key, just return its index.
If not, make the number at that index as the key and assign that index as its value

## 2. Contains Duplicate
Learnings - Simply use set(especially whenever checking for duplicates). If it is already there, remember to use .add() for set. Even in the 2 sum variant where u just want to know if u have seen that particular value before, it's the best approach.
Set membership is O(1) on average because Python uses a hash table, allowing direct access via hash computation rather than linear scanning,hence making it faster than list
num in list   # O(n)
num in set    # O(1)

## 3. Best Time to Buy and Sell Stock
Learnings - Max/min problem can be greedy or dp. Try Greedy approach. At each point selecting the best possible option. Here we just keep a track of
min_price (first)
max_profit (second)
at each point
Greedy - An overall optimal solution can be reached by choosing the oprimal choice at each step
A problem has an optimal substructure if an optimal solution to the entire problem contains the optimal solutions to the sub problems.
Can use greedy for fractional knapsack but not knapsack(requires DP)