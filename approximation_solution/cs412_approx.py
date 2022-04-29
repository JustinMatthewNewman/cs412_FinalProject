"""
    Approximate Solution to Max Knapsack using psuedo-polynomial random approximation
     
""" 
import random, time
def main():
    maxW = int(input())
    numItems = int(input())

    items = [[y[0], float(y[1]), float(y[2])] for y in [input().split() for i in range(numItems)]]
    start = time.time()
    
    func = lambda list: list[1]/list[2]
    func2 = lambda list: list[2]
    func3 = lambda list: list[1]
    sorted_items = sorted(items, key=func)
    sorted_weights = sorted(items, key=func2)[::-1]

    upperBound = FindUpperBound(sorted_items, maxW)
    picks = sorted(FindApproxSolution(sorted_weights, upperBound, maxW, start), key=func3)[::-1]

    print("\nSelected items: \n")
    max_val = 0
    total_weight = 0
    for item in picks:
        print(item[0], item[1], item[2])
        max_val += item[1]
        total_weight += item[2]
    print("\nBound Value: \t", upperBound, "\nTotal value: \t", max_val, "\nTotal weight: \t", total_weight)
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

def FindApproxSolution(items, upperBound, maxW, start_time):
    resetable_items = items.copy()
    chosen_items = []
    max = 0
    error = (upperBound - max) / upperBound

    while error > 0.01 and time.time() - start_time < 5:
        wRem = maxW
        resetable_items = items.copy()
        chosen_items = []
        while wRem > 0:
            rand = chooseRandomItemThatFits(resetable_items, wRem)
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

def chooseRandomItemThatFits(items, wRem):
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
