def my_enumerate(x):
    count = 0
    for i in x:
        yield count, i
        count += 1


for i, el in my_enumerate('stuff'):
    print i, el
