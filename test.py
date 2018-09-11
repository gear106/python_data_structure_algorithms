def shellSort(alist):
    gap = len(alist) // 2
    while gap > 0:
        for start in range(gap):
            gapShellSort(alist, start, gap)
        gap = gap // 2
    
def gapShellSort(alist, start, gap):
    for i in range(start+gap, len(alist), gap):
        currentvalue = alist[i]
        position = i
        while position >= gap and alist[position-gap] > currentvalue:
            alist[position] = alist[position-gap]
            position -= gap
        alist[position] = currentvalue


def insertionSort(alist):
    for i in range(len(alist)):
        currentvalue = alist[i]
        position = i
        while position > 0 and alist[position-1] > currentvalue:
            alist[position] = alist[position-1]
            position -= 1
        alist[position] = currentvalue
        
def bubbleSort(alist):
    for i in range(len(alist)-1, 0, -1):
        for j in range(i):
            if alist[j] > alist[j+1]:
                alist[j], alist[j+1] = alist[j+1], alist[j]
                
def shortBubbleSort(alist):
    exchange = True
    pos = len(alist) - 1
    while pos > 0 and exchange:
        exchange = False
        for i in range(pos):
            if alist[i] > alist[i+1]:
                exchange = True
                alist[i], alist[i+1] = alist[i+1], alist[i]
                
def selectionSort(alist):
    for i in range(len(alist)-1, 0, -1):
        maxid = 0
        for j in range(1, i+1):
            if alist[j] > alist[maxid]:
                maxid = j
        alist[i], alist[maxid] = alist[maxid], alist[i]
        
        
def mergeSort(alist):
    if len(alist) > 1:
        mid = len(alist) // 2
        left = alist[:mid]
        right = alist[mid:]
         
        mergeSort(left)
        mergeSort(right)
         
        i,j,k = 0,0,0
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                alist[k] = left[i]
                i += 1
            else:
                alist[k] = right[j]
                j += 1
            k += 1
        
        while i < len(left):
            alist[k] = left[i]
            i += 1
            k += 1
        while j < len(right):
            alist[k] = right[j]
            j += 1
            k += 1
        
                
def quickSort(alist, first, last):
    left = first
    right = last
    if left >= right:
        return

    pivot = alist[left]
    
    while left < right:
        while left < right and alist[right] >= pivot:
            right -= 1
        alist[left] = alist[right]
        while left < right and alist[left] <= pivot:
            left += 1
        alist[right] = alist[left]
    alist[left] = pivot
    
    quickSort(alist, first, left-1)
    quickSort(alist, left+1, last)
    
    
    
def binarySearch(alist, item):
    left = 0
    right = len(alist) - 1
    found = False
    
    while left <= right and not found:
        mid = (left + right) // 2
        if item == alist[mid]:
            found = True
        else:              
            if item < alist[mid]:
                right = mid-1
            else:
                left = mid+1
    return found

def binarySearch2(alist, item):
    if len(alist) == 0:
        return False
    else:
        mid = len(alist) // 2
        if item == alist[mid]:
            return True
        else:          
            if item < alist[mid]:
                return binarySearch2(alist[:mid], item)
            else:
                return binarySearch2(alist[mid+1:], item)
    
def sequentialSearch(alist, item):
    pos = 0
    found = False
    while pos < len(alist) and not found:
        if alist[pos] == item:
            found = True
        else:
            pos += 1
    return found


def sequentialSearch2(alist, item):
    pos = 0 
    found = False
    stop = False
    while pos < len(alist) and not found and not stop:
        if alist[pos] == item:
            found = True
        else:
            if alist[pos] > item:
                stop = True
            else:
                pos += 1
    return found
        
        
            







        
        
            
if __name__ == '__main__':
    test1 = [54,26,93,17,77,31,44,55,20]
    test2 = [54,26,93,17,77,31,44,55,20]
    test3 = [54,26,93,17,77,31,44,55,20]
    test4 = [54,26,93,17,77,31,44,55,20]
    test5 = [54,26,93,17,77,31,44,55,20]
    test6 = [54,26,93,17,77,31,44,55,20]
    shellSort(test5)
    print('shell\n',test5)
    
    insertionSort(test4)
    print('insert\n',test4)
    
    bubbleSort(test1)
    print('bubble\n',test1)
    
    shortBubbleSort(test2)
    print('shortbubble\n',test2)
    
    selectionSort(test3)
    print('selection\n',test3)
    
    mergeSort(test6)
    print('merge\n',test6)
    
    quickSort(test6, 0, len(test6)-1)
    print('quick\n',test6)
    
    testlist = [0,1,3,4,5,6,8]
    print(binarySearch2(testlist, 6))
    print(sequentialSearch2(testlist, 8))
