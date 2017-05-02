def intersection_of_lists(listOne, listTwo):
    """
    (list, list) -> (list)
    Given two lists, find intersection of them. No duplicates.

    Example:
    intersection_of_lists([1,5,6,8,8],[8,7,5]) -> [5,8]
    """
    intersection = []
    for num in listOne:
        if  num in listTwo:
            if num not in intersection:
                intersection.append(num)

    return intersection

def nonintersection_of_lists(listOne, listTwo):
    """
    (list, list) -> (list)
    Given two lists, find values that are not intersectional.
    No duplicates.

    Example:
    nonintersection_of_lists([1,5,6,8,8],[8,7,5]) -> [1,6,7]
    """
    intersection = []
    for num in listOne:
        if num not in listTwo:
            if num not in intersection:
                intersection.append(num)

    for num in listTwo:
        if num not in listOne:
            if num not in intersection:
                intersection.append(num)

    return intersection    

