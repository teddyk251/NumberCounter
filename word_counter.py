def count_words(string=None,file=None):
    words = 0
    if string:
        words = len(string.split())
    if file:
        with open(file) as f:
            words = len(f.read().split())
    return words
