import json

names = ['abc', 'def', 'ghi', 'jkl', 'mno', 'pqr', 'stu', 'vwx', 'yz']

filename = 'c:/temp/data.json'

'''use load to read'''
with open(filename) as file:
    values = json.load(file)
print(values)

'''use dump to write'''
with open(filename, 'w') as file:
    json.dump(names, file)