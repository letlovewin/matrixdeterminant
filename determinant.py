def determinant(matrix):
    if len(matrix[0])==1:
        return matrix[0][0]
    elif len(matrix[0])==2: #The most important case
        return (matrix[0][0]*matrix[1][1])-(matrix[0][1]*matrix[1][0])
    else:
        x = []
        c = 0 #Determinant += count
        for i in range(len(matrix)):
            y = []
            p = None
            for j in range(1,len(matrix)): #Takes our minors
                if j < len(matrix):
                    p = matrix[j].copy() 
                    p.pop(i) #If the number is in the same row/column as our first column number, pop it out
                    y.append(p)
            if i%2 != 0: #Determinant adding operation
                c -= determinant(y)*matrix[0][i] 
            else:
                c += determinant(y)*matrix[0][i]
        return c
