

#冒泡排序
def bubble_sort(alist,n):
    for i in range(n-1):
        for j in range(n-1):
            if alist[j] > alist[j+1]:
                temp = alist[j]
                alist[j] = alist[j+1]
                alist[j+1] = temp
                print(alist)
    print(alist)


alist = [2,1,4,3,7,6,9,5]
n = len(alist)

bubble_sort(alist,n)