#Shabri Ash Shiddieqy
#First created 21 January 2021
#Python 3.8

#Create an empty 4x4 array
A = [[0 for i in range (4)] for j in range (4)]

#Filling the array with user input (write 0 for empty cell)
for i in range (4):
    X=input("Row " + str(i+1) +" : ")
    for j in range (4):
        A[i][j]=int(X[j])

'''Create a null list that will be filled with index of array A which contain 
a number in order to make it immutable'''
C=[]
for i in range(16):
    if (A[(i)//4][(i)%4] == 0):
        C.append(i)
print(C)
#isSolved variable : tells us is the sudoku solved or not
isSolved=0
def isDone(Arr):
    m=0
    for i in range (4):
        for j in range (4):
            for k in range (j+1,4):
                if Arr[i][k]==Arr[i][j] or Arr[k][i]==Arr[j][i] or Arr[(2*(k//2))+i//2][(2*(k%2))+i%2]==Arr[(2*(k//2))+j//2][(2*(k%2))+j%2]:
                    m=1
                    return False
    if m == 0 :
        return True
#The main loop to solve the sudoku
'''There are 2**(len(C) possible ways to fill the sudoku. This loop try each possibilities.
And will stop if the sudoku solved. Or there is no more possibility left.'''
for i in range(4**(len(C))):
    for j in range(len(C)):
        A[C[j]//4][C[j]%4]=((i//(4**j))%(4)+1)
    if isDone(A):
        print("The solution is : ")
        for x in range(4):
            for y in range(4):
                print(A[x][y], end=" ")
            print()
        isSolved=1
        break
#If the loop stop without solving the sudoku, an error message will appear
if isSolved==False :
    print("Error, sudoku has no solution")
