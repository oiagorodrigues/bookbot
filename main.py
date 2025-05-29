from stats import get_num_words, get_sorted_num_characters

def main():
    file_path = "./books/frankenstein.txt"
    num_words = get_num_words(file_path)
    characters_count = get_sorted_num_characters(file_path)

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {file_path}...")

    print("----------- Word Count ----------")
    print(num_words)

    print("--------- Character Count -------")
    for character in characters_count:
        char = str(character.get("char"))
        num = character.get("num")
        if not char.isalpha():
            continue
        print(f"{char}: {num}")

    print("============= END ===============")

main()
