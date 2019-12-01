import pyodbc

__version__ = "2019.09.30.01"
__author__ = "Muthukumar Subramanian"


class SqlDecoratorCheck(object):
    class SqlConnectionDecorator(object):
        def SqlObjCreate(func):
            # print("wrapper before") # debug purpose
            def wrapped(self, *args, **kwargs):
                self.sql_con_obj = None
                try:
                    self.sql_con_obj = pyodbc.connect(
                        'DRIVER={SQL Server};SERVER=localhost;DATABASE=user_verification;UID=sa;PWD=P@ssword;')
                    self.cursor_obj = self.sql_con_obj.cursor()
                    # self.log_obj.info("pyobdc object is created successfully...".format())
                    print("pyobdc object is created successfully...".format())
                except Exception as err_pyodc:
                    # self.log_obj.error("Observed exception: {}".format(err_pyodc))
                    print("Observed exception: {}".format(err_pyodc))
                    self.cursor_obj = "HARDCODE value"
                return func(self, *args, **kwargs)
            return wrapped

    def __init__(self, *args, **kwargs):
        self.fail = "FAIL"
        self.log_obj = None
        self.user_lib_obj = None
        if kwargs:
            self.user_lib_obj = kwargs.get('user_lib_obj')
            self.log_obj = kwargs.get('log_obj')
        self.cursor_obj = None

    @SqlConnectionDecorator.SqlObjCreate
    def muthu(self, *args, **kwargs):
        '''
        ..codeauthor:: Muthukumar Subramanian
        Usage:
            Required argument(s):
                None
            Optional argument(s):
                None
        :return: Boolean
        '''
        self.log_obj = "overwrite in method muthu"
        print("hi i am from muthu method {}".format(self.cursor_obj))
        return True

    @SqlConnectionDecorator.SqlObjCreate
    def Create_new_table(self, *args, **kwargs):
        '''
        ..codeauthor:: Muthukumar Subramanian
        Create new table for new user admin/user, as now it is disabled
        Usage:
            Required argument(s):
                :param kwargs: default dict, required 'login_type' either admin or user
                                required 'create_table_name' user passed name is created table name on database
            Optional argument(s):
                :param args: default list
        :return: Boolean
        '''
        print("self dict: {}".format(self.__dict__))
        print("cursor_obj: {}".format(self.cursor_obj))
        print("log_obj: {}".format(self.log_obj))
        return True


if __name__ == '__main__':
    obj = SqlDecoratorCheck()
    obj.muthu()
    obj.Create_new_table()
