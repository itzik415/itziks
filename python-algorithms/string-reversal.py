#String Reversal

def string_reversal(str):
    newString = ''
    for i in range(len(str)-1, -1, -1):
        newString = newString + str[i]

    print(newString)

string_reversal("Hello")
