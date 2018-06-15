#Two sided step pyramid

def hashes_pyramid(n):
    number = 0
    for i in range(0,n):
        print("'" + (n-i-1) * ' '+ (1+number) * "#" + (n-i-1) * ' ' + "'")
        number += 2

hashes_pyramid(3)
