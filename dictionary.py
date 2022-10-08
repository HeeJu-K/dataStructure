### dictionaries

#lists have index, dictionary have keys 

#declared with empty {}
from cgi import test


testDictionary = {}
key1 = 1
testDictionary[key1] = "data1"
testDictionary["key2"] = 2
testDictionary["key3"] = "data3"

print("printing dictionary itself", testDictionary)
print("printing dictionary keys", testDictionary.keys())
print("printing dictionary items", testDictionary.items()) # returns tuples (key value pair)

#this function puts data attribute to dictionary 
class testClass:
    def __init__(dict):
        dict.data = "data from class"
        dict.key = "key from class"

instance = testClass()
testDictionary["class"] = instance
print("printing data from class", testDictionary["class"], testDictionary["class"].data, testDictionary["class"].key)
print("printing keys and items", testDictionary.keys(), testDictionary.items())
for key, value in testDictionary.items():
    print("in for loop", key, value)