from timeit import Timer

def binarysearch(sortedlist,value):
    start = 0
    end = len(sortedlist)-1
    while start <= end:
        mid = int((start+end)/2)
        if sortedlist[mid]==value:
            print("binarysearch: Found @ ", mid)
            return
        elif sortedlist[mid]>value:
            end = mid-1
        else:
            start = mid+1
    print("binarysearch: Not found %s"%value)


def linearsearch(list,value):
    for x in range(len(list)):
        if list[x] == value:
            print("linearsearch: Found @ ", x)
            return
    print("linearsearch: Not found %s"%value)




time1 = Timer("binarysearch(list(range(100000)),99999)","from linearVSbinarySearch_timeit import binarysearch").timeit(3)
#time2 = Timer("linearsearch(list(range(100000)),99999)","from linearVSbinarySearch_timeit import linearsearch").timeit(3)


time2 = Timer("""
a = list(range(100000))
linearsearch(a,99999)
""","from linearVSbinarySearch_timeit import linearsearch").timeit(3)

print("binarysearch:  %7.6f " %time1)
print("linearsearch:  %7.6f " %time2)
