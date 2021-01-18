#Shabri Ash Shiddieqy
A = [[0 for i in range (2)] for j in range (2)]
for i in range (2):
    X=input("Input row " + str(i+1) +" : ")
    for j in range (2):
        A[i][j]=int(X[j])
i =0

C=[]
for i in range(4):
    if (A[(i)//2][(i)%2] == 0):
        C.append(i)
i = 0
j=1
isSolve=0
#while ((0 in A[0]) or (0 in A[1])) or (A[0][0]==A[0][1] or A[1][0]==A[0][0] or A[1][1]==A[0][1] or A[1][0]==A[1][1]):
for i in range(2**(len(C))):
    for j in range(len(C)):
        A[C[j]//2][C[j]%2]=((i//(j+1))%(2)+1)
    if not (((0 in A[0]) or (0 in A[1])) or (A[0][0]==A[0][1] or A[1][0]==A[0][0] or A[1][1]==A[0][1] or A[1][0]==A[1][1])):
        print("The solution is : ")
        for x in range(2):
            for y in range(2): 
                print(A[x][y], end=" ")
            print()
        isSolve=1
        break
if isSolve==False :
    print("Error, sudoku has no solution")
