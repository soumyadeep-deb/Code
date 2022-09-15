def merge(arr,s,mid,e):
    len1 = mid - s +1
    len2 = e - mid

    # Copy the left side into a new array
    k = s
    leftSide = []
    for i in range(len1):
        leftSide.append(arr[k])
        k+=1
    

    # Copy the right side into a new array
    k = mid+1
    rightSide = []
    for i in range(len2):
        rightSide.append(arr[k])
        k+=1


    # Merge 2 sorted lists problem
    ptr1,ptr2 = 0,0
    k = s

    while (ptr1<len1) and (ptr2<len2):
        if leftSide[ptr1] > rightSide[ptr2]:
            arr[k] = rightSide[ptr2]
            ptr2+=1
        else:
            arr[k] = leftSide[ptr1]
            ptr1+=1
        k+=1
    

    while ptr1<len1:
        arr[k] = leftSide[ptr1]
        ptr1+=1
        k+=1
    while ptr2<len2:
        arr[k] = rightSide[ptr2]
        ptr2+=1
        k+=1

    

def mergeSort(arr,s,e):
    if s>=e:
        return
    
    mid = (s+e)//2

    # Call Merge Sort on Left side
    mergeSort(arr,s,mid)

    # Call Merge Sort on Right side
    mergeSort(arr,mid+1,e)

    # At last, merge the sorted sub arrays
    merge(arr,s,mid,e)
