

"""
    in hashmap (get,set,del,in)
    O(1) : avg
    O(n) : worst
    iteration still O(n)
"""


def main(items):  # recursive function
    item_type = type(items)  # store items type
    if item_type is tuple or item_type is list:  # if items is list or tuple
        return arrayHandler(items)
    elif item_type is dict:  # if items is dict
        return dictHandler(items)
    return items  # if item is not both
    """
    # oneliner
    return arrayHandler(items) if type(items) is tuple or type(items) is list else dictHandler(items)if type(items) is dict else items
    """


def removedPassword(items):  # del password in items
    if 'password' in items:
        del items['password']
    return items


def dictHandler(items):
    items = removedPassword(items)  # del password in items

    for key in items.keys():  # iterate and edit email value to 'redacted'
        if key == 'email':
            items[key] = 'redacted'
        else:
            items[key] = main(items[key])
    return items
    """
    # one liner ->
    return dict(map(lambda item: (item[0], main(item[1]) if item[0] != 'email' else 'redacted'), removedPassword(items).items()))
    """


def arrayHandler(items):  # handle tuple and list
    for i in items:
        i = main(i)
    return items
    """
    # for oneliner 
    return type(items)(map(lambda i: main(i), items))
    """


# input
value = {'dear': 'recruiter'}
if __name__ == "__main__":
    print(main(value))
