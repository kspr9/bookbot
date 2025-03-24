from stats import count_words, count_characters, sort_characters
import sys

def get_book_text(path: str) -> str:
    with open(path, "r") as file:
        return file.read()
    
def print_report(charlistofdics: list[dict[str, int]]):
    for dic in charlistofdics:
        # Skip if the character is not an alphabetical character.
        if not dic["character"].isalpha():
            continue
        print(f"{dic['character']}: {dic['count']}")


def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    print("============ BOOKBOT REPORT =============")
    book_path = sys.argv[1]
    print(f"Analysing book found at {book_path}...")
    #print(book_text)
    book_text = get_book_text(book_path)
    print(f'---------------- Word Count ----------------')
    num_words = count_words(book_text)
    print(f'Found {num_words} total words')
    print(f'-------------- Character Count --------------')
    characters = count_characters(book_text)
    sorted_characters = sort_characters(characters)
    print_report(sorted_characters)
    print("=============== End report ===============")



if __name__ == "__main__":
    main()
