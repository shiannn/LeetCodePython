import numpy as np
def binary_search(array,l,r,target):
    while(l<r):
        mid = l + (r-l)//2
        if(array[mid] == target):
            return mid
        elif(array[mid] < target):
            #binary_search(array,mid+1,r)
            l = mid+1
        elif(array[mid] > target):
            #binary_search(array,l,mid)
            r = mid
    return -1

if(__name__=='__main__'):
    #array = [1,2,3,4,5,6,7,8,9,10]
    #array = np.random.randint(0,100,size=50)
    a = np.arange(100)
    np.random.shuffle(a)
    A = a[0:10]
    print(A)
    A = list(A)
    print(A)
    A.sort()
    print (A)
    
    ans = binary_search(A,0,10,23)
    print(ans)