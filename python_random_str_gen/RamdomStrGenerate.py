import random
import string
import re

__version__ = "2019.09.17.01"
__author__ = 'Muthukumar Subramanian'


class RamdomStrGenerate(object):
    def __init__(self):
        pass

    '''
    Randomly generate number(s)/string(s)/special characters
    Usage:
        Required argument(s):
            None
        Optional argument(s):
            :param :option (Default value as None [will generate 1 to 5 range of str],
              we can use 'all' or 'int' or or ‘str’ or ‘str_with_lowercase’ or ‘str_with_uppercase’ or 'special_char')
            :param :list_range [user can use specific range value]
            :param :generate_type [user can generate either string or list and return the appropriate output]
            :param :list_count [<when you are parsing generate_type as ‘list’>
                                user can specify how many index you need from a list]
            :param :ignore_spl_char [<when you are parsing option as ‘special_char’>
                                            user can ignore specific(any) special characters]

    Example 1:
        list_1 =['1','10'] '1' is start range '10' is end range
    ret = RamdomStrGenerate.random_str_gen(list_1, option ='all')

    Return sample output:
                    P,i%xXSz?
    Example 2:
            Default value will generate (1 to 5 range of str)
        ret = RamdomStrGenerate.random_str_gen()
    Return sample output:
                    %lC
    Example 3:
            Default value will generate (1 to 5 range of str)
        obj_randm_str = RamdomStrGenerate()
        ret_output = obj_randm_str.random_str_gen(generate_type='list', list_count=5, option='special_char',
                                              ignore_spl_char='!@#$%^')
    Return sample output:
                        ['_:_', ':}]', '=;(', '*}.', '){.']
    Example 4:
            Default value will generate (1 to 5 range of str)
    obj_randm_str = RamdomStrGenerate()
    ret_output = obj_randm_str.random_str_gen(generate_type='list', list_count=3, option='all')
    Return sample output:
                ['aY$', 'oL]', 'HB+']
     Example 5:
            Default value will generate (10 to 25 range of str)
    obj_randm_str = RamdomStrGenerate()
    ret_output = obj_randm_str.random_str_gen(list_range=[10,25], generate_type='list', list_count=5, option='all')
    Return sample output:
    ['td*V2bzPiBK6!@YZI\\', 'fNahI\\;I:_DM9-zjUW', '=ZHFS6%K,!3UJ7AwE]', '23tT.:N/?{bJbz(2l4', 'T3d]n/d3AOEbjKWILP']
    Example 6:
            Default value will generate (10 to 25 range of str)
    obj_randm_str = RamdomStrGenerate()
    ret_output = obj_randm_str.random_str_gen(list_range=[5,100], generate_type='string', option='all')
    Return sample output:
            'fH/hY=V{Sjdf5anF$y3fbXCT0lxCoK;pKOSnRa*wz#3p3V^)Oc.@r}LuR[[F*qY]fQu'
    '''

    def random_str_gen(self, list_range=None, generate_type=None, list_count=2, option=None, ignore_spl_char=None):
        '''
        ..codeauthor:: Muthukumar Subramanian
        '''
        self.start_range = None
        self.end_range = None
        if isinstance(list_count, str):
            self.list_count = int(list_count)
        else:
            self.list_count = list_count
        random_str_output = None
        if isinstance(list_range, list) or isinstance(list_range, tuple):
            self.start_range = int(list_range[0])
            self.end_range = int(list_range[1])
        else:
            self.start_range = 1
            self.end_range = 6

        # randomly create a range based on the user input
        fixed_range = random.randrange(self.start_range, self.end_range, 2)
        print("start_range is: {} end_range is: {}".format(self.start_range, self.end_range, fixed_range))
        if generate_type == 'string':
            # Create random integer, string, special character based on the range
            if option == 'all' or option is None:
                random_str_output = ''.join([random.choice(string.ascii_letters + string.digits +
                                                           r'!@#$%^&*(){}_+-=:;,.?/\[]') for n in range(fixed_range)])
            elif option == 'str':
                random_str_output = ''.join([random.choice(string.ascii_letters) for n in range(fixed_range)])
            elif option == 'str_with_lowercase':
                random_str_output = ''.join([random.choice(string.ascii_lowercase) for n in range(fixed_range)])
            elif option == 'str_with_uppercase':
                random_str_output = ''.join([random.choice(string.ascii_uppercase) for n in range(fixed_range)])
            elif option == 'int':
                random_str_output = ''.join([random.choice(string.digits) for n in range(fixed_range)])
            elif option == 'special_char':
                if ignore_spl_char is not None:
                    default_special_char = r'!@#$%^&*(){}_+-=:;,.?/\[]'
                    regex_sub = re.sub(ignore_spl_char, '', default_special_char)
                    random_str_output = ''.join([random.choice(regex_sub) for n in range(fixed_range)])
                else:
                    random_str_output = ''.join([random.choice(r'!@#$%^&*(){}_+-=:;,.?/\[]')
                                                 for n in range(fixed_range)])
            return random_str_output
        elif generate_type == 'list':
            self.return_list = []
            # Create random integer, string, special character based on the range
            if option == 'all' or option is None:
                for i in range(self.list_count):
                    random_str_output = ''.join([random.choice(string.ascii_letters + string.digits +
                                                               r'!@#$%^&*(){}_+-=:;,.?/\[]') for n in
                                                 range(fixed_range)])
                    if random_str_output in self.return_list:
                        if random_str_output == self.return_list[-1]:
                            continue
                        else:
                            self.return_list.append(random_str_output)
                    else:
                        self.return_list.append(random_str_output)
            elif option == 'str':
                for i in range(self.list_count):
                    random_str_output = ''.join([random.choice(string.ascii_letters) for n in range(fixed_range)])
                    if random_str_output in self.return_list:
                        if random_str_output == self.return_list[-1]:
                            continue
                        else:
                            self.return_list.append(random_str_output)
                    else:
                        self.return_list.append(random_str_output)
            elif option == 'str_with_lowercase':
                for i in range(self.list_count):
                    random_str_output = ''.join([random.choice(string.ascii_lowercase) for n in range(fixed_range)])
                    if random_str_output in self.return_list:
                        if random_str_output == self.return_list[-1]:
                            continue
                        else:
                            self.return_list.append(random_str_output)
                    else:
                        self.return_list.append(random_str_output)
            elif option == 'str_with_uppercase':
                for i in range(self.list_count):
                    random_str_output = ''.join([random.choice(string.ascii_uppercase) for n in range(fixed_range)])
                    if random_str_output in self.return_list:
                        if random_str_output == self.return_list[-1]:
                            continue
                        else:
                            self.return_list.append(random_str_output)
                    else:
                        self.return_list.append(random_str_output)
            elif option == 'int':
                for i in range(self.list_count):
                    random_str_output = ''.join([random.choice(string.digits) for n in range(fixed_range)])
                    if random_str_output in self.return_list:
                        if random_str_output == self.return_list[-1]:
                            continue
                        else:
                            self.return_list.append(random_str_output)
                    else:
                        self.return_list.append(random_str_output)
            elif option == 'special_char':
                if ignore_spl_char is not None:
                    for i in range(self.list_count):
                        default_special_char = r'!@#$%^&*(){}_+-=:;,.?/\[]'
                        append_list = []
                        default_special_char = r'!@#$%^&*(){}_+-=:;,.?/\[]'
                        for j in ignore_spl_char:
                            append_list.append(r'\%s|' % (j))
                        ignore_spl_char = "".join(append_list)
                        regex_sub = None
                        try:
                            regex_sub = re.sub(r'%s' % (ignore_spl_char), '', default_special_char)
                        except Exception as err:
                            print("Observed exception is: {}".format(err))
                        if regex_sub == '':
                            error_msg = "ignore_spl_char variable is equal to special character!!!." \
                                "Please check your ignore_spl_char variable"
                            raise RamdomStrGenerate.CustomError(error_msg)
                        else:
                            random_str_output = ''.join([random.choice(regex_sub) for n in range(fixed_range)])
                            if random_str_output in self.return_list:
                                if random_str_output == self.return_list[-1]:
                                    continue
                                else:
                                    self.return_list.append(random_str_output)
                            else:
                                self.return_list.append(random_str_output)
                else:
                    for i in range(self.list_count):
                        random_str_output = ''.join(
                            [random.choice(r'!@#$%^&*(){}_+-=:;,.?/\[]') for n in range(fixed_range)])
                        if random_str_output in self.return_list:
                            if random_str_output == self.return_list[-1]:
                                continue
                            else:
                                self.return_list.append(random_str_output)
                        else:
                            self.return_list.append(random_str_output)
            return self.return_list

    '''
         Creating custom exception
    '''
    class CustomError(Exception):
        '''
        ..codeauthor:: Muthukumar Subramanian
        '''

        def __init__(self, value=None):
            self.value = value

        def __str__(self):
            return repr(self.value)


if __name__ == '__main__':
    '''
    Not mandatory below lines,below lines will work when you are executing this file.
    '''
    obj_randm_str = RamdomStrGenerate()
    ret_output = obj_randm_str.random_str_gen(list_range=[5, 100], generate_type='string', option='all')
    print("ret_output from RamdomStrGenerate class: {}".format(ret_output))
else:
    print("script execution from imported file")
