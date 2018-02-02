# 1.
# phonebook_dict = {
#   'Alice': '703-493-1834',
#   'Bob': '857-384-1234',
#   'Elizabeth': '484-584-2923'
# }

# phonebook_dict['Kareem'] = '938-489-1234'
# phonebook_dict['Alice'] = None
# phonebook_dict['Bob'] = '968-345-2345'

# print phonebook_dict

# 2.
# ramit = {
#   'name': 'Ramit',
#   'email': 'ramit@gmail.com',
#   'interests': ['movies', 'tennis'],
#   'friends': [
#     {
#       'name': 'Jasmine',
#       'email': 'jasmine@yahoo.com',
#       'interests': ['photography', 'tennis']
#     },
#     {
#       'name': 'Jan',
#       'email': 'jan@hotmail.com',
#       'interests': ['movies', 'tv']
#     }
#   ]
# }

# print ramit['email']
# print ramit['interests'][0]
# print ramit['friends'][0]['email']
# print ramit['friends'][1]['interests'][1]



# 3.
# word = raw_input('please enter a word: ')
# dictionary = {}

# for i in word:
#     if i not in dictionary:
#         dictionary[str(i)] = 1
#     else:
#         dictionary[str(i)] = dictionary[i] + 1

# print dictionary

# 4.
# sentence = str(raw_input('please enter a sentence: '))
# dictionary = {}
# sentence2 = sentence.split()
   
# for i in sentence2:
#     if i not in dictionary:
#         dictionary[str(i)] = 1
#     else:
#         dictionary[str(i)] = dictionary[i] + 1

# print dictionary


# 5.
# sentence = raw_input('please enter a sentence: ')
# dictionary = {}
# sentence2 = sentence.split()
   
# for i in sentence2:
#     if i not in dictionary:
#         dictionary[str(i)] = 1
#     else:
#         dictionary[str(i)] = dictionary[i] + 1

# sort_by_keys = sorted(dictionary, key=dictionary.__getitem__)
# sort_by_values = sorted(dictionary.values())

# print "The top 3 words are: "

# for i in range(1,4):
#     print str(sort_by_keys[-i]) + ":" + str(sort_by_values[-i])
    






















