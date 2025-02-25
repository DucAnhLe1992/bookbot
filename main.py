from stats import get_num_words
import sys

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    with open(sys.argv[1]) as f:
        file_contents = f.read()
        count = get_num_words(file_contents)

        lower_contents = file_contents.lower()
        count = {}
        for letter in lower_contents:
            if letter.isalpha():
                if letter not in count:
                    count[letter] = 1
                else:
                    count[letter] += 1
        count_list = list(map(lambda key: { "name": key, "num": count[key]}, count.keys()))
        count_list.sort(reverse=True, key=lambda dict: dict["num"])

        print(f"Found {count} total words")
        for item in count_list:
            print(f"{item["name"]}: {item["num"]}")

main()