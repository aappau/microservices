"""
Dictionary
 - key-value pairs
 - unordered
 - mutable
 - allows duplicates
"""

# dictionary definition
items = {
    "name": "Tony",
    "age": 30,
    "city": "Joppa"
}

item2 = dict(name="John", age="26", city="Rockville")


#accessing values
name = items['name']


# add new key
items['email'] = "dev@email.com"


# delete key
del item2['age']

items.pop("age")

# check of key exits
if "name" in items:
    print(items['name'])
