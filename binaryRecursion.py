# When the function makes two recursive calls 
def binary_sum(S,start,stop):
    if start >= stop:           # zero elements in slice
        return 0
    elif start == stop-1:       # One elements in slice
        return S[start]
    else:
        mid = (start+stop) // 2  # two or more elements in the slice
        return binary_sum(S,start,mid) + binary_sum(S,mid,stop)




if __name__ == '__main__':
    A = [8,7,6,5,4,3,2,1]  
   # A = [999]
   # A = []  
    print( binary_sum(A,0,len(A)) )