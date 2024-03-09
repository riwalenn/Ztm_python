from collections import defaultdict

dictionary = defaultdict(lambda: 'does not exist', {'a': 1, 'b': 2})
print(dictionary['a'])
print(dictionary['c'])