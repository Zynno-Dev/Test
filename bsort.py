arr=[1, 2, 3, 2, 1, 3, 1]
ord=False
while ord==False:
    ord=True
    for i in range(len(arr)-1):
        if arr[i] > arr[i+1]:
            aux=arr[i]
            arr[i]=arr[i+1]
            arr[i+1]=aux
            ord=False

print(arr)