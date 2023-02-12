def find_lead(arr):
    n = len(arr)
    leaders = []
    max_ele = arr[n-1]
    leaders.append(max_ele)
    for i in range(n-2, -1, -1):
        if arr[i] >= max_ele:
            max_ele = arr[i]
            leaders.append(max_ele)
    res = [*set(leaders)]
    res.sort(reverse=True)
    print("Leaders : ",res)



arr1 = []
x = int(input("insert how many elements you want:"))
for i in range(0, x):
    arr1.append(int(input("Enter next no :")))
print(arr1)
find_lead(arr1)


