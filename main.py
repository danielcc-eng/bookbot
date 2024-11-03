def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    #print(text)
    number_of_words = get_words(text)
    print(f"{number_of_words} words found in the document")
    chars_dict = get_characters(text)
    print("Count of all characters in Frankenstein is : \n"
          + str(chars_dict))
    report = get_report(text, book_path)
    print(report)



def get_book_text(path):
    with open(path) as f:
        return f.read()
def get_words(text):

    return len(text.split())

def get_characters(text):
    #count = dict()
    #text.lower()v
    '''
    chars = {}
    for c in text:
        lowered = c.lower()
        if lowered in chars:
            chars[lowered] += 1
        else:
            chars[lowered] = 1
    return chars
    '''
    chars = {}

    for keys in text.lower():
        chars[keys] = chars.get(keys, 0) + 1



    return chars

def sort_on(d):
    return d["num"]


def chars_dict_to_sorted_list(num_chars_dict):
    sorted_list = []
    for ch in num_chars_dict:
        sorted_list.append({"char": ch, "num": num_chars_dict[ch]})
    sorted_list.sort(reverse=True, key=sort_on)
    return sorted_list
def get_report(text, book_path):
    report = "--- Begin report of " + book_path.__str__() + " ---\n"
    words = get_words(text)
    report += words.__str__() + " words found in the document \n"

    chars_dict = get_characters(text)
    sorted_list = chars_dict_to_sorted_list(chars_dict)
    for item in sorted_list:
        if not item["char"].isalpha():
            continue
        report += "The " + item['char'].__str__() + " character was found " + item['num'].__str__() + " times\n"
        # print(f"The '{item['char']}' character was found {item['num']} times")

    #print("--- End report ---")
    report += "--- End report ---"
    #print (report)
    return report


main()
