#capitalize

def capitalize(str):
    new_str = ''
    for i in range(-1, len(str)-1):
        if str[i] == ' ' or i == -1:
            new_str = new_str + str[i+1].upper()
        else:
            new_str = new_str + str[i+1]

    print(new_str)

capitalize("how are you?")

#Solution-2

def capitalize(str):
    split_str = str.split()
    new_array = []
    for i in split_str:
        new_array.append(i[0].upper() + i[1:])
        
    print(' '.join(new_array))

capitalize(' how are you?')

