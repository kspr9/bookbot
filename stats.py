def count_words(text: str) -> int:
    return len(text.split())

def count_characters(text: str) -> dict[str, int]:
    chardic = {}
    for char in text.lower():
        if char not in chardic:
            chardic[char] = 1
        else:
            chardic[char] += 1
    return chardic

#  function that takes the dictionary of characters and their counts and returns a sorted list of dictionaries.
#   Each dictionary should have two key-value pairs: one for the character and one for the count.
#   Sort from greatest to least by the count.
def sort_characters(chardic: dict[str, int]) -> list[dict[str, int]]:
    # Sort the items and convert each tuple to a dictionary
    return [{"character": char, "count": count} for char, count in sorted(chardic.items(), key=lambda x: x[1], reverse=True)]

