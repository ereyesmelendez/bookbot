def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    num_letters = get_num_total_letters(text)
    letter_nums = get_num_each_letter(text)
    print(f"{num_words} words found in the document")
    print(f"{num_letters} letters found in the document")
    for letter, count in sorted(letter_nums.items()):
            print(f"{letter}: {count}")

def get_num_words(text):
    words = text.split()
    return len(words)

def get_num_total_letters(text):
    letters = text.lower()
    return len(letters)

def get_num_each_letter(text):
    letter_nums = {} #dictionary to store frequency of each letter
    for line in text:
        for char in line:
            if char.isalpha():
                char=char.lower()
                letter_nums[char] = letter_nums.get(char, 0) + 1
    return letter_nums



def get_book_text(path):
    with open("/home/edrick/workspace/github.com/ereyesmelendez/bookbot/books/frankenstein.txt") as f:
        return f.read()


#def get_average_letters_per_word(text):
    #average = num_letters / num_words

main()