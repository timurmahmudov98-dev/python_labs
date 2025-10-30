import sys
from lib import count_freq, tokenize, normalize, top_n


def main():
    text = sys.stdin.read().strip()
    
    if not text:
        print("Всего слов: 0")
        print("Уникальных слов: 0")
        print("Топ-5:")
        return
    k = 0
    total_words = tokenize(text)
    for i in total_words:
        k += i
    unique_words = count_freq(text)
    top_words = top_n(text, 5)
    print(f"Всего слов: {k}")
    print(f"Уникальных слов: {unique_words}")
    print("Топ-5:")
    
    for word, count in top_words:
        print(f"{word}:{count}")


if __name__ == "__main__":
    main() 