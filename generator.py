def getfun():
    yield 23
    yield 3
    yield 54

for value in genfun():
    print(value)
