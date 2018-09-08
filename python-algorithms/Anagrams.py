#Anagrams

import re

def anagram(str1, str2):
    new_str1 = sorted(re.sub(r"[^a-z0-9]","",str1.lower()))
    new_str2 = sorted(re.sub(r"[^a-z0-9]","",str2.lower()))
    if new_str1 == new_str2:
        print("True")
        return True
    else:
        print('false')
        return False
        

            

anagram("aFsd#3", "Bdsa3")
