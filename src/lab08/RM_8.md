# models.py
Описание структуры класса Student:
Атрибуты:
fio - ФИО студента
birthdate - Дата рождения в формате YYYY-MM-DD(год-месяц-число)
group - название группы
gpa - средний балл(от 0 до 5)

Методы:
__post_init__(self)
Автоматически вызывается после инициализации объекта и ыполняет валидацию полей birthdate и gpa.

age(self)
Вычисляет текущий возраст студента в полных годах.

to_dict(self)
Преобразует объект в словарь с ключами: fio, birthdate, group, gpa.

@classmethod from_dict(cls, data: Dict[str, Any]) -> 'Student'
Создает объект Student из словаря 

__str__(self)
Возвращает строковое представление объекта

```python
from dataclasses import dataclass, field
from datetime import date, datetime
from typing import Dict, Any


def _validate_birthdate(value: str) -> str:
    """Валидация формата даты рождения YYYY-MM-DD"""
    try:
        datetime.strptime(value, "%Y-%m-%d")
    except ValueError:
        raise ValueError("Дата рождения должна быть в формате YYYY-MM-DD")
    return value


def _validate_gpa(value: float) -> float:
    """Валидация среднего балла: 0 ≤ gpa ≤ 5"""
    if not (0 <= value <= 5):
        raise ValueError("Средний балл должен быть в диапазоне от 0 до 5")
    return value


@dataclass
class Student:
    fio: str
    birthdate: str
    group: str
    gpa: float

    def __post_init__(self) -> None:
        # Выполняем валидацию после инициализации датакласса
        _validate_birthdate(self.birthdate)
        _validate_gpa(self.gpa)

    def age(self) -> int:
        """Возвращает текущий возраст студента в годах"""
        today = date.today()
        birth_date = datetime.strptime(self.birthdate, "%Y-%m-%d").date()
        age = today.year - birth_date.year
        # Уменьшаем на 1, если день рождения ещё не наступил в этом году
        if (today.month, today.day) < (birth_date.month, birth_date.day):
            age -= 1
        return age

    def to_dict(self) -> Dict[str, Any]:
        """Преобразует объект Student в словарь"""
        return {
            "fio": self.fio,
            "birthdate": self.birthdate,
            "group": self.group,
            "gpa": self.gpa
        }

    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> 'Student':
        """Создаёт экземпляр Student из словаря"""
        return cls(
            fio=data["fio"],
            birthdate=data["birthdate"],
            group=data["group"],
            gpa=data["gpa"]
        )

    def __str__(self) -> str:
        return  f"Студент: {self.fio}\nВозраст: {self.age()}\nГруппа: {self.group}\nGPA: {self.gpa}"


# Пример использования 
if __name__== "__main__":
    try:
        s1 = Student("Иванов Иван Иванович", "2003-05-15", "ИВБО-01-21", 4.7)
        print(s1)
        print("Возраст:", s1.age())
        s2 = Student("Сидоров Олег Викторович", "1999-11-01", "ИВБО-02-20", 7.0) # Ошибка
    except ValueError as e:
        print("Ошибка валидации:", e)
```
![картинка 1](./images_lab08/models_lab08_res.png)