def heapify(mylist, n ,i):
    max , left , right = i , 2*i + 1, 2*i + 2
    if left <= n and mylist[left] > mylist[max]:
        max = left
    if right <=n and mylist[right] > mylist[max]:
        max = right
    if max != i:
        mylist[i], mylist[max] = mylist[max], mylist[i]

        heapify(mylist, n, max)

def heapsort(mylist):
    n = len(mylist)
    for i in range(n//2, -1, -1):
        heapify(mylist, n-1, i)

    for i in range(n-1, -1, -1):
        mylist[i], mylist[0] = mylist[0], mylist[i]
        heapify(mylist, i-1, 0)


mylist = [11, 541, 7, 168, 24, 0, -8, -15, -478, 57, 149, -845, 5, 289, -9]
heapsort(mylist)
print(mylist)