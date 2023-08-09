def print_rangoli(size):
    # your code goes here
      lst = list(map(chr,range(97,123)))
      # problem 1
      #5print(lst[n-1::-1] + lst[1:n:1])
      x = lst[n-1::-1] + lst[1:n:1]
      lstr = len('-'.join(x)) 
      # problem 2
      #      |e
      #    e |d e
      #  e d |c d e
      #e d c |b c d e


      for i in range(1,size):
        print('-'.join(lst[size-1:size-i:-1]+lst[size-i:size]).center(lstr,'-'))
      for i in range(n,0,-1):
        print('-'.join(lst[size-1:size-i:-1]+lst[size-i:size]).center(lstr,'-'))


if __name__ == '__main__':
    n = int(input())
    #e-d-c-b-a  -b-c-d-e

    print_rangoli(n)