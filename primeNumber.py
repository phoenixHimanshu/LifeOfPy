import math
def prime(num):
    prime = True
    x = int( math.sqrt(num) )
   
   
    for itr in range(1,x) :
        if num % x == 0:
            prime = False
            break
        else:
            --x
            print(x) 

        prime =  True

    if prime:
        print(f'{num} is a prime number')
    else:
        print(f'{num} is not a prime number')               
    
    


if __name__ == '__main__':
    
    num = int(input('Enter number to be tested for prime'))
    prime(num)