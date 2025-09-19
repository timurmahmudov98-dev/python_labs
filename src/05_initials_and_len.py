fio = input().strip()
fio_cleaned = ' '.join(fio.split())
parts = fio_cleaned.split()
surname, name, patronymic = parts[0], parts[1], parts[2]
initials = surname[0] + name[0] + patronymic[0] + '.'
length = len(fio_cleaned)
print(f"Инициалы: {initials}")
print(f"Длина (символов): {length}")
