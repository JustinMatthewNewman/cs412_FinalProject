
v = 0
for a in range(10, 100000, 100):
    f = open("test_cases_forGraph/test" + str(v) + ".txt", "w")
    v+=1
    f.write(str(a)+"\n")
    f.write("3\n")
    f.write("ring 100 5\n")
    f.write("gold 50 10\n")
    f.write("silver 50 5\n")
    f.close()