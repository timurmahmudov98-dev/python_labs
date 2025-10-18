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