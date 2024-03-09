from collections import OrderedDict

d = OrderedDict()
d['a'] = 1
d['b'] = 2

d2 = OrderedDict()
d2['a'] = 1
d2['b'] = 2

print(d2 == d)
# Recently, the Python has made Dictionaries ordered by default! So unless you need to maintain older version of
# Python (older than 3.7), you no longer need to use ordered dict, you can just use regular dictionaries!
