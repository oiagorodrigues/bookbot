def get_content(file_path: str) -> str:
    with open(file_path) as f:
        return f.read()


def get_num_words(file_path: str) -> str:
    content = get_content(file_path)
    num_words = len(content.split())
    return f"{num_words} words found in the document"
