#Fibonacci
#For getting the n amount of first numbers in the fibonacci list

def fib(n):
    fib_list = [1,1]
    for i in range(0, n-2):
        fib_list.append(fib_list[i]+ fib_list[i+1])
    print(fib_list)
    
fib(10)

#For getting the n number in the sequence

def fib_sequence(n):
    fib_list = [1,1]
    for i in range(0, n-2):
        fib_list.append(fib_list[i]+ fib_list[i+1])
    print(fib_list[n-1])




fib_sequence(10)



