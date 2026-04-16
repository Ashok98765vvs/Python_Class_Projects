import re
from collections import Counter

def normalize_words(text: str):
    return re.findall(r"[a-zA-Z']+", text.lower())

def word_frequency(text: str):
    return dict(Counter(normalize_words(text)))

def unique_words(text: str):
    return set(normalize_words(text))

def split_paragraphs(text: str):
    return [p.strip() for p in text.strip().split("\n") if p.strip()]

with open("whisker.txt", "r", encoding="utf-8") as file:
    text = file.read()

freq = word_frequency(text)
unique = unique_words(text)

paragraphs = split_paragraphs(text)

p1_words = unique_words(paragraphs[0])
p2_words = unique_words(paragraphs[1])

common_words = p1_words & p2_words
only_p1 = p1_words - p2_words
symmetric = p1_words ^ p2_words

with open("report.txt", "w", encoding="utf-8") as f:
    f.write("REPORT\n")
    f.write("="*50 + "\n\n")

    f.write("1. WORD FREQUENCY\n")
    f.write("-"*50 + "\n")
    for word, count in sorted(freq.items()):
        f.write(f"{word}: {count}\n")

    f.write("\n2. UNIQUE WORDS\n")
    f.write("-"*50 + "\n")
    for word in sorted(unique):
        f.write(word + "\n")

    f.write("\n3. PARAGRAPH COMPARISON\n")
    f.write("-"*50 + "\n")

    f.write("\n3.1 COMMON WORDS\n")
    for word in sorted(common_words):
        f.write(word + "\n")

    f.write("\n3.2 ONLY IN PARAGRAPH 1\n")
    for word in sorted(only_p1):
        f.write(word + "\n")

    f.write("\n3.3 UNIQUE (NOT COMMON)\n")
    for word in sorted(symmetric):
        f.write(word + "\n")

print("report.txt created")