#Shabri Ash Shiddieqy
#First created 21 January 2021
#Python 3.8

#Create an empty 4x4 array
A = [[0 for i in range (9)] for j in range (9)]

#Filling the array with user input (write 0 for empty cell)
for i in range (9):
    X=input("Row " + str(i+1) +" : ")
    for j in range (9):
        A[i][j]=int(X[j])

'''Create a null list that will be filled with index of array A which contain 
a number in order to make it immutable'''
C=[]
D=[]
for i in range(81):
    if (A[(i)//9][(i)%9] == 0):
        C.append(i)
    else :
        D.append(i)

'''#isSolved variable : tells us is the sudoku solved or not
isSolved=0
def isDone(Arr):
    m=0
    for i in range (4):
        for j in range (4):
            for k in range (j+1,4):
                if Arr[i][k]==Arr[i][j] or Arr[k][i]==Arr[j][i] or Arr[(2*(i//2))+j//2][(2*(i%2))+j%2]==Arr[(2*(i//2))+k//2][(2*(i%2))+k%2]:
                    m=1
                    return False
    if m == 0 :
        return True
There is a problem with previous method. The maximum value of all the possibilities are too big. 
Its about 4 billion. So i use different method'''

rows = [set(range(1,10)) for i in range (9)]
columns = [set(range(1,10)) for i in range (9)]
squares = [set(range(1,10)) for i in range (9)]

for i in D:
    k = A[i//9][i%9]
    rows[i//9].discard(k)
    columns[i%9].discard(k)
    squares[(i//9)//3*3+(i%9)//3].discard(k)
F=[0,0,0]
for i in range (9):
    F[0]+=len(rows[i])
    F[1]+=len(columns[i])
    F[2]+=len(squares[i])

if not len(C) == F[0] == F[1] == F[2] :
    print("Error, sudoku has no solution")

else :
    M=0
    L=[0 for i in range(len(C))]
    U=[0 for i in range(len(C))]
    j=0

    while j < len(C):
        i = C[j]
        x = rows[i//9] & columns[i%9] & squares[(((i//9)//3)*3)+((i%9)//3)]
        y = list(x)
        U[j]=len(y)
        if len(y)==0:
            m=0
            for k in range (1,j+1):
                l=C[j-k]
                m+=1
                rows[l//9].add(A[l//9][l%9])
                columns[l%9].add(A[l//9][l%9])
                squares[(((l//9)//3)*3)+((l%9)//3)].add(A[l//9][l%9])
                if U[j-k]-1 == L[j-k]:
                    L[j-k]=0
                else :
                    L[j-k]+=1
                    break
            j-=m
            continue 
        else :
            
            A[i//9][i%9]=y[L[j]]
            rows[i//9].remove(y[L[j]])
            columns[i%9].remove(y[L[j]])
            squares[(((i//9)//3)*3)+((i%9)//3)].remove(y[L[j]])
            j+=1

    print("the solution is: ")    
    for i in range (9):
        for j in range (9):
            print(A[i][j],end=" ")
            if j%3 == 2:
                print('|', end=" ")
        print()
        if i%3 == 2 :
            print("-----------------------")