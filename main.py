def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    word_count = count_words(text)
    print(f"--- Begin report of {book_path} ---")
    print(f"{word_count} words found in the document\n")
    char_count = count_char(text)
    char_lst = dict_lst(char_count) 
    char_lst.sort(reverse=True, key=sort_on)
    for dic in char_lst: 
        print(f"The '{dic['letter']}' character was found {dic['num']} times")
    print('--- End report ---')


def get_book_text(path):
    with open(path) as f:
        return f.read()

def count_words(text):
    words = text.split()
    return len(words)

def count_char(text):
    count_dict = {} 
    lower_text = text.lower()
    for cr in lower_text: 
        count_dict[cr] = count_dict.get(cr,0)+1
    return count_dict

def dict_lst(dict): 
    lst = []
    for i in dict: 
        if i.isalpha():
            lst.append({"letter" : i, "num" : dict[i]})
    return lst

def sort_on(dict):
    return dict["num"]

main()
