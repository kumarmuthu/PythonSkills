__version__ = "2019.10.29.01"
__author__ = "Muthukumar Subramanian"

# import abc   # for Python lessthan 3.4
from abc import ABC, abstractmethod
# class MyOwnAbstractClass(metaclass=abc.ABCMeta):


class MyOwnAbstractClass(ABC):
    # @abc.abstractmethod
    @abstractmethod
    def template_common_method(self):
        '''
        i) This is the Abstract class for common framework/base-program of our project.
        ii) Exception will throw if your are not given this Abstract method(user defined name)'template_common_method'
        in subclass of "ExecuteScript.
        ..codeauthor:: Muthukumar Subramanian
        Usage:
            Required argument(s):
                None
            Optional argument(s):
                None
        :return: boolean and ref
        '''
        # you can define a common Application Program Interface(API)
        # for a set of subclasses.
        print("1 - I am from Abstract class of method 'template_common_method'")
        return True, "Start"

    @abstractmethod
    def template_common_method_2(self):
        '''
        i) This is the Abstract class for common framework/base-program of our project.
        ii) Exception will throw if your are not given this Abstract method(user defined name)'template_common_method_2'
        in subclass of "ExecuteScript.
        ..codeauthor:: Muthukumar Subramanian
        Usage:
            Required argument(s):
                None
            Optional argument(s):
                None
        :return: boolean and ref
        '''
        # you can define a common Application Program Interface(API)
        # for a set of subclasses.
        print("2 - I am from Abstract class of method 'template_common_method_2'")
        return True, "End"


class ExecuteScript(MyOwnAbstractClass):
    def __init__(self, x, y):
        self.fname = x
        self.lname = y

    def template_common_method(self):
        '''
        i) subclass method for end user.
        ..codeauthor:: Muthukumar Subramanian
        Usage:
            Required argument(s):
                None
            Optional argument(s):
                None
        :return: func return data
        '''
        # If you want to access our main framework of code
        # just call  super().<method>. It is optional
        r, rt = super().template_common_method()
        if r is True:
            print("Base_class_return: {}, {}".format(r, rt))
        print("I am from ExecuteScript class")
        return self.fname + '_' + self.lname

    def muthu(self):
        '''
        subclass non-abstract method for end user, this is a normal method.
        ..codeauthor:: Muthukumar Subramanian
        Usage:
            Required argument(s):
                None
            Optional argument(s):
                None
        :return: boolean
        '''
        print("Hello welcome!!!")
        return True


cls_obj = ExecuteScript("Muthu", "Kumar")
ret = cls_obj.template_common_method()
print('RET: {}'.format(ret))
ret_2 = cls_obj.muthu()
print('RET_2: {}'.format(ret_2))
