from stats import get_num_words, get_num_characters

def main():
    file_path = "./books/frankenstein.txt"
    print(get_num_words(file_path))
    print(get_num_characters(file_path))

main()
