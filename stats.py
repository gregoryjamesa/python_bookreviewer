def number_counter(text):
    counter = 0
    new_list = []
    new_list = text.split()
    for word in new_list:
        counter += 1
    pass
    print(f"Found {counter} total words")


def character_counter(text):
    new_chars = []
    lower_new_chars = []
    for word in text:
        for character in word: 
            new_chars.append(character)
    for char in new_chars:
        lower_new_chars.append(char.lower())
    # print(lower_new_chars)
    new_set = set()
    counter = 0
    new_dict ={}
    for item in lower_new_chars:
        item.lower()
        new_set.add(item)
    for setpiece in new_set:  
        new_dict[setpiece] = 0
    for item in lower_new_chars:
        if item in new_dict:
            new_dict[item] += 1
        else:
            pass
        #print(new_dict)
    return new_dict

def sorting_values(new_dict):
        dict_list = list(new_dict.items())
        dict_list.sort(key= lambda x: x[1], reverse=True)
        result =[]
        for key, value in dict_list:
            result.append({"char": key, "num": value})
        
        return result
    




