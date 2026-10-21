def reverse_string(text):
    return text[::-1]


def capitalize_words(text):
    return ' '.join(word.capitalize() for word in text.split())


def truncate(text, length, suffix='…'):
    if len(text) <= length:
        return text
    return text[:length - len(suffix)] + suffix


def slugify(text):
    return '-'.join(text.lower().split())
