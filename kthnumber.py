def solution(array, commands):
    answer = 0
    #1
    #cut the list
    #for i in range(0, len(commands)):
        #repeat for the whole whole commands
        #m = slice(commands[i, 0], len(commands))
        #array[] = array[m]
        #x = slice(0, commands[i, 1])
        #array[] = array[x]
    array = [1, 5, 2, 6, 3, 7, 4]
    abe = array[2:5]
    print(abe)

    #for a in range (commands[1], len(commands)):
    #    del array[(commands[1])]
    #for i in range (0, commands[0]):
    #    del array[0]
    # list.sort() -> 오름차순
    # list.reverse() -> 뒤집기
'''
    #2
    #organize in ascending order...
        onee = 1
        zero = 0
        for n in range (0, len(array)):
            if (array[zero]>array[onee]):
                qwe = array.pop(array[n])
                array.append(n)
            elif (array[zero]<array[onee]):
                zero = zero + 1
                onee = onee + 1
    # 5, 2, 6, 3
    # 2, 6, 3, 5
    # 
    #print the final number
    answer = array[commands[2]]
    
    return answer
'''
 #for a in range (commands[1], len(commands)):
    #    del array[(commands[1])]
    #for i in range (0, commands[0]):
    #    del array[0]
'''
        for n in range (1, len(array)):
            if (arr[n]>arr[0]):
                qwe = arr.pop(arr[n])
                arr.append(qwe)
            elif (arr[n]<arr[0]):
                qwe = arr.pop(arr[n])
                arr.append(qwe)
'''