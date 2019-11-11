
__version__ = "2019.11.11.01"
__author__ = "Muthukumar Subramanian"

# Example-1


class MyClass:
    def __init__(self, age=0):
        '''
        ..codeauthor:: Muthukumar Subramanian
        Usage:
              Required argument(s):
                  :param age: int
              Optional argument(s):
                  None
        :return: None
        '''
        self._age = age

    # getter method
    def get__age(self):
        '''
        ..codeauthor:: Muthukumar Subramanian
        Usage:
              Required argument(s):
                  None
              Optional argument(s):
                  None
        :return: _age
        '''
        return self._age

    # setter method
    def set__age(self, x):
        '''
        ..codeauthor:: Muthukumar Subramanian
        Usage:
              Required argument(s):
                  :param x: int
              Optional argument(s):
                  None
        :return: _age
        '''
        self._age = x


cls_obj = MyClass()
# setting the age using setter
cls_obj.set__age(2)

# retrieving age using getter
print("Example-1 - retrieving age using getter: {}".format(cls_obj.get__age()))

# Example-2


class MyClasss:
    def __init__(self):
        self._age = 0

    # function to get value of _age
    def get_age(self):
        '''
        ..codeauthor:: Muthukumar Subramanian
        Usage:
              Required argument(s):
                  None
              Optional argument(s):
                  None
        :return: _age
        '''
        print("Example-2 - getter method called".format())
        return self._age

    # function to set value of _age
    def set_age(self, a):
        '''
        ..codeauthor:: Muthukumar Subramanian
        Usage:
              Required argument(s):
                  :param a: int
              Optional argument(s):
                  None
        :return: _age
        '''
        print("Example-2 - setter method called".format())
        self._age = a

    # function to delete _age attribute
    def del_age(self):
        '''
        ..codeauthor:: Muthukumar Subramanian
        Usage:
              Required argument(s):
                  None
              Optional argument(s):
                  None
        :return: None
        '''
        print("Example-2 - before delete self dict: {}".format(self.__dict__))
        print("Example-2 - before delete: {}".format(self._age))
        del self._age
        print("Example-2 - after delete: {}".format(self.__dict__))

    age = property(get_age, set_age, del_age)


mark = MyClasss()
mark.age = 10
print("Example-2 - Mark: {}".format(mark.age))
del mark.age

# Example-3


class MyClasss:
    def __init__(self):
        '''
        ..codeauthor:: Muthukumar Subramanian
        Usage:
              Required argument(s):
                  None
              Optional argument(s):
                  None
        :return: None
        '''
        self._age = 0

    # using property decorator
    # a getter function
    @property
    def age(self):
        '''
        ..codeauthor:: Muthukumar Subramanian
        Usage:
              Required argument(s):
                  None
              Optional argument(s):
                  None
        :return: _age
        '''
        print("Example-3 - getter method called".format())
        return self._age

    # a setter function
    @age.setter
    def age(self, a):
        '''
        ..codeauthor:: Muthukumar Subramanian
        Usage:
              Required argument(s):
                  :param a: int
              Optional argument(s):
                  None
        :return: _age
        '''
        if (a < 18):
            raise ValueError("Sorry you age is below eligibility criteria")
        print("Example-3 - setter method called".format())
        self._age = a

    # a deleter function
    @age.deleter
    def age(self):
        '''
        ..codeauthor:: Muthukumar Subramanian
        Usage:
              Required argument(s):
                  None
              Optional argument(s):
                  None
        :return: None
        '''
        print("Example-3 - deleter method called".format())
        del self._age


mark = MyClasss()
mark.age = 19
print("Example-3 - Mark: {}".format(mark.age))
del mark.age

# Example-4


class MyClasss:
    def __init__(self):
        '''
        ..codeauthor:: Muthukumar Subramanian
        Usage:
              Required argument(s):
                  None
              Optional argument(s):
                  None
        :return: _age
        '''
        self._age = 0

    # using property decorator
    # a getter function
    @property
    def age(self):
        '''
        ..codeauthor:: Muthukumar Subramanian
        Usage:
              Required argument(s):
                  None
              Optional argument(s):
                  None
        :return: _age
        '''
        print("Example-4-1 - getter method called: {}".format(self._age))
        return self._age

    # a getter function - Above getter method will be overridden here
    @age.getter
    def age(self):
        '''
        ..codeauthor:: Muthukumar Subramanian
        Usage:
              Required argument(s):
                  None
              Optional argument(s):
                  None
        :return: _age
        '''
        print("Example-4-2 - getter method called: {}".format(self._age))
        return self._age

    # a setter function
    @age.setter
    def age(self, a):
        '''
        ..codeauthor:: Muthukumar Subramanian
        Usage:
              Required argument(s):
                  :param a: int
              Optional argument(s):
                  None
        :return: _age
        '''
        if a < 18:
            raise ValueError("Sorry you age is below eligibility criteria")
        print("Example-4 - setter method called".format())
        self._age = a

    # a deleter function
    @age.deleter
    def age(self):
        '''
        ..codeauthor:: Muthukumar Subramanian
        Usage:
              Required argument(s):
                  None
              Optional argument(s):
                  None
        :return: None
        '''
        print("Example-4 - deleter method called".format())
        del self._age


mark = MyClasss()
mark.age = 19
print("Example-4 - Mark: {}".format(mark.age))
del mark.age
