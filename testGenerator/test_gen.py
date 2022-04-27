import random
weight = random.randint(0,10000)
numItems = random.randint(0,100)
print(weight)
print(numItems)
from wordlist import wordlist
for i in range(numItems):
    print(random.choice(wordlist), end=" ")
    print(random.randint(1,10000), end=" ")
    print(random.randint(1,weight), end="")
    print()

