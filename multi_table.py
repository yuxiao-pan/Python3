
#w/out X
print ("Multiplication Chart\n")

for i in range(1,13):
    print (i, end="\t")
print ()
for j in range(1,13):
    for k in range(1,13):
        print (j*k, end="\t")
    print ("\n")

i = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
print (i)
for j in [i]:
    for k in [i]:
        print (j*k, end="\t")
    print ("\n")
