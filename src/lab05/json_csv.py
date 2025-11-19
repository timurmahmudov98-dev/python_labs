import json
import csv
from pathlib import Path


def json_to_csv(json_path: str, csv_path: str) -> None:
    # Проверка расширения файла
    if not json_path.lower().endswith('.json'):
        raise ValueError("Исходный файл должен быть в формате JSON")
    if not csv_path.lower().endswith('.csv'):
        raise ValueError("Целевой файл должен быть в формате CSV")
    
    # Проверка существования файла
    json_file = Path(json_path)
    if not json_file.exists():
        raise FileNotFoundError(f"Файл {json_path} не найден")
    
    # Чтение JSON
    try:
        with open(json_path, 'r', encoding='utf-8') as f:
            data = json.load(f)
    except json.JSONDecodeError as e:
        raise ValueError(f"Ошибка парсинга JSON: {e}")
    
    # Проверка типа данных
    if not isinstance(data, list):
        raise ValueError("JSON должен содержать список объектов")
    
    if len(data) == 0:
        raise ValueError("JSON файл пуст")
    
    # Получение всех уникальных полей (из первого объекта + алфавитная сортировка остальных)
    if len(data) > 0:
        first_item_fields = list(data[0].keys()) if data[0] else []
        all_fields = set(first_item_fields)
        
        for item in data[1:]:
            if isinstance(item, dict):
                all_fields.update(item.keys())
        
        # Порядок: сначала поля из первого объекта, затем остальные в алфавитном порядке
        remaining_fields = sorted(all_fields - set(first_item_fields))
        fieldnames = first_item_fields + remaining_fields
    else:
        fieldnames = []
    
    # Запись CSV
    try:
        with open(csv_path, 'w', encoding='utf-8', newline='') as f:
            if fieldnames:
                writer = csv.DictWriter(f, fieldnames=fieldnames)
                writer.writeheader()
                
                for item in data:
                    if not isinstance(item, dict):
                        raise ValueError("Все элементы JSON должны быть словарями")
                    
                    # Заполняем отсутствующие поля пустыми строками
                    row = {field: item.get(field, '') for field in fieldnames}
                    # Конвертируем не-строковые значения в строки
                    row = {k: str(v) if not isinstance(v, str) else v for k, v in row.items()}
                    writer.writerow(row)
    except Exception as e:
        raise ValueError(f"Ошибка записи CSV: {e}")





def csv_to_json(csv_path: str, json_path: str):
    #ошибки в форматах
    if not csv_path.lower().endswith('.csv'):
        raise ValueError("Исходный файл должен быть в формате CSV")
    if not json_path.lower().endswith('.json'):
        raise ValueError("Целевой файл должен быть в формате JSON")
    
    # Проверка существования файла
    csv_file = Path(csv_path)
    if not csv_file.exists():
        raise FileNotFoundError(f"Файл {csv_path} не найден")
    try:
        with open(csv_path, 'r', encoding='utf-8') as f:
            reader = csv.DictReader(f)
            # Проверка наличия заголовков
            if reader.fieldnames is None:
                raise ValueError("CSV файл должен содержать заголовок")
            data = list(reader)
            
    except Exception as e:
        raise ValueError(f"Ошибка чтения CSV: {e}")
    if len(data) == 0:
        raise ValueError("CSV файл пуст (нет данных, только заголовок)")
    
    # Запись JSON
    try:
        with open(json_path, 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=2)
    except Exception as e:
        raise ValueError(f"Ошибка записи JSON: {e}")




# Примеры использования (для тестирования)
if __name__ == "__main__":
    try:
        # Тест JSON -> CSV
        test_json = [
            {"name": "Alice", "age": 25, "country": "Russia", "city": "Moscow"},
            {"name": "Bob", "age": 30, "country": "USA", "city": "New York"},
            {"name": "Charlie", "age": 14, "country": "United Kingdom", "city": "London"}
        ]
        
        with open('src/data/samples/people.json', 'w', encoding='utf-8') as f:
            json.dump(test_json, f, ensure_ascii=False, indent=2)
        
        json_to_csv('src/data/samples/people.json', 'src/data/out/people_from_json.csv')
        print("JSON -> CSV: успешно")

        csv_to_json('src/data/samples/people.csv', 'src/data/out/people_from_csv.json')
        print("CSV -> JSON: успешно")
        
    except Exception as e:
        print(f"Ошибка: {e}")
