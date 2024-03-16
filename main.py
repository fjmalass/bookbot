from pathlib import Path
from collections import Counter

def word_count(text):
    return len(text.split())

def count_letters(text):
    count = Counter()
    for c in text.lower():
        count.update(c)
    return count


if __name__ == "__main__":

    file_name =  Path("books/frankenstein.txt")
    with open(file_name) as f:
        file_contents = f.read()

    print(f"words: {word_count(file_contents)}")

    char_counter = count_letters(file_contents)
    for c, count in char_counter.most_common():
        if c.isalpha():
            print(f"The {c} character was found {count} times")

    # print(f"counter: {count_letters(file_contents)}")

