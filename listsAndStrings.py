#String are immutabele you will get error
b = "abc"
#b[0]=''
print(b)

##list are mutable

c = list()
c.append(5)
c.append(10)
c.append(1)
print(len(c))
print(c)

#### list have other functions such as max,min,sum

print(max(c))
print(min(c))
print(sum(c))

## Concatenation of list

fruits =["apple","pineapple"]
vegetables=["ladyfinger","Tomato"]
mixed = fruits+vegetables
print(mixed)

### slicing the list
print(mixed[1:3])

## Deleting elements from the list
del fruits[0]
print(fruits)