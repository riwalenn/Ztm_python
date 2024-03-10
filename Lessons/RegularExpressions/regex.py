import re

pattern = re.compile('this')
pattern2 = re.compile('search this inside of this text please')
pattern3 = re.compile('search this inside')
string = "search this inside of this text please"

a = pattern.search(string)
b = pattern.findall(string)
c = pattern.fullmatch(string)
d = pattern2.fullmatch(string)
e = pattern3.match(string)  # search match à the beginning of the string
# print(a)
# print(a.group())
# print(b)
# print(c)  # none
# print(d)  # match
print(e)
