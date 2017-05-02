def fizz_buzz(num):
    for i in range(0, num):
        if i % 3:
            print('fizz')
        if i % 5:
            print('buzz')
        if i % 3 and i % 5:
            print('fizzbuzz')
    
        
