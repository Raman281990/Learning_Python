### Dictionaries are data structures that are used to map key to values.

ages = {"Raman":1,"Gagan":2,"Sarbjit":3,"Navdeep":4}
print(ages["Raman"])
print(ages["Sarbjit"])


colors = {
    "red":[255,0,0],
    "green":[0,255,0],
    "blue":[0,0,255]
}
### referencing invalid key gives KeyError
#print(colors["yellow"])

## Only immutable objects can be used as keys in the dictionaries, mutuable objects such as list and dictionaries will give Type error
bad_dict ={
   # [1,2]: "Raman"
}
## you can use in and not in operator to check if particular key is in Dictionary or not

nums = {
  1: "one",
  2: "two",
  3: "three",
}
print(1 in nums)
print("three" in nums)
print(4 not in nums)

## Other functions in dictionaries..get method returns value

print(nums.get(1))
print(nums.get(4))#returns None if the key is not found

## you can also give default value in get function
print(nums.get(4,9))