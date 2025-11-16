def get_num_words(text):
    split_book = text.split()
    return len(split_book)

def character_count(text):
    word_dic = {}
    for l in text:
        lower = l.lower()
        if lower in word_dic:
            word_dic[lower] += 1
        else: 
            word_dic[lower] = 1
    return word_dic

def sort_on(items):
    return items["num"]

def sort_dictionary(char_dic):
    new_dic = []
    for i in char_dic:
        if type(i) == str:
            if i.isalpha():
                new_dic.append({"char": i, "num" : char_dic[i]})
    new_dic.sort(reverse=True ,key=sort_on)
    return new_dic
            
    