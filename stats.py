def count(data):
    num_words = len(data.split())
    return num_words

def get_character_counts(characters):
    letters = {}
    for i in characters:
        low_char = i.lower()
        if low_char in letters:
            letters[low_char] += 1
        else:
            letters[low_char] = 1
    return letters

def sortings(items):
    return items["num"]

def sorting_line(sorts):
    lines = []
    for low_char, count in sorts.items():
        if low_char.isalpha():
            final_char = {"char": low_char, "num": count}
            lines.append(final_char)
    lines.sort(reverse=True, key=sortings)
    return lines
