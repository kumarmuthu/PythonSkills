
__version__ = "2019.11.11.01"
__author__ = "Muthukumar Subramanian"

# Example-1
# Examples of used defined polymorphic functions


def add(x, y, z=0):
    return x + y + z


# Driver code
print("Example-1 - Call 'add' function with default zero: {}".format(add(2, 3)))
print("Example-1 - Call 'add' function with 3rd value: {}".format(add(2, 3, 4)))

# Example-2
# Polymorphism with class methods


class India(object):
    '''
    ..codeauthor:: Muthukumar Subramanian
    '''

    def __init__(self):
        pass

    def capital(self):
        print("Example-2 - New Delhi is the capital of India.".format())

    def language(self):
        print("Example-2 - Hindi the primary language of India.".format())

    def type(self):
        print("Example-2 - India is a developing country.".format())


class USA(object):
    '''
    ..codeauthor:: Muthukumar Subramanian
    '''

    def __init__(self):
        pass

    def capital(self):
        print("Example-2 - Washington, D.C. is the capital of USA.".format())

    def language(self):
        print("Example-2 - English is the primary language of USA.".format())

    def type(self):
        print("Example-2 - USA is a developed country.".format())


obj_ind = India()
obj_usa = USA()
for country in (obj_ind, obj_usa):
    country.capital()
    country.language()
    country.type()

# Example-3
# Polymorphism with Inheritance(the child class is known as 'Method Overriding')


class Bird(object):
    '''
    ..codeauthor:: Muthukumar Subramanian
    '''

    def __init__(self):
        pass

    def intro(self):
        print("Example-3 - There are many types of birds.".format())

    def flight(self):
        print("Example-3 - Most of the birds can fly but some cannot.".format())


class Sparrow(Bird):
    '''
    ..codeauthor:: Muthukumar Subramanian
    '''

    def __init__(self):
        pass

    def flight(self):
        print("Example-3 - Sparrows can fly.".format())


class Ostrich(Bird):
    '''
    ..codeauthor:: Muthukumar Subramanian
    '''

    def __init__(self):
        pass

    def flight(self):
        print("Example-3 - Ostriches cannot fly.".format())


obj_bird = Bird()
obj_spr = Sparrow()
obj_ost = Ostrich()

obj_bird.intro()
obj_bird.flight()

obj_spr.intro()
obj_spr.flight()

obj_ost.intro()
obj_ost.flight()

# Example-4
# Polymorphism with a Function and objects


class India(object):
    '''
    ..codeauthor:: Muthukumar Subramanian
    '''

    def __init__(self):
        pass

    def capital(self):
        print("Example-4 - New Delhi is the capital of India.".format())

    def language(self):
        print("Example-4 - Hindi the primary language of India.".format())

    def type(self):
        print("Example-4 - India is a developing country.".format())


class USA(object):
    '''
    ..codeauthor:: Muthukumar Subramanian
    '''

    def __init__(self):
        pass

    def capital(self):
        print("Example-4 - Washington, D.C. is the capital of USA.".format())

    def language(self):
        print("Example-4 - English is the primary language of USA.".format())

    def type(self):
        print("Example-4 - USA is a developed country.".format())


def func(obj):
    obj.capital()
    obj.language()
    obj.type()


obj_ind = India()
obj_usa = USA()

func(obj_ind)
func(obj_usa)
