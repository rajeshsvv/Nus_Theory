import re
value = "two 2  four 4  six 6"
#separate those non-digit characters
res = re.split ("\D+" , value)
# print the result
for elements in res :
    print (elements)