def compact(lst):
    
    new_lst = []
    for elem in lst:
        if elem:
            new_lst.append(elem)
    return new_lst

"""
OR

def compact(lst)
    return[elem for elem in lst if elem]


"""