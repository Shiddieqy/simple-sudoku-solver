#Shabri Ash Shiddieqy
#First created 18 January 2021
#Python 3.8

#Create an empty 2x2 array
A = [[0 for i in range (2)] for j in range (2)]

#Filling the array with user input (write 0 for empty cell)
for i in range (2):
    X=input("Row " + str(i+1) +" : ")
    for j in range (2):
        A[i][j]=int(X[j])

'''Create a null list that will be filled with index of array A which contain 
a number in order to make it immutable'''
C=[]
for i in range(4):
    if (A[(i)//2][(i)%2] == 0):
        C.append(i)

#isSolved variable : tells us is the sudoku solved or not
isSolved=0

#The main loop to solve the sudoku
'''There are 2**(len(C) possible ways to fill the sudoku. This loop try each possibilities.
And will stop if the sudoku solved. Or there is no more possibility left.'''
for i in range(2**(len(C))):
    for j in range(len(C)):
        A[C[j]//2][C[j]%2]=((i//(j+1))%(2)+1)
    if not (((0 in A[0]) or (0 in A[1])) or (A[0][0]==A[0][1] or A[1][0]==A[0][0] or A[1][1]==A[0][1] or A[1][0]==A[1][1])):
        print("The solution is : ")
        for x in range(2):
            for y in range(2):
                print(A[x][y], end=" ")
            print()
        isSolved=1
        break
#If the loop stop without solving the sudoku, an error message will appear
if isSolved==False :
    print("Error, sudoku has no solution")
