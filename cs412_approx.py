"""
    Approximate Solution to Max Knapsack using psuedo-polynomial random approximation
"""

def main():
    maxW = int(input())
    numItems = int(input())

    items = [[y[0], float(y[1]), float(y[2])] for y in [input().split() for i in range(numItems)]]
    func = lambda list: list[1]/list[2]
    sorted_items = sorted(items, key=func) #list of items sorted from lowest value per weight to highest

    # Use Fractional Knapsack to find an upperbound for correctness checking later on
    upperBound = FindUpperBound(sorted_items, maxW)
    print(upperBound)

    sorted_items = sorted_items[::-1]

def FindUpperBound(items, wRem):
    value = 0
    for i in reversed(range(len(items))):
        wRem -= items[i][2]
        if wRem < 0:
            wRem += items[i][2]
            value += (items[i][1] * wRem) / items[i][2]
            return value
        else:
            value += items[i][1]

def FindApproxSolution(items, upperBound, maxW):
    #untill our best solution is within a error range of our upper bound we continue to run a while loop
    #the while loop will keep picking items at random until it finds a full or close to full bag

    #when withing the error margin return the list of items and the value back to main
    pass

def chooseRandomItemFits(items, wRem):
    #randomly picks and item out of the list and returns it if item's weight <= wRem
    pass

if __name__ == "__main__":
    main()
