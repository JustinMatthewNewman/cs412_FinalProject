"""
    name:  Justin Newman
"""
def max_profit(heavy, stack):
    for item in stack:
        item.append(item[1]/item[2])
    stack.sort(key=lambda x: x[3])
    def recursion_profit():
        if sum(item[2] for item in stack) == w[0]: return bag
        if stack == []: return bag
        item = stack.pop()
        if item[2] > w[0]:
            item[1] = (w[0]/item[2]) * item[1]
            item[2] = (w[0]/item[2]) * item[2]
        w[0] -= item[2]
        A[0] += item[1]
        if (item[2] > 0): bag.append(item)
        return recursion_profit()
    bag = []
    w = [heavy]
    return(recursion_profit())

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