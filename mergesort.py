def merge(list1, list2, m, n, c):                  
    i = 0
    j = 0
    c.clear()
    
    while(i<m and j<n):
        if list1[i] <= list2[j]:
            c.append(list1[i])
            i += 1
        else:
            c.append(list2[j])
            j += 1
        
    for p in range(i,m):                           
        c.append(list1[p])
        
    for q in range(j,n):
        c.append(list2[q])
        

    
    
            
            
    
def Merge_Sort(array, low, high):
    
    if low!=high-1:
        mid = (low+high)//2
        arr1 = array[:mid]
        arr2 = array[mid:]
        

        Merge_Sort(arr1, 0, mid)
        Merge_Sort(arr2, mid, high)

        merge(arr1, arr2, len(arr1), len(arr2), array)
        

A = [9,8,7,6,1,2]

Merge_Sort(A, 0, len(A))

print(A)
