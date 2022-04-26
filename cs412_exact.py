"""
    Exact Solution to Max Knapsack using Brute Force.
"""
def max_profit(weight, stack):
    for item in stack:
        item.append(item[1]/item[2])
    stack.sort(key=lambda x: x[3])
    bag = []
    while sum(item[2] for item in bag) < weight or len(stack) != 0:
        if weight - item[2] > 0:
            item = stack.pop()
            weight -= item[2]
            A[0] += item[1]
            if (item[2] > 0): bag.append(item)
        else: break
    return bag

A = [0]
def main(): 
    weight = int(input())
    n = int(input())
    lines = [input().split(" ") for _ in range(n)]
    for line in lines:
        line[1] = float(line[1])
        line[2] = float(line[2])
    bag = max_profit(weight, lines)
    for a in bag:
        if a == bag[-1]: print(a[0] + "(" + "{a:.2f}, {b:.2f}"
        .format(a = a[1], b = a[2]) + ")", end="")
        else: print(a[0] + "(" + "{a:.2f}, {b:.2f}"
        .format(a = a[1], b = a[2]) + ")", end=" ")
    print("\n" + str(A[0]))

if __name__ == "__main__":
    main()