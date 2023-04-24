def snippet_maker(text):
    if isinstance(text,str):
        words = text.split()
        if len(words) > 5:
            return " ".join(words[:5]) + "..."
        if len(words) > 0:
            return text
        else:
            raise Exception("Empty string!")
    else:
        raise Exception("Not a string!")