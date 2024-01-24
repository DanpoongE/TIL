person = {
    'name': 'Alice', 
    'age': 25
    }

print(person['name'])
print(person.get('name'))
print(person.get('country', '키가 없습니다.'))

print(person.keys()) #dict_keys(['name', 'age'])

for key in person.keys():
    print(key) 
    #name   
    #age

print(person.values()) #dict_values(['Alice', 25])

for value in person.values():
    print(value)
    #Alice
    #25
    
print(person.items()) #dict_items([('name', 'Alice'), ('age', 25)])

for key, value in person.items():
    print(key, value)
    #name Alice
    #age 25

print(person.pop('age')) #25
print(person) #{'name': 'Alice'}
print(person.pop('con'))

person.clear()
print(person)