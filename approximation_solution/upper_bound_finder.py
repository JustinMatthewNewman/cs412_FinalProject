"""

    Uses fractional knapsack algorithm to find the upper bound to max knapsack.

"""

def sortKey(e):
    return e[1] / e[2]

def find(w, n, sack):
    if w <= 0 or n == -1:
        return 0.0
    elif w-sack[n][2] < 0:
        return sack[n][1] * (w / sack[n][2])
    return find(w-sack[n][2], n-1, sack) + sack[n][1]

def main():
    w = int(input())
    n = int(input())
    sack = [["", 0.0, 0.0]] * n
    for i in range(n):
        sack[i] = input().split()
        sack[i][1] = float(sack[i][1])
        sack[i][2] = float(sack[i][2])
    sack.sort(key=sortKey)
    total = find(w, n-1, sack)
    print(total)

if __name__ == "__main__":
    main()
