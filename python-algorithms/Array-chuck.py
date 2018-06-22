# Array chunk

def chunk(array, amount):
    new_array= []
    for y in range(0, len(array), amount):
        new_array.append(array[y:y+amount])
    print(new_array)


chunk([1,2,3,4,5,6,7,8,9], 3)
