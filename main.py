def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    letter_count_dict = num_of_characters(text)
    letter_count = [{"character": k, "count": v} for k, v in letter_count_dict.items()
    ]
    letter_count.sort(reverse=True, key=sort_on)
    for letter in letter_count:
        if letter["character"].isalpha():
            print(f"The '{letter['character']}' character was found {letter['count']} times.")

    print(f"{num_words} words found in the document")

def get_num_words(text):
    words = text.split()
    return len(words)

def get_book_text(book_path):
    with open(book_path) as f:
        return f.read()
    
def num_of_characters(text):
    dictionary = {}
    for letter in text:
        letter = letter.lower()
        if letter in dictionary:
            dictionary[letter] = dictionary[letter] +1
        else:
            dictionary[letter] = 1
    return dictionary

def sort_on(dict_item):
    return dict_item['count']
    

main()
