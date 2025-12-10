def normalize(text: str, *, casefold: bool = True, yo2e: bool = True):
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
def tokenize(text):
    tokens = []
    current_token = []
    for ch in text:
        if ch.isalnum() or ch == '_':
            current_token.append(ch)
        elif ch == '-' and current_token:
            current_token.append(ch)
        else:
            if current_token:
                tokens.append(''.join(current_token))
                current_token = []
    if current_token:
        tokens.append(''.join(current_token))
    
    return tokens

#print(tokenize("привет мир"))
#print(tokenize("hello,world!!!"))
#print(tokenize("по-настоящему круто"))
#print(tokenize("emoji 😀 не слово"))
def count_freq(tokens):
    freq_dict = {}
    for token in tokens:
        freq_dict[token] = freq_dict.get(token, 0) + 1
    return freq_dict
#print(count_freq(["a","b","a","c","b","a"]))
#print(count_freq(["bb","aa","bb","aa","cc"]))

def top_n(freq, n):
    sorted_items = sorted(freq.items(), key=lambda x: (-x[1], x[0]))
    return sorted_items[:n]
#print(top_n({"a": 3, "b": 2, "c": 1},n=2))
#print(top_n({"bb": 2, "aa": 2, "cc": 1}, n=2))