# 1.sum the numbers
# numbers = [1,2,3,4,5,6]

# def sum(a):
#     total = 0
#     for i in numbers:
#         total = total + i
#     return total

# print sum(numbers)
     
# 2.largest number
# numbers = [7,-1,3,4,5,6]

# def largest(a):
#     largest = numbers[0]
#     for i in numbers:
#         if largest < i:
#             largest = i
#     return largest

# print largest(numbers)

#3.smallest number
# numbers = [7,-1,3,4,5,6]

# def largest(a):
#     largest = numbers[0]
#     for i in numbers:
#         if largest > i:
#             largest = i
#     return largest

# print largest(numbers)

#4.positive numbers
# numbers = [1,2,34,43,5,6,67-2]

# def even(a):
#     for i in numbers:
#         if i % 2 == 0:
#             if i > 0:
#                 print i
        
# even(numbers)

#5.positive number II
# numbers = [1,2,34,43,5,6,67-2]

# def even(a):
#     for i in numbers:
#         if i % 2 == 0:
#             print i
        
# even(numbers)

#6.multiply list
# numbers = [1,2,34,43,5,6,67,-2]
# factor = 2
# new_list = []

# def multiply(a,b):
#     for i in b:
#         new_list.append(a * i)
#     return new_list

# print multiply(factor,numbers) 


#7.multiply vector
# numbers1 = [1,2,3,3]
# numbers2 = [3,4,5,-2]
# new_list2 = []

# def multiply2(a,b):
#     i = 0
#     while i < len(a):
#         new_list2.append(a[i] * b[i])
#         i += 1
#     return new_list2

# print multiply2(numbers1,numbers2) 


#8.matrix edition
# numbers1 = [[2,3],
#             [1,2]]

# numbers2 = [[1,4],
#            [6,3]]

# def total(a,b):
#     new_list2 = []
#     for i in range(0,2):
#         new_list1 = []  
#         for e in range(0,2):
#             new_list1.append(a[i][e] + b[i][e])
#         new_list2.append(new_list1)
    
#     return new_list2

# print total(numbers1,numbers2)

#9.matrix edition II
# numbers1 = [[2,3,3,3],
#             [1,2,1,4]]

# numbers2 = [[1,4,3,4],
#            [6,3,2,2]]

# def total(a,b):
#     new_list2 = []
#     for i in range(0,2):
#         new_list1 = []  
#         for e in range(0,len(numbers2[0])):
#             new_list1.append(a[i][e] + b[i][e])
#         new_list2.append(new_list1)
    
#     return new_list2

# print total(numbers1,numbers2)

#10. De-dup
# numbers = [1,2,1,2,8,3,2,4,'f','f','ff']
# array = []

# def dup(a):
#     for i in numbers:
#         if i not in array:
#             array.append(i)
#     return array

# print dup(numbers)

#11. Bonus: Matrix Multiplication
numbers1 = [[2,-2], 
            [5,3]]   
            
numbers2 = [[-1,4],
            [7,-6]]

var1 = numbers1[0][0] * numbers2[0][0] 
var2 = numbers1[0][1] * numbers2[1][0] 
var3 = var1 + var2

print var3

