"""
    Approximate Solution to Max Knapsack using psuedo-polynomial random approximation
     
""" 
import random, time
def main():
    maxW = int(input())
    numItems = int(input())

    items = [[y[0], float(y[1]), float(y[2])] for y in [input().split() for i in range(numItems)]]
    start = time.time()
    
    func = lambda list: list[1]/list[2] #price/weight
    func2 = lambda list: list[2]
    func3 = lambda list: list[1]
    sorted_items = sorted(items, key=func) #list of items sorted from lowest value per weight to highest
    sorted_weights = sorted(items, key=func2)[::-1]

    # Use Fractional Knapsack to find an upperbound for correctness checking later on
    upperBound = int(FindUpperBound(sorted_items, maxW))
    print("Upper Bound", upperBound)
    ret = FindApproxSolution(sorted_weights, upperBound, maxW)

    sorted_ret = sorted(ret, key=func3)[::-1]
    for item in sorted_ret:
        print(item[0] + "(" + str(item[1]) + ", " + str(item[2]) + ")", end=" ")
    print("\nApproximated Value", getValue(ret))
    print()
    
    end = time.time()
    print(end - start, "seconds\n")

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
    return value

def FindApproxSolution(items, upperBound, maxW):
    #untill our best solution is within a error range of our upper bound we continue to run a while loop
    #the while loop will keep picking items at random until it finds a full or close to full bag

    #when within the error margin return the list of items back to main
    resetable_items = items.copy()
    chosen_items = []
    max = 0
    error = (upperBound - max) / upperBound

    while error > 0.1:
        wRem = maxW
        resetable_items = items.copy()
        chosen_items = []
        while wRem > 0:
            rand = chooseRandomItemFits(resetable_items, wRem)
            if rand == None:
                break
            else:
                chosen_items.append(rand)
                resetable_items.remove(rand)
                wRem -= rand[2]
        error = (upperBound - getValue(chosen_items)) / upperBound
    return chosen_items            

def getValue(items):
    value = 0
    for item in items:
        value += item[1]
    return int(value)

def chooseRandomItemFits(items, wRem):
    #randomly picks and item out of the list and returns it if item's weight <= wRem
    index = -1
    for i in range(len(items)):
        if items[i][2] <= wRem:
            index = i
            break
    if index == -1:
        return None
    randomIndex = int(random.random() * (len(items) - index) + index)
    return items[randomIndex]

if __name__ == "__main__":
    main()
