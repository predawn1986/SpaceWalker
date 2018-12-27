from inspect import isfunction, isclass

one = __import__('math')
for key, value in one.__dict__.items():
    # if hasattr(value, '__call__'):
    if isfunction(value):
        print(key)

two = __import__('person')
for key, value in two.__dict__.items():
    if isclass(value):
        for m, n in value.__dict__.items():
            if isfunction(n) and m != '__init__':
                print(m, n.__doc__)
