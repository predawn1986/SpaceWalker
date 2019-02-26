def add(a, b):
    '''
    :param a:
    :param b:
    :return:
    '''
    return a + b

class People():
    def __int__(self, name, age):
        self.age = age
        self.name = name

    def get_name(self):
        print(self.name)

    def get_age(self):
        print(self.age)

print(add.__doc__)
print(type(add))
print(add.__name__)