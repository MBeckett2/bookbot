def word_counter(file_contents):
    return len(file_contents.split())

def character_sort(file_contents):
    character_count = {}
    for c in file_contents:
        a = c.lower()
        if a in character_count:
            character_count[a] += 1
        else:
            character_count[a] = 1
    return character_count

def sort_on(key):
    return key["num"]
            
def sort_by_count(character_count):
    dict_list = []
    for c in character_count:
        dict_list.append({"char" : c, "num": character_count[c]})
        
    dict_list.sort(reverse=True, key=sort_on)   
    return dict_list
    
           
        
