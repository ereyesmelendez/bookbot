def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    print(f"{num_words} words found in the document")

def get_num_words(text):
    words = text.split()
    return len(words)


def get_book_text(path):
    with open("/home/edrick/workspace/github.com/ereyesmelendez/bookbot/books/frankenstein.txt") as f:
        return f.read()

if __name__ == '__main__':
    main()


main()