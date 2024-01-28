def merge(arr,p,q,r):
    tmp = arr
    t = 1
    while (p<=q and (q+1) <=r):
        if arr[p] <= arr[q+1]:
            t+=1
            p+=1
            tmp[t] = arr[p]
            
            
def merge_sort(arr,p,r):
    if p < r:
        q = (p+r)/2
        merge_sort(arr,p,q)
        merge_sort(arr,q+1,r)
        merge(arr,p,q,r)
        

n, k = map(int, input().split())

arr = list(map(int,input().split()))

