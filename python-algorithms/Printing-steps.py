#Printing steps

def hashes(n):
    for i in range(0, n):
        print("'" + (n-(n-i-1)) * "#" + (n-(i+1)) * " " + "'")

hashes(20)

    
