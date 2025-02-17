import re

text = 'Hello my name is David. My phone number is 185-948-3759'
'''

print('name' in text) #True

pattern = 'nothing'
print(re.search(pattern, text)) #None

pattern = 'is'
print(re.search(pattern, text))

pattern = 'is'
print(re.findall(pattern, text))


'''
pattern = 'is'
for el in re.finditer(pattern, text):
    print(el.span())

p1 = r'\d{3}-\d{3}-\d{4}'
found = re.search(p1, text)
print(found.group()) #Value found




