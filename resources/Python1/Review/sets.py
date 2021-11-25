# Dictionary Syntax
dictionary = { "key" : "value"}

# List Syntax
l1 = ['Nice']

# Set Syntax
s1 = {'Nice', 'Spice', 'Very'}
s2 = {'Very', 'Naice', 'Nice'}
s1.add('Something')
s1.discard('Something')
print(s1.union(s2))
print(s1.intersection(s2))

if 'something' in s1:
    print(True)