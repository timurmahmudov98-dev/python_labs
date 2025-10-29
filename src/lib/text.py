def normalize(text: str, *, casefold: bool = True, yo2e: bool = True) -> str:
    if yo2e:
        text = text.replace('ё', 'е').replace('Ё', 'Е')
    result = []
    for char in text:
        if char in {'\t', '\r', '\n', '\v', '\f'}:
            result.append(' ')
        else:
            result.append(char)
    text = ''.join(result)
    if casefold:
        text = text.casefold()
    words = text.split()
    return ' '.join(words)
#print(repr(normalize("ПрИвЕт\nМИр\t")))  
#print(repr(normalize("ёжик, Ёлка")))
#print(repr(normalize("Hello\r\nWorld")))
#print(repr(normalize("  двойные   пробелы  ")))