def bubblesort(N):
    for possnum in range(len(N)-1,0,-1):
        for i in range(possnum):
            if N[i]> N[i+1]:
                N[i],N[i+1]=N[i+1],N[i]

N=[54,26,93,17,77,31,44,55,20]
bubblesort(N)
print(N)


###selectionsort

def selectionsort(N):
    for i in range(len(N)-1,0,-1):
        positionofmax=0
        for location in range(1,i+1):
            if N[location]> N[positionofmax]:
                positionofmax=location
        temp=N[i]
        N[i]=N[positionofmax]
        N[positionofmax]=temp



N=[54,26,93,17,77,31,44,55,20]
selectionsort(N)
print(N)


####shakersort

###shakersort
def  shaker_sort(N):
    def swap(i, j):
        N[i], N[j] =N[j], N[i]

    upper = len(N) - 1
    lower = 0

    no_swap = False
    while (not no_swap and upper - lower > 1):
        no_swap = True
        for j in range(lower, upper):
            if N[j + 1] < N[j]:
                swap(j + 1, j)
                no_swap = False
        upper = upper - 1

        for j in range(upper, lower, -1):
            if N[j - 1] > N[j]:
                swap(j - 1, j)
                no_swap = False
        lower = lower + 1
N=[3,9,7,5,3,2,1,8,10]
shaker_sort(N)
print(N)
