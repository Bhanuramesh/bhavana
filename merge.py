def mergesort(array):
     if len(array)>1:
         r=len(array)//2
         l=array[:r]
         M=array(l)
         mergesort(l)
         mergesort(M)
         i=j=k=0
         while i<len(l)and j<len(M):
               if l[i]<M[j]:
                  array[k]=l[i]
                  i+=1
               else:
                    array[k]=l[i]
                    i+=1
                    k+=1
         while i<len(l):
            array[k]=l[i]
            i+=1
            k+=1
        while j<len(M):
            array[k]=M[j]
            j+=1
            k+=1
def print list(array):
    for i in range(len(array)):
        print(array[i],end="")
    print()
array=[6,5,12,10,9,1]
mergesort(array)
print("sorted array is:")
print list(array)
