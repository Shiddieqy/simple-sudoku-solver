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
D=[]
for i in range(16):
    if (A[(i)//4][(i)%4] == 0):
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

rows = [set(range(1,5)) for i in range (4)]
columns = [set(range(1,5)) for i in range (4)]
squares = [set(range(1,5)) for i in range (4)]

for i in D:
    k = A[i//4][i%4]
    rows[i//4].discard(k)
    columns[i%4].discard(k)
    squares[(i//4)//2*2+(i%4)//2].discard(k)
F=[0,0,0]
for i in range (4):
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
        x = rows[i//4] & columns[i%4] & squares[(((i//4)//2)*2)+((i%4)//2)]
        y = list(x)
        U[j]=len(y)
        if len(y)==0:
            m=0
            for k in range (1,j+1):
                l=C[j-k]
                m+=1
                rows[l//4].add(A[l//4][l%4])
                columns[l%4].add(A[l//4][l%4])
                squares[(((l//4)//2)*2)+((l%4)//2)].add(A[l//4][l%4])
                if U[j-k] == L[j-k]:
                    L[j-k]=0
                else :
                    L[j-k]+=1
                    break
            j-=m
            continue 
        else :
            
            A[i//4][i%4]=y[L[j]]
            rows[i//4].remove(y[L[j]])
            columns[i%4].remove(y[L[j]])
            squares[(((i//4)//2)*2)+((i%4)//2)].remove(y[L[j]])
            j+=1

    print("the solution is: ")    
    for i in range (4):
        for j in range (4):
            print(A[i][j],end=" ")
            if j == 1:
                print('|', end=" ")
        print()
        if i == 1 :
            print("----------")