
medals = dict()
medals['gold']=33
medals['silver']=17
medals['bronze']=12
print(medals)

print(medals.keys())

for k in medals:
    print(k)
print(list(medals.values()))
print(list(medals.items()))
# dictionaries are mutuable

print('raman' in medals)
print(medals.get('gold'))

# two aliases will refer to the same dictionary objects
# create copy of the dictionary using copy method
medals2 = medals.copy()
print(medals2)
