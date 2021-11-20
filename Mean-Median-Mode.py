# Input Handling

n = input()

li = []

for p in n.split():
    li.append(int(p))

print(li)

# Finding Mean Value

total = 0

for i in range(len(li)):
    total = total+li[i]
    
mean = total/len(li)
print(mean)

# Finding median Value

arrSort = sorted(li)

firMid = int(len(arrSort)/2)

if (len(arrSort)%2 == 0):
    intCon = int(len(arrSort))
    secMid = int(intCon/2)
    firMid = int(intCon/2 - 1)
    median = (arrSort[firMid]+arrSort[secMid])/2
    print(median)
else:
    odd = int(len(arrSort)/2 - .5)
    print(arrSort[odd])
    
# Finding Mode Value

newCount = 0

for k in range(len(arrSort)):
    curCount = arrSort.count(arrSort[k])
    
    if(newCount < curCount):
        newCount = curCount
        mode = arrSort[k]

print(mode)
    

