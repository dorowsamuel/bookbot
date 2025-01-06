def get_book_text(path):
    with open(path) as f:
        file_contents = f.read()
    return file_contents

def get_wordcount(text):
    return len(str.split(text))

def main():
    path = "./books/frankenstein.txt"
    book = get_book_text(path)
    wordcount = get_wordcount(book)
    print(book)
    print(f"\n{wordcount}")

main()