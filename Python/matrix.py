# Program to add two matrices using nested loop

X = Y =[[1,2],
    [4,5]]

result = [[0,0],
         [0,0]]

# iterate through rows
for i in range(len(X)):
   # iterate through columns
   for j in range(len(X[0])):
       result[i][j] = X[i][j] * Y[i][j]

for r in result:
   print(r)
