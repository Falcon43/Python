

def binarysearch(sortedlist,value):
    start = 0
    end = len(sortedlist)-1
    while start <= end:
        mid = int((start+end)/2)
        if sortedlist[mid]==value:
            print("Found @ ", mid)
            return
        elif sortedlist[mid]>value:
            end = mid-1
            print(start," ... ",end)
        else:
            start = mid+1
            print(start," ... ",end)



a = list(range(100))
b = [44,3,34,1,7,87,56,43,22,66,75,88,32,79,35,97,433,542,43,5,66,222,99]
print(sorted(a))
print(sorted(b))
binarysearch(sorted(a),77)
binarysearch(sorted(b),222)