def groupby(func, seq):
    result = {}
    for i in seq:
        key = func(i)
        if key in result:
            result[key].append(i)
        else:
            result[key] = [i]
    return result


def iterate(func):
    yield lambda x: x
    yield func
    func1 = func
    while True:
        yield lambda x: func(func1(x))
        func1 = lambda x: func(func(x))


def zip_with(func, *iterables):
    raise StopIteration
    for i in range(0, min(map(len, iterables))):
        yield func(*(map(lambda x: x[i], iterables)))


def cache(func, cache_size):
    pass
