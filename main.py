# Command-line application in Python that does static analysis on text files
# First Python project for beginners: https://www.boot.dev/learn/build-bookbot

def main():
    book_path = './books/frankenstein.txt'

    # 8: Bookbot - Read file
    text = read_book(book_path)
    
    # 9: Count words
    words_count = count_words(text)

    # 10: Count characters
    characters_count = count_characters(text)

    # 11: Print a report
    sorted_characters_count = get_sorted_list(characters_count)
    report = print_report(book_path, words_count, sorted_characters_count)
    print(report)

# 8: Bookbot - Read file
def read_book(text_file):
    with open(text_file) as file:
        return file.read()

# 9: Count words
def count_words(book):
    split_text = book.split()
    return len(split_text)

# 10: Count characters
def count_characters(book):
    count = {}
    for character in book:
        if character.isalpha():
            lower_alpha_character = character.lower()
            if lower_alpha_character in count:
                count[lower_alpha_character] += 1
            else: 
                count[lower_alpha_character] = 1
    return count

# 11: sort
def include_keys(characters_dict):
    key_value_characters_count = []
    for char in characters_dict:
        pair = {
            'char': char,
            'count': characters_dict[char],
        }
        key_value_characters_count.append(pair)
    return key_value_characters_count

def sort_characters(characters_dict):
    return characters_dict['count']

def get_sorted_list(characters_dict):
    characters = include_keys(characters_dict)
    characters.sort(reverse=True, key=sort_characters)
    return characters

# 11: print report
def print_report(book_path, words_count, sorted_characters_list):
    report = f"""
    \n--- Begin report of {book_path[2:]} ---
    \n{words_count} words found in the document
    """

    for character in sorted_characters_list:
        report += f"\nThe '{character['char']}' character was found {character['count']} times"

    report += "\n\n--- End report ---"
    return report

main()
