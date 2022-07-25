from collections import Counter
list = ['red','blue','red','green','blue','blue']
print(dict(Counter(list)))
print(Counter(list)['blue'])
