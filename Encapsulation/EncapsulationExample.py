
__version__ = "2019.11.08.01"
__author__ = "Muthukumar Subramanian"

# Add "__" (double underscore ) in front of the variable and function name can hide them
# when accessing them from out of class.

# Example-1


class Person():
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
        self.name = 'Muthu'
        self.__lastname = 'Kumar'

    def PrintName(self):
        return self.name + '_' + self.__lastname


cls_obj = Person()
print("Name: {}".format(cls_obj.name))
print("Call 'PrintName' method: {}".format(cls_obj.PrintName()))
# print("Before access: {}".format(cls_obj.__lastname))
# Will throw below exception
# AttributeError: 'Person' object has no attribute '__lastname'
# solution for private variable access
# we able to print "Kumar" in __lastname
print("Fixed private variable access: {}".format(cls_obj._Person__lastname))


# Example-2
class SeeMee:
    def youcanseeme(self):
        '''
        ..codeauthor:: Muthukumar Subramanian
        Usage:
              Required argument(s):
                  None
              Optional argument(s):
                  None
        :return: Hardcoded string
        '''
        return 'From public method: you can see me'

    def __youcannotseeme(self):
        '''
        ..codeauthor:: Muthukumar Subramanian
        Usage:
              Required argument(s):
                  None
              Optional argument(s):
                  None
        :return: Hardcoded string
        '''
        return 'From privte method: you cannot see me'


cls_obj = SeeMee()
print("Call 'youcanseeme' method: {}".format(cls_obj.youcanseeme()))
# print("Call '__youcannotseeme()' method: {}".format(cls_obj.__youcannotseeme()))
# Will throw below exception
# AttributeError: 'SeeMee' object has no attribute '__youcannotseeme'
# solution for private method access
print("Fixed private method access: {}".format(cls_obj._SeeMee__youcannotseeme))
