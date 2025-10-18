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

def format_record(rec):
    if not isinstance(rec, tuple) or len(rec) != 3:
        raise TypeError
    
    fio, group, gpa = rec
    
    if not isinstance(fio, str):
        raise TypeError
    if not isinstance(group, str):
        raise TypeError
    if not isinstance(gpa, (int, float)):
        raise TypeError
    
    fio_clean = ' '.join(fio.split()).strip()
    if not fio_clean:
        raise ValueError
    
    group_clean = group.strip()
    if not group_clean:
        raise ValueError
    
    if gpa < 0:
        raise ValueError
    
    parts = fio_clean.split()
    surname = parts[0].title()
    
    initials = []
    for name_part in parts[1:]:
        if name_part:
            initials.append(f"{name_part[0].upper()}.")
    
    formatted_fio = f"{surname} {''.join(initials)}"
    formatted_gpa = f"{gpa:.2f}"
    
    return f"{formatted_fio}, гр. {group_clean}, GPA {formatted_gpa}"
#
# if __name__ == "__main__":
#     test_cases = [
#         ("Иванов Иван Иванович", "BIVT-25", 4.6),
#         ("Петров Пётр", "IKBO-12", 5.0),
#         ("Петров Пётр Петрович", "IKBO-12", 5.0),
#         ("  сидорова  анна   сергеевна ", "ABB-01", 3.999),
#     ]
    
#     for test in test_cases:
#         print(format_record(test))