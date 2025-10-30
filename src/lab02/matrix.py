def transpose(mat):
    if not mat:
        return []
    lenn = len(mat[0])
    for row in mat:
        if len(row) != lenn:
            raise ValueError
    res = []
    for colindex in range(len(mat[0])):
        newrow = []
        for rowindex in range(len(mat)):
            newrow.append(mat[rowindex][colindex])
        res.append(newrow)
    return res
#print(transpose([[1, 2, 3]]))
#print(transpose([[1], [2], [3]]))
#print(transpose([[1, 2], [3, 4]]))
#print(transpose([[]]))
#print(transpose([[1, 2], [3]]))


def row_sums(mat):
    if not mat:
        return []
    lenn1 = len(mat[0])
    for i, row in enumerate(mat):
        if len(row) != lenn1:
            raise ValueError
    return [int(sum(row)) for row in mat]
#print(row_sums([[1, 2, 3], [4, 5, 6]]))
#print(row_sums([[-1, 1], [10, -10]]))
#print(row_sums([[0, 0], [0, 0]]))
#print(row_sums([[1, 2], [3]]))


def col_sums(mat):
    if not mat:
        return []
    lenn1 = len(mat[0])
    for i, row in enumerate(mat):
        if len(row) != lenn1:
            raise ValueError
    numcols = len(mat[0])
    sums = [0] * numcols
    
    for row in mat:
        for j in range(numcols):
            sums[j] += row[j]
    return sums
#print(col_sums([[1, 2, 3], [4, 5, 6]]))
#print(col_sums([[-1, 1], [10, -10]]))
#print(col_sums([[0, 0], [0, 0]]))
#print(col_sums([[1, 2], [3]]))

