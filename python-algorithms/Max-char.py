#Max Char

def max_char(string):
    array = []
    num = 0
    for a in string:
        array.append([a,num])

    for i in range(0, len(array)):
        for n in string:
            if array[i][0] == n:
                array[i][1] = array[i][1] + 1

    hieghstNum = ''
    for i in array:
        for z in array:
            if i[1] > z[1]:
                hieghstNum = ''
                hieghstNum = hieghstNum + i[0]

    print(hieghstNum)
        
                

max_char("f2222 676hjhj")
