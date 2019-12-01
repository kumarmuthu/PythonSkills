import pyodbc

__version__ = "2019.10.01.01"
__author__ = "Muthukumar Subramanian"


def SqlObjCreate(func):
    def wrapped(class_obj, *args, **kwargs):
        '''
        ..codeauthor:: Muthukumar Subramanian
        Usage:
            Required argument(s):
                :param class_obj: We can use any variable here instead of 'class_obj',
                                executed class object will be present here.
                                Example: <__main__.SqlDecoratorSkipCheck object at 0x0000023BA70B7EF0>
                :param args: default list
                :param kwargs: default dict
                :return: SqlDecoratorSkipCheck.<called method|function>,
                         Example: <function SqlDecoratorSkipCheck.test at 0x0000023BA70B60D0>
            Optional argument(s):
                None
        '''
        if class_obj.cursor_obj is None:
            # we can do any operation here before actual execution
            print("From decorator function".format())
            print("Function name is: {}".format(func))
            print("Creating new object here!")
            # I just assigning value to 'cursor_obj' variable
            try:
                class_obj.sql_con_obj = pyodbc.connect(
                    'DRIVER={SQL Server};SERVER=localhost;DATABASE=user_verification;UID=sa;PWD=P@ssword;')
                class_obj.cursor_obj = class_obj.sql_con_obj.cursor()
                # self.log_obj.info("pyobdc object is created successfully...".format())
                print("pyobdc object is created successfully...".format())
            except Exception as err_pyodc:
                # self.log_obj.error("Observed exception: {}".format(err_pyodc))
                print("Observed exception: {}".format(err_pyodc))
                class_obj.cursor_obj = "HARDCODE value"  # we can remove this hardcode value
        else:
            print("cursor_obj is already created|updated: {}".format(class_obj.cursor_obj))
        return func(class_obj, *args, **kwargs)
    return wrapped


class OptionalDecoratorManage(object):
    def __init__(self, decorator):
        '''
        ..codeauthor:: Muthukumar Subramanian
        :param decorator: Actually def 'SqlObjCreate' will present here,
                        Example: @OptionalDecoratorManage(SqlObjCreate)
        '''
        self.deco = decorator

    def __call__(self, func):
        '''
        ..codeauthor:: Muthukumar Subramanian
        :param func: SqlDecoratorSkipCheck.test(.*|2|3|4)
        :return:
        '''
        # self.deco(func) --> SqlObjCreate(SqlDecoratorSkipCheck.test(|2|3|4)),
        # decorator function will execute, then normal def will call
        self.deco = self.deco(func)
        self.func = func  # SqlDecoratorSkipCheck.test, here normal def will call

        def wrapped(*args, **kwargs):
            if kwargs.get("skip_decorator") is True:
                return self.func(*args, **kwargs)  # test will present
            else:
                return self.deco(*args, **kwargs)  # SqlObjCreate will present
        return wrapped


class SqlDecoratorSkipCheck(object):
    '''
    ..codeauthor:: Muthukumar Subramanian
    Actual execution class
    '''

    def __init__(self, *args, **kwargs):
        self.fail = "FAIL"
        self.log_obj = None
        self.user_lib_obj = None
        if kwargs:
            self.user_lib_obj = kwargs.get('user_lib_obj')
            self.log_obj = kwargs.get('log_obj')
        self.cursor_obj = None
        print("SqlDecoratorSkipCheck class init")

    @OptionalDecoratorManage(SqlObjCreate)
    def test(self, *args, **kwargs):
        print("self dict: {}".format(self.__dict__))
        print("kwargs: {}".format(kwargs))

    @OptionalDecoratorManage(SqlObjCreate)
    def test_2(self, *args, **kwargs):
        print("self dict: {}".format(self.__dict__))
        print("kwargs: {}".format(kwargs))

    @OptionalDecoratorManage(SqlObjCreate)
    def test_3(self, *args, **kwargs):
        self.cursor_obj = None
        print("self dict: {}".format(self.__dict__))
        print("kwargs: {}".format(kwargs))

    @OptionalDecoratorManage(SqlObjCreate)
    def test_4(self, *args, **kwargs):
        print("self dict: {}".format(self.__dict__))
        print("kwargs: {}".format(kwargs))

    def test_5(self, *args, **kwargs):
        print("I am from class method".format(kwargs))

    @staticmethod
    def test_6(*args, **kwargs):
        print("I am from static method".format(kwargs))


if __name__ == '__main__':
    obj = SqlDecoratorSkipCheck()
    # without decorator skip
    obj.test()
    # call test_2 method
    obj.test_2()
    # reset cursor_obj
    obj.test_3()
    # enable cursor_obj
    obj.test_4()
    # decorator function skip
    ss = {'muthu': 123}
    obj.test(skip_decorator=True, **ss)
    obj.test_5()
    obj.test_6()
