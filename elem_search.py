

def basic_binary_search(item, itemList):
    """
    (str, sequence) -> (bool)
    Uses binary search to split a list and find if the item is in the list.

    Examples:
    basic_binary_search(7,[1, 4, 6, 7, 8, 9, 11, 15, 70, 80, 90, 100, 600]) -> True
    basic_binary_search(99,[1, 4, 6, 7, 8, 9, 11, 15, 70, 80, 90, 100, 600]) -> False
    """
    found = False
    while found == False:
        half = round(len(itemList)/2)
        if not half % 2:
            half -= 1
        
        if len(itemList) == 1:
            return itemList[0] == item

        if itemList[half] == item:
            found == True
            
        if item >= itemList[half]:
            itemList = itemList[half:]
        elif item < itemList[half]:
            itemList = itemList[:half]
            
    return found


print(basic_binary_search(7,[1, 4, 6, 7, 8, 9, 11, 15, 70, 80, 90, 100, 600]))
