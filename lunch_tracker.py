
options = { 1: "Check my restaurants",
            2: "The restaurant you have visited",
            3: "Add new restaurant",
            4: "Delete restaurant",
            5: "quit"
}

restaurants = [ "chipotle",
               "farm burger",
               "ru san's"
]

visited = [ ["chipotle", 0],
            ["farm burger", 0],
            ["ru san's", 0]
]

x = True


def res_list():
    num = 1
    for i in restaurants:
        print "  " + str(num) + ": " + str(i)
        num += 1
    choiceRes = raw_input("\nWhat is your choice? ")
    for restaurant in range(0,len(restaurants)):
        if restaurant == int(choiceRes)-1:
            visited[restaurant][1] += 1
    return "You chose " + str(restaurants[1])

def addNew():
    name = raw_input("What is the restaurant name: ")
    restaurants.append(name)
    visited.append([name,0])

def delete():
    num = 1
    for i in restaurants:
        print "  " + str(num) + ": " + str(i)
        num += 1
    delName = raw_input("\nWhich restaurant would you like to delete: ")
    
    for i in range(0,len(visited)):
        if delName == visited[i][0]:  
            restaurants.remove(delName)
            print "\n  **" + delName + " deleted from list**"
            return    
    print "\n  **You put the wrong name try again**"
    delete()

while x:
    print "\nHello what would you like to do?\n"
    for key,value in options.iteritems():
        print "  " + str(key) + ": " + str(value)
    choiceOp = raw_input("\nWhat is your choice? " )
    
    if choiceOp == '1':
        print res_list()
        
    elif choiceOp == '2':
        for i in range(0,len(visited)):
            print visited[i][0] + ": " + str(visited[i][1])
        
    elif choiceOp == '3':
        print addNew()
    
    elif choiceOp == '4':
        delete()
    
    elif choiceOp == '5':
        x = False
        print "Bye see you next time!"
