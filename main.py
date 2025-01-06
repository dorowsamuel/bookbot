def get_book_text(path):
    with open(path) as f:
        file_contents = f.read()
    return file_contents

def get_wordcount(text):
    return len(str.split(text))

def get_charcount(text):
    chars = {
        "a": 0, "b": 0, "c": 0, "d": 0, "e": 0, "f": 0, "g": 0, "h": 0, "i": 0, "j": 0, "k": 0, "l": 0, "m": 0, "n": 0, "o": 0, "p": 0, "q": 0, "r": 0, "s": 0, "t": 0, "u": 0, "v": 0, "w": 0, "x": 0, "y": 0, "z": 0
    }
    lower_text = text.lower()
    for character in list(lower_text):
        if character in chars:
            chars[character] += 1
    
    return chars

def main():
    path = "./books/frankenstein.txt"
    book = get_book_text(path)
    wordcount = get_wordcount(book)
    chars = get_charcount(book)

    print(f"--- Begin report of {path} ---\n")
    print(f"{wordcount} words found in the document")
    for i in chars:
        print(f"The letter {i} was found {chars[i]} times")
    print("\n--- End report ---")

main()