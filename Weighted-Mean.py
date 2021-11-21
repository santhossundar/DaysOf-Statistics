size = int(input().strip())

values = list(map(int, input().rstrip().split()))

weights = list(map(int, input().rstrip().split()))


temp = []

if(len(values) == size and len(weights) == size):
    for i in range(size):
        product = values[i] * weights[i]
        temp.append(product)

    sum = 0
    for x in range(size):
        sum += temp[x]

    wSum = 0
    for y in range(len(weights)):
        wSum += weights[y]


    print("\nWeighted Mean is " + str(round(sum/wSum, 4)))

else:
    print("\nInvalid input!")
    