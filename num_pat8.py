#revese pyramid pattern
for i in range(5):
        for j in range(i): #printing spaces
            print(' ',end=' ')
        for j in range(2*(5-i)-1): #printing numbers
            print(j+1,end=' ')
        print()

