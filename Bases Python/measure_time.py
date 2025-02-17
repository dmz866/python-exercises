import time
import timeit

def test_for(n):
    l = []

    for e in range(0, n + 1):
        l.append(e)

    return l

def test_while(n):
    l = []
    e = 0

    while e <= n:
        l.append(e)
        e+= 1

    return l
'''

i = time.time()
print(test_for(15))
f = time.time()

print(f'For loop time: ${f - i}')

i = time.time()
print(test_while(15))
f = time.time()
print(f'While loop time: ${f - i}')

'''

test1 = timeit.timeit(lambda: test_for(15))
print(f'For loop time: ${test1}')
test2 = timeit.timeit(lambda: test_while(15))
print(f'While loop time: ${test2}')
