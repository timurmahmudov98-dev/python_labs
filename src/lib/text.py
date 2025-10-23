import re

def normalize(text: str, *, casefold: bool = True, yo2e: bool = True) -> str:
    result = text
    if casefold:
        result = result.casefold()
    if yo2e:
        result = result.replace('ё', 'е').replace('Ё', 'Е')
    result = result.replace('\t', ' ').replace('\r', ' ').replace('\n', ' ')
    result = re.sub(r'\s+', ' ', result).strip()
    return result
# тест кейсы
#print(normalize("ПрИвЕт\nМИр\t"))
#print(normalize("ёжик, Ёлка"))
#print(normalize("Hello\r\nWorld"))
#print(normalize(" двойные пробелы "))
