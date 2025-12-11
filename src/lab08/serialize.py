import json
from pathlib import Path

from models import Student


def students_to_json(students: list[Student], path: str | Path) -> None:
    path = Path(path)

    data = [s.to_dict() for s in students]

    with open(path, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)


def students_from_json(path: str | Path) -> list[Student]:
    path = Path(path)

    with open(path, "r", encoding="utf-8") as f:
        raw = json.load(f)

    if not isinstance(raw, list):
        raise ValueError("JSON must contain array of students")

    students = []
    for obj in raw:
        try:
            student = Student.from_dict(obj)
            students.append(student)
        except Exception as e:
            raise ValueError(f"invalid student object: {obj!r}, error: {e}") from e

    return students


def main():
    # 1. Сначала запишем входные данные в файл (если его еще нет)
    students = [
        Student(
            fio="Бибер Джастин Дрюевич",
            birthdate="2007-11-04",
            group="БИВТ-23-17",
            gpa=3.01,
        ),
        Student(
            fio="Иванов Иван Иванович",
            birthdate="2009-01-18",
            group="БИВТ-22-10",
            gpa=5.0,
        ),
        Student(
            fio="Пупкин Василий Сергеевич",
            birthdate="2007-04-03",
            group="БИВТ-21-11",
            gpa=5.0,
        ),
    ]
    
    # Создаем входной файл
    students_to_json(students, "src/data/lab08/students_input.json")
    print("Создан файл students_input.json")
    
    # 2. Читаем данные из входного файла
    loaded_students = students_from_json("src/data/lab08/students_input.json")
    print(f"Загружено {len(loaded_students)} студентов")
    
    # 3. Записываем результат в выходной файл
    students_to_json(loaded_students, "src/data/lab08/students_output.json")
    print("Создан файл students_output.json")
    
    # Проверяем, что файлы идентичны
    with open("src/data/lab08/students_input.json", "r", encoding="utf-8") as f1, \
         open("src/data/lab08/students_output.json", "r", encoding="utf-8") as f2:
        content1 = f1.read()
        content2 = f2.read()
        
    if content1 == content2:
        print("Файлы students_input.json и students_output.json идентичны")
    else:
        print("Файлы различаются")
    print("\nСтуденты из JSON")
    for s in loaded_students:
        print(s)
        print()


if __name__ == "__main__":
    main()

