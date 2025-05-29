def get_content(file_path: str) -> str:
    with open(file_path) as f:
        return f.read()


def get_num_words(file_path: str) -> str:
    content = get_content(file_path)
    num_words = len(content.split())
    return f"{num_words} words found in the document"

def get_num_characters(file_path: str) -> object:
    characters_count: dict[str, int] = {}
    content = get_content(file_path).lower()

    for character in content:
        characters_count[character] = characters_count[character] + 1 if character in characters_count else 1;

    return characters_count
