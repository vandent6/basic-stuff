


def count_code(string):
    """
    find count of words with co*e where * can be any alpha
    """
    count = 0
    tempStr = string.lower()
    for i in range(0,string.count('co')):
        num = tempStr.find('co')
        if len(tempStr) > num + 3:      
            if tempStr[num + 3] == "e":
                count += 1
                tempStr = tempStr[num+4:]
            else:
                tempStr = tempStr[num+2:]
        print(tempStr)
        
    return count



def end_other(a,b):
    """
    if strings end eachother, return true or false
    """
    start = abs(len(a) - len(b))
    return a[start:].lower() == b.lower() or b[start:].lower() == a.lower()


def xyz_there(str):
    """
    find instances of xyz, if with . in front, return false
    if no . in front, return true
    """
    if len(str) < 3:
        return False
    
    tempStr = str.lower()
    for i in range(0,str.count('xyz')):
        num = tempStr.find('xyz')
        if len(tempStr) > num + 2:
            if tempStr[num-1] is not ".":
                return True
            else:
                tempStr = tempStr[num+2:]
    
    return False




def last2(str):
    count = -1
    subStr = str[len(str)-2:]

    for i in range(0, len(str)-1):
        if subStr == str[i] + str[i+1]:
            count += 1

    return count












