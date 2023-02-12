def profit(prices):
    if len(prices) < 2:
        return 0

    min_p = prices[0]
    max_p = 0

    for i in prices[1:]:
        if i < min_p:
            min_p = i
        else:
            max_p = max(max_p, i - min_p)

    print(max_p)

arr1 = []
x = int(input("insert how many elements you want:"))
for i in range(0, x):
    arr1.append(int(input("Enter next no :")))
print(arr1)
profit(arr1)
