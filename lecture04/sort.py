def findmax(a) :
    max = -1
    for i in range(len(a)) :
        if max <= a[i] :
            max = a[i]
    return max

def findmin(a) :
    min = 999999999999
    for i in range(len(a)) :
        if a[i] <= min :
            min = a[i]
    return min

def sortnum(a) : 
    for i in range(len(a)) :
        res = findmax()


a = [1,3,6,5,5,9,4,52,3,2,2,255,1023]
