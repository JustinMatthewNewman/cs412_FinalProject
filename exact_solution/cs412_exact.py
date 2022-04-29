import time
def knapsack_dp(values,weights,n_items,capacity):
    table = [[0.0 for x in range(capacity + 1)] for x in range(n_items + 1)]
    keep = [[0.0 for x in range(capacity + 1)] for x in range(n_items + 1)]
    for i in range(1,n_items+1):
        for w in range(0,capacity+1):
            wi = weights[i-1]
            vi = values[i-1]
            if (wi <= w) and (vi + table[i-1][w-wi] > table[i-1][w]):
                table[i][w] = vi + table[i-1][w-wi]
                keep[i][w] = 1
            else:
                table[i][w] = table[i-1][w]
    picks = []
    K = capacity
    for i in range(n_items,0,-1):
        if keep[i][K] == 1:
            picks.append(i)
            K -= weights[i-1]
    picks = [x-1 for x in picks] # change to 0-index
    return picks

# A naive recursive implementation O(2^n)
def knapSack(W, wt, val, n):
    # Base Case
    if n == 0 or W == 0:
        return 0
    # If weight of the nth item is
    # more than Knapsack of capacity W,
    # then this item cannot be included
    # in the optimal solution
    if (wt[n-1] > W):
        return knapSack(W, wt, val, n-1)
    # return the maximum of two cases:
    # (1) nth item included
    # (2) not included
    else:
        return max(
            val[n-1] + knapSack(
                W-wt[n-1], wt, val, n-1),
            knapSack(W, wt, val, n-1))

#Driver Code
# val = [60, 100, 120]
# wt = [10, 20, 30]
# W = 50
# n = len(val)
# print knapSack(W, wt, val, n)

if __name__ == '__main__':
    start = time.time()
    capacity = int(input())
    n_items = int(input())
    lines = [input().split() for _ in range(n_items)]
    names=[]
    values=[]
    weights=[]
    for line in lines:
        names.append(line[0])
        values.append(int(line[1]))
        weights.append(int(line[2]))
    picks = knapsack_dp(values,weights,n_items,capacity)
    max_val = knapSack(capacity, weights, values, n_items)
    #total_weight = 0
    # print("\nSelected items: \n")
    #for a in picks:
        #print(names[a], values[a], weights[a])
        #max_val += values[a]
        #total_weight += weights[a]
    # print("\nTotal value: ", max_val, "\nTotal weight: ", total_weight)
    print(max_val, end=" ")
    end = time.time()
    print(end - start)
    