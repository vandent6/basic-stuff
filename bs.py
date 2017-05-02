def binary_search(item_list,item):
    first = 0
    last = len(item_list)-1
    found = False
    while( first<=last and not found):
        mid = (first + last) // 2
        if item_list[mid] == item :
            found = True
        else:
            if item < item_list[mid]:
                last = mid - 1
            else:
                first = mid + 1

    return found

'''
print(binary_search([1,2,3,5,8], 6))

print(binary_search([1,2,3,5,8], 5))  
'''

def sequential_search(item_list,item):

    for it in item_list:
        print(it)
        if it == item:
            return (True, item)

    return (False, item)
'''
print(sequential_search([11,23,58,31,56,77,43,12,65,19],31))
'''
