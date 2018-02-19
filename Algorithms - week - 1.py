#1.
# def cal():
#     num = 0
#     total = 0
#     while num < 1000:
#         if num % 3 == 0 or num % 5 == 0:
#             total = total + num
#             num += 1
#         else:
#             num += 1
#     return total

# print cal()

#2.
# def fib():    
#     array =[1,2,3]
#     i = 2
#     total = 0
#     while array[-1] < 4000000 :
#         array[i] = array[i-1] + array[i-2] 
#         array.append(array[i])
#         i += 1
#     for j in array:
#         if j % 2 == 0:
#             total += j
#         else:
#             j += 1
#     return total 
# print fib()

#3.
# x = 600851475143 

# def prime():
#     array = []
#     t = []
#     b = []
#     i = 2
#     while i < 1000000:
#         if x % i == 0:
#             array.append(i)
#             i += 1
#         else:
#             i += 1
#     y = 6
   
#     for i in range(0,7):
#         t.append(array[i])

#     while y >= 0:
#         t.append(x / array[y])
#         y = y - 1
    
#     for i in t:
#         e = 3
#         if i % (e/2) != 0:
#             b.append(i)
#             e += 1
#     return b


# print prime()

# Better solution
number = 600851475143
while True:
    foundFactor = False
    for i in xrange(2, number):
        if number % i == 0:
            number = number / i
            foundFactor = True
            break
    if not foundFactor:
        break
print number











