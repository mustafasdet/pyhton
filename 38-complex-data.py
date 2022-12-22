import pprint
# pprint: pretty print

people = {}

people['Arthur'] = {'Name': 'Arthur Dent',
                    'Gender': 'Male',
                    'Occupation': 'Sandwich-Maker',
                    'Home Planet': 'Earth'}

people['Trillian'] = {'Name': 'Tricia McMillan',
                      'Gender': 'Female',
                      'Occupation': 'Mathematician',
                      'Home Planet': 'Earth'}


people['Robot'] = {'Name': 'Marvin',
                   'Gender': 'Unknown',
                   'Occupation': 'Paranoid Android',
                   'Home Planet': 'Unknown'}

people['Ford'] = {'Name': 'Ford Prefect',
                  'Gender': 'Male',
                  'Occupation': 'Researcher',
                  'Home Planet': 'Betelgeuse Seven'}
# print without pretty print (pprint)
print(people)

# print people with pprint
pprint.pprint(people)

# pprint the key Arthur
pprint.pprint(people['Arthur'])

# pprint the key Arthur>>Occupation
pprint.pprint(people['Arthur']['Occupation'])  # 'Sandwich-Maker'

# print same key Arthur>>Occupation without pprint
print(people['Arthur']['Occupation'])  # Sandwich-Maker
