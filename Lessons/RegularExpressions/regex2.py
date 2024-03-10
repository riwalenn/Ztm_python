import re

pattern = re.compile(r'([a-zA-Z]).([a])')
string = 'search this inside'

a = pattern.search(string)
print(a.group())  # return sea
print(a.group(2))  # return a
