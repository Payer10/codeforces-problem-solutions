def quick_sort(arr):
    if(len(arr)==1):
        return 0
    else:
        pivot=arr[0]
        left=[x for x in arr[1:]if x<pivot]
        right=[x for x in arr[1:]if x>=pivot]
        return min(len(left),len(right))
for _ in range(int(input())):
    a,b=map(int,input().split())
    l=list(map(int,input().split()))
    print(quick_sort(l))
