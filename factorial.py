


# def calculate(number):
#     fact = 1
#     for x in range(2,number):
#         fact = fact * x
#     print(fact)



def calculate(number):
        
    if (number == 1):
        return number
    else: 
        return number * calculate(number - 1)
         

if __name__ == '__main__':
    
    number = int( input('Enter a number for factorial=>'))
    print(calculate(number))