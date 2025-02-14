from collections import Counter, defaultdict, namedtuple


#returns a diccionary
let = ['a', 'a', 'a', 'b', 'c', 'c', 'b','b','b','b']
count = Counter(let)
print(count)
# elements according to the frequency in decreasing order
print(count.most_common())
print(count.most_common(2))
print(Counter('al pan pan y al vino vino'.split()))


########################################################

midic = defaultdict(lambda: "valor por defecto")
midic['1'] = 'uno'

print(midic)
print(midic['key_no_existe']) # valor por defecto

########################################################

#type Person
Person = namedtuple('Person', ['name', 'height', 'weight'])
p = Person('Dosh', '1.71', '65')

print(p.name)
print(p[0])

