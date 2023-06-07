#right triangle pattern
for i in range(5):
    for j in range(1,5-i): #it creates spaces
        print(" ",end=' ')
    for k in range(1,i+2): #it fills the numbers in the non spaces
        print(k,end=' ')
    print()