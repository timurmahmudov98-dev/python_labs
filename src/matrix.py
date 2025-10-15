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
print(transpose([[1, 2, 3]]))
print(transpose([[1], [2], [3]]))
print(transpose([[1, 2], [3, 4]]))
print(transpose([[]]))
print(transpose([[1, 2], [3]]))