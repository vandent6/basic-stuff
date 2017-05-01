def make_bricks(small, big, goal):
    """
    Goal inches long, big bricks are 5 long, small bricks are 1 long.
    Can we make the goal with bricks given?
    """
    if small >= goal:
        return True
    
    if (big * 5 + small) >= goal:
        if small >= goal % 5:
            return True
  
    return False


def lucky_sum(a, b, c):
    nums = [a,b,c]
    sum = 0
  
    for pt in nums:
        if pt == 13:
            break
        sum += pt
    
    return sum


def round10(num):
    if num % 10 >= 5:
        return num + (10 - num % 10)
    elif num % 10 < 5:
        return num - (num % 10)    

def make_chocolate(small, big, goal):
  if small >= goal:
    return goal
    
  if (small + 5 * big) >= goal:
    for i in range(0, big):
      if goal >= 4:
        goal -= 5
    return goal
      
  return -1
            












            
    
