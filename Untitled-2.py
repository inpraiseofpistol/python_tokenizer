def tokenize_text(text):
    list_of_tokens = (
        text
        .replace("!", "")
        .replace("?", "")
        .replace(",", "")
        .replace(".", "")
        .replace(";", "")
        .replace(":", "")
        .replace(")","")
        .replace("(", "")
        .replace("'", "")
        .replace("\"", "")
        .lower()
        .split()
        )
    return list_of_tokens 