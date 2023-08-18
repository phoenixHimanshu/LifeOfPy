import  array as arr
import fileinput



if __name__ == '__main__':
    a =  arr.array('I',[10,11,12,13])

    for x in a:
        print(x)

    print(a.itemsize)
    print(a.tobytes())
    #print(a.tofile(fileinput.filename()))  
      