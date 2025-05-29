import sys

def sort_on(dict):
    return dict["num"]


def get_content(file_path: str) -> str:
    content = ""
    try:
        with open(file_path) as f:
            content = f.read()
    except FileNotFoundError:
        print(f"File {file_path} not found. Please provide the correct path to your book.")
        sys.exit(1)
    return content


def get_num_words(file_path: str) -> str:
    content = get_content(file_path)
    num_words = len(content.split())
    return f"Found {num_words} total words"


def get_num_characters(file_path: str) -> dict[str, int]:
    characters_count: dict[str, int] = {}
    content = get_content(file_path).lower()

    for character in content:
        characters_count[character] = characters_count[character] + 1 if character in characters_count else 1;

    return characters_count


def get_sorted_num_characters(file_path: str) -> list[dict[str, int | str]]:
    characters_count_sorted_list: list[dict[str, int | str]] = []

    characters_count = get_num_characters(file_path)
    for char, num in characters_count.items():
      characters_count_sorted_list.append({ "char": char, "num": num })

    characters_count_sorted_list.sort(reverse=True, key=sort_on)
    return characters_count_sorted_list
