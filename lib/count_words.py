def count_words(text):
    if isinstance(text,str):
        words = text.split()
        return f'Number of words: {len(words)}'
    else:
        raise Exception("Not a string!")