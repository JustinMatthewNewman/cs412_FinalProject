"""
    Exact Solution to Max Knapsack using Brute Force.
"""
def max_profit(weight, stack):
    for item in stack: # O(n)
        item.append(item[1]/item[2])
    stack.sort(key=lambda x: x[3]) #O(nlog(n))
    bag = []
    while sum(item[2] for item in bag) < weight or len(stack) != 0: # O(n)
        if weight - item[2] > 0:
            item = stack.pop()
            weight -= item[2]
            A[0] += item[1]
            if (item[2] > 0): bag.append(item)
        else: break
    return bag

def knapSack(W, items, n):
    bag = []
    wt = [item[2] for item in items]
    val = [item[1] for item in items]
    dp = [0 for i in range(W+1)]
    for i in range(1, n+1):
        for w in range(W, 0, -1):
            if wt[i-1] <= w:
                dp[w] = max(dp[w], dp[w-wt[i-1]]+val[i-1])
    A[0] = dp[W]
    return bag

A = [0]
def main(): 
    weight = int(input())
    n = int(input())
    lines = [input().split(" ") for _ in range(n)] # O(n)
    for line in lines: # O(n)
        line[1] = float(line[1])
        line[2] = int(line[2])
    # bag = max_profit(weight, lines) # O(nlog(n))
    bag  = knapSack(weight, lines, n) # O(n*W)
    print(A[0])
    # for a in bag: # O(n)
    #     if a == bag[-1]: print(a[0] + "(" + "{a:.2f}, {b:.2f}"
    #     .format(a = a[1], b = a[2]) + ")", end="")
    #     else: print(a[0] + "(" + "{a:.2f}, {b:.2f}"
    #     .format(a = a[1], b = a[2]) + ")", end=" ")
    # print("\n" + str(A[0]))

if __name__ == "__main__":
    main()