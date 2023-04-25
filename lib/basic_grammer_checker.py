
def basic_grammer_checker(text):
    punctuation = [".", "!", "?"]
    if text[-1] not in punctuation:
        text = text + "."
    if text[0] != text[0].capitalize():
        text = text[0].capitalize() + text[1:]
    return text