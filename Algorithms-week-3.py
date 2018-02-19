#1.

#How many blue moon there are between 2000-2999
#full moon each 29.5 days
#every 4 years lype year leap year

month = [31,28,31,30,31,30,31,31,30,31,30,31]
# once every four years 
month2 = [31,29,31,30,31,30,31,31,30,31,30,31]

# month_dic = {"1" : 31, "2" : 28, "3" : 31, "4" : 30,
#              "5" : 31, "6" : 30, "7" : 31, "8" : 31,
#              "9" : 30, "10" : 31, "11" : 30, "12" : 31}

counter = 0

full_moon = [-8.5]


for t in range(2000,3000):
    moon = 0
    while moon < len(full_moon):
        i = 0
        while i < len(month):
            if (full_moon[-1] + 29.5) > month[i]:
                full_moon.append((full_moon[-1] + 29.5) % month[i])
                i += 1
            else:
                full_moon.append(full_moon[-1] + 29.5)
                i += 1
        moon += 13000

for i in full_moon:
    if (i >= 0.5 and i <= 1.5) and (i+1 >= 30 and i+1 <= 31):
        counter += 1

print counter

