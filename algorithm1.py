# -*- coding: utf-8 -*-

#1.

# x = 2520
# i = 10

# while x % i == 0:
#     i += 1
#     if i == 20:
#         print x
#         break

#     elif x % i != 0:
#         x += 2520
#         i = 10

#1. shiti way same problem

# x = 2520 
# y = True 

# while y:    
#     if x % 20 == 0 and x % 19 == 0 and x % 18 == 0 and x % 17 == 0 and x % 16 == 0 and x % 15 == 0 and x % 14 == 0 and x % 13 == 0 and x % 12 == 0 and x % 11 == 0: 
#         print x
#         y = False
#     else:
#         x += 2520 

#2.
# array =[]
# array1 =[]
# array2 =[]
# for i in range(100,1000):
#     for e in range(100,1000):
#         num = i * e
#         if len(str(num)) % 2 == 0:
#             if str(num)[0] == str(num)[5] and str(num)[1] == str(num)[4] and str(num)[2] == str(num)[3]:
#                 array.append(num)
#         elif len(str(num)) % 2 != 0:
#             if str(num)[0] == str(num)[4] and str(num)[1] == str(num)[3]:
#                 array.append(num)
                

# for k in range(100,1000):
#     if max(array) % k == 0:
#         array2.append(k)

# print max(array)
# print max(array2) 
# print max(array) / max(array2)

#3.
# for num in range(99,-1,-1):
#     if num % 7 == 0 and num % 5 == 0:
#         print """%s Bottles of Lite Miller, take one down,
#     pass it around, %s bottles of Lite beer on the wall.""" %(str(num), str(num-1))
#     elif num % 7 == 0:
#         print """%s Bottles of Miller, take one down,
#     pass it around, %s bottles of Miller on the wall.""" %(str(num), str(num-1))
#     elif num % 5 == 0:
#         print """%s Bottles of Lite beer, take one down,
#     pass it around, %s bottles of Lite beer on the wall.""" %(str(num), str(num-1))
#     else:
#         print """%s Bottles of beer, take one down,
#     pass it around, %s bottles of beer on the wall.""" %(str(num), str(num-1))
       
#3. Bonus Challenge 
# for num in range(99,0,-1):
#     while num % 7 == 0 and num % 5 == 0:
#         print """%s Bottles of Lite Miller, take one down,
#     pass it around, %s bottles of Lite beer on the wall.""" %(str(num), str(num-1))
#         break
#     while num % 7 == 0:
#         print """%s Bottles of Miller, take one down,
#     pass it around, %s bottles of Miller on the wall.""" %(str(num), str(num-1))
#         break
#     while num % 5 == 0:
#         print """%s Bottles of Lite beer, take one down,
#     pass it around, %s bottles of Lite beer on the wall.""" %(str(num), str(num-1))
#         break
#     while num % 7 != 0 or num % 5 != 0:
#         print """%s Bottles of beer, take one down,
#     pass it around, %s bottles of beer on the wall.""" %(str(num), str(num-1))
#         break
        
        

             

