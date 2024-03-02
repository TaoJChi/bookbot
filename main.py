def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    word_count = get_word_count(text)
    letter_count_dict = get_letter_count_dict(text)
    ordered_dict_list = get_ordered_dict_list(letter_count_dict)    
    print(f'--- Begin report of {book_path} --- \n{word_count} words found in the document \n') 
    for entry in ordered_dict_list:
        print(f'The {entry["char"]} character was found {entry["num"]} times')
    print('--- End report ---')

def get_book_text(path):
    with open(path) as f:
        return f.read()


def get_word_count(text):
    num_words = text.split()
    return len(num_words)


def get_letter_count_dict(text):
    l_text = text.lower()
    l_dict = {}
    for letter in l_text:
        if letter in l_dict:
            l_dict[letter] += 1
        else:
            l_dict[letter] = 1
    return l_dict


def sort_num(dict_entry):
    return dict_entry["num"]


def get_ordered_dict_list(let_dict):
    alpha_dict_list = []
    for char, num in let_dict.items():
        if char.isalpha():
            alpha_dict_list.append({"char":char, "num":num})
    alpha_dict_list.sort(reverse=True, key=sort_num)
    return alpha_dict_list


main()