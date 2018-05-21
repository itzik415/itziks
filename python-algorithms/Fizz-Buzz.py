#Fizz Buzz

def fizz_buzz(num):
    for i in range(num, 1, -1):
        if i % 15 == 0 :
            print("FIZZBUZZ")
        elif i % 5 == 0:
            print("FIZZ")
        elif i % 3 == 0:
            print("BUZZ")
        else:
            print(i)

fizz_buzz(100)
            
