

ages_dict = {'Bill': 17, 'Jane': 35, 'Jack': 56, 'Sarah': 12}
name = input('Name: ')
age = int(input('Age: '))

ages_dict[name] = age
for name in ages_dict:
    print('{} - {}'.format(name, ages_dict[name]))

# produce the same result as above
for name, age in ages_dict.items():
    print('{} - {}'.format(name, age))

# filtering
new_ones = {name: age for name, age in ages_dict.items() if age < 18}
print(new_ones)
