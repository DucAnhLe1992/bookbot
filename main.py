def main():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
        #count = len(file_contents.split())
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

        for item in count_list:
            print(f"The letter '{item["name"]}' appears {item["num"]} times.")

main()