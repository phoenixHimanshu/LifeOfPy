# write fuction for power

def powerN(x,n):
    if n == 0:
      return 1
    else:
      return x * powerN(x,n-1)


def powerLogN(x,n):
    if n == 0:
      return 1
    else:
       partial = powerLogN(x,n//2)
       result = partial * partial
       if n%2 == 1:
          result *=x
       return result   

if __name__ == '__main__':
    print(powerN(2,3))
    print(powerLogN(2,3))