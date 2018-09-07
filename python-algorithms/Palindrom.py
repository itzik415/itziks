#Palindroms

#Creating new string to the opsite way. If they are both the
#same we will get True else wi will get False
def is_palindrom(str):
    newStr = ''
    for i in range(len(str)-1, -1, -1):
        newStr = newStr + str[i]
    if newStr == str:
        print("True")
     else:
       print("False")

is_palindrom("abba")

#Compering the letters with each other. The first letter against the last one
# the second letter against the second from the end and so on.

def is_palindrom(str):
    num = 0
    for i in str:
        if i == str[-1+num]:
            num = num -1
        else:
            print("False")
            return False
    print("True")
    return True

is_palindrome("abccdcba")

