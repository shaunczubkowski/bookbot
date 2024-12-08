def count_words(file_contents):
    return len(file_contents.split())

def print_report(character_counts, word_count):
    print("--- Begin report of books/frankenstein.txt ---")
    print(f"{word_count} words found in the document.\n")

    for key in character_counts:
        print(f"The '{key}' character was found {character_counts[key]} times")

    print("\n--End of Report--")

def count_characters(book_as_string):
    character_count = {}
    for letter in book_as_string:
        lower_case_letter = letter.lower()
        if lower_case_letter in character_count:
            character_count[lower_case_letter] += 1
        else:
            character_count[lower_case_letter] = 1
    
    sorted_character_count = {k: v for k, v in sorted(character_count.items(), key=lambda item: item[1], reverse=True)}

    return sorted_character_count


def main():
    with open("./books/frankenstein.txt") as f:
        file_contents = f.read()
        word_count = count_words(file_contents)
        print_report(count_characters(file_contents), word_count)

main()