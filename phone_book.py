import pickle

main_menu = """
Electronic Phone Book
=====================
1. Look up an entry
2. Set an entery
3. Delete an entery
4. List all enteries
5. Save enteries
6. Laod enteries
7. Quit
"""

phoneBook = [
            ["Itzik", "954-343-2342"]
        ]
        
x = True


def look_up():
    personName = raw_input("\n  name: ")
    for i in range(0,len(phoneBook)):
        if personName == phoneBook[i][0]:
            return "  number: " + phoneBook[i][1] + "\n"
    for i in range(0,len(phoneBook)):
        if personName != phoneBook[i][0]:
            print "\n  **You put the wrong name try again**"
            break
    
    return look_up()
    

def set_entry():
    personName = raw_input("\n  name: ")
    personNumber = raw_input("  number: ")
    phoneBook.append([personName,personNumber])
    return "\n  " + personName + " " + "added to the list"
         
       
def delete():
    personName = raw_input("\n  name: ")
    for name in range(0,len(phoneBook)):
        if personName == phoneBook[name][0]:
            phoneBook.pop(name)
    return "\n  " + personName + " " + "has been deleted from the list"
        

def all_enteries():
    newPhoneBookDic = {}
    sort = raw_input("Would you like to sort by name or by number? \nPress '1' for name or '2' for number  ")
    for i in range(0,len(phoneBook)):
        newPhoneBookDic[phoneBook[i][0]] = phoneBook[i][1]
    if sort == '1':
        for key in sorted(newPhoneBookDic):
            print "\n  %s: %s" % (key, newPhoneBookDic[key])
    else:
        new = sorted((value,key) for (key,value) in newPhoneBookDic.items())
        print "\n"
        for key,value in new:
            print "  " +key + ": " + value + "\n"
    return " "
    

def save_enteries():
    myfile = open('phonebook.pickle', 'w')
    pickle.dump(phoneBook, myfile)
    myfile.close()
    return "\n  **Changes have been saved**"

def load_enteries():
    global phoneBook
    myfile = open('phonebook.pickle', 'r')
    phoneBook = pickle.load(myfile)
    return "\n  **Changes have been saved**"


while x:    
    print main_menu
    number = raw_input("What do you want to do (1-5)? ")
    if number == '1':
        print look_up()
    elif number == '2':
        print set_entry()
    elif number == '3':
        print delete()
    elif number == '4':
        print all_enteries()
    elif number == '5':
        print save_enteries()
    elif number == '6':
        print load_enteries()
    elif number == '7':
        x = False
        print "Bye!"
    else:
        print "\n  **YOU PRESS THE WRONG NUMBER TRY AGAIN**"

