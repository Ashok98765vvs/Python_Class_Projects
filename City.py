import string

def word_frequency(text: str) -> dict[str, int]:
    text = text.lower()
    for ch in string.punctuation:
        text = text.replace(ch, "")
    words = text.split()
    freq = {}
    for word in words:
        freq[word] = freq.get(word, 0) + 1
    return freq

def word_unique_dict(text: str) -> dict[str, bool]:
    text = text.lower()
    for ch in string.punctuation:
        text = text.replace(ch, "")
    words = text.split()
    unique = {}
    for word in words:
        unique[word] = True
    return unique

def main():
    text = input("Enter a sentence: ")
    print(word_frequency(text))
    unique_words = word_unique_dict(text)
    print(", ".join([f"'{word}'" for word in unique_words.keys()]))

if __name__ == "__main__":
    main()