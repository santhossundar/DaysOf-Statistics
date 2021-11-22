def quartiles(arr, size):
    if(len(arr) == size and size>=5):
        arr.sort()

        temp1 = []
        temp2 = []

        if(size%2!=0):
            for i in range(int(size/2)):
                temp1.append(arr[i])
            arr.reverse()
            for i in range(int(size/2)):
                temp2.append(arr[i])
                           
            if(len(temp1)%2!=0):
                print("1st Quartile is "+ str(temp1[round(len(temp1)/2)]-1))
            else:
                print("1st Quartile is "+ str((temp1[round(len(temp1)/2)-1] + temp1[round(len(temp1)/2+1)-1])/2))

            print("2nd Quartile is " + str(arr[round(len(arr)/2)]))

            if(len(temp2)%2!=0):
                print("3rd Quartile is "+ str(temp2[round(len(temp2)/2)]-1))
            else:
                print("3rd Quartile is "+ str((temp2[round(len(temp2)/2)-1] + temp2[round(len(temp1)/2+1)-1])/2))

        else:
            for i in range(int(size/2)):
                temp1.append(arr[i])
            arr.reverse()
            for i in range(int(size/2)):
                temp2.append(arr[i])
                           
            if(len(temp1)%2!=0):
                print("1st Quartile is "+ str(temp1[round(len(temp1)/2)]-1))
            else:
                print("1st Quartile is "+ str((temp1[round(len(temp1)/2)-1] + temp1[round(len(temp1)/2+1)-1])/2))

            print("2nd Quartile is " + str((arr[round(len(arr)/2)-1] + arr[round(len(arr)/2)])/2))

            if(len(temp2)%2!=0):
                print("3rd Quartile is "+ str(temp2[round(len(temp2)/2)]-1))
            else:
                print("3rd Quartile is "+ str((temp2[round(len(temp2)/2)-1] + temp2[round(len(temp1)/2+1)-1])/2))
    
    else:
        print("\nInvalid input!")
        
if __name__ == '__main__':
    
    size = int(input().strip())

    array = list(map(int, input().rstrip().split()))

    quartiles(array, size)