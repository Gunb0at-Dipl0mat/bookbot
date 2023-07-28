def count_words(file_contents) -> int:
    words = file_contents.split()
    return len(words)


def count_characters(file_contents) -> dict:
    dictionary = {}
    for character in file_contents:
        c = character.lower()
        if c not in dictionary.keys():
            dictionary[c] = 1
        else:
            dictionary[c] += 1
    return dictionary


filepath = "books/frankenstein.txt"
with open(filepath) as f:
    file_contents = f.read()
    print(f"--- Begin report of {filepath} ---")
    print(f"{count_words(file_contents)} words found in the document\n")
    unsorted_dict = count_characters(file_contents)
    sorted_dict = sorted(unsorted_dict.items(), key=lambda x: x[1])
    sorted_dict.reverse()
    for t in sorted_dict:
        if t[0].isalpha():
            print(f"The '{t[0]}' character was found {t[1]} times")
        else:
            continue
    print("--- End report ---")
