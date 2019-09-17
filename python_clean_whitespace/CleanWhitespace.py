import re
from collections import OrderedDict


__version__ = "2019.09.17.01"
__author__ = 'Muthukumar Subramanian'


class CleanWhitespace(object):
    def __init__(input_dictionary):
        pass

    '''
        This function will clean whitespace's or convert lower/upper case from the dictionary keys/values
        Usage:
            Required argument(s):
                    None
            Optional argument(s):
                   :param :key_strip - (Default value as None [It will return the same value],
                        we can use below options:
                        key_strip = 'all' [removing much spaces, leading spaces and trailing spaces ]
                        key_strip = 'all_with_lower_case' [removing much spaces, leading spaces,
                        trailing spaces and converting lower case ]
                        key_strip = 'all_with_upper_case' [removing much spaces, leading spaces,
                        trailing spaces and converting upper case ]
                        key_strip = 'lead_and_trail' [removing leading and trailing spaces ]
                        key_strip = 'much_spaces' [removing much spaces]
                        key_strip = 'lower_case' [converting lower case]
                        key_strip = 'upper_case' [converting upper case] )
                   :param :value_strip - (Default value as None [It will return the same value],
                        we can use below options:
                        value_strip = 'all' [removing much spaces, leading spaces and trailing spaces ]
                        value_strip = 'all_with_lower_case' [removing much spaces, leading spaces,
                        trailing spaces and converting lower case ]
                        value_strip = 'all_with_upper_case' [removing much spaces, leading spaces,
                        trailing spaces and converting upper case ]
                        value_strip = 'lead_and_trail' [removing leading and trailing spaces ]
                        value_strip = 'much_spaces' [removing much spaces]
                        value_strip = 'lower_case' [converting lower case]
                        value_strip = 'upper_case' [converting upper case] )
            Example 1:
                Dict input:
                    abc = {' E123      yuyu' : ' QWEerer' , ' Qwerty   22' : ' 89RThhjj ',
                     'DDf     ' : { ' MuthUkU      fdf ' : 'asdfgFG2 '}}
                ret = clean_whitespace(abc, key_strip = 'lead_and_trail', value_strip='all')
                Return output:
                    ret =  {'E123      yuyu': 'qweerer', 'Qwerty   22': '89rthhjj',
                            'DDf': {'MuthUkU      fdf': 'asdfgfg2'}}
             Example 2: (dict values spaces remove)
                Dict input:
                    abc = {' E123      yuyu' : ' QWEerer' , ' Qwerty   22' : ' 89RThhjj ',
                         'DDf     ' : { ' MuthUkU      fdf ' : 'asdfgFG2 '}}
                ret = clean_whitespace(abc, value_strip='lead_and_trail')
                Return output:
                    ret = {   ' E123      yuyu': 'QWEerer',
                        ' Qwerty   22': '89RThhjj',
                        'DDf     ': {' MuthUkU      fdf ': 'asdfgFG2'}}
             Example 3:
                Dict input:
                    abc = {1: 2, 3: [4, {5: 6}, 7]}
                ret = clean_whitespace(abc, key_strip = 'lead_and_trail', value_strip='all')
                Return output:
                    ret = {1: 2, 3: [4, {5: 6}, 7]}
              Example 4:
                Dict input:
                    abc = {1:2, 3:[4,{'5  ':6},7]}
                ret = clean_whitespace(abc, key_strip = 'lead_and_trail', value_strip='all')
                Return output:
                    {1: 2, 3: [4, {'5': 6}, 7]}
        '''

    def clean_whitespace(self, input_dictionary, key_strip=None, value_strip=None):
        '''
        ..codeauthor:: Muthukumar Subramanian
        '''
        if isinstance(input_dictionary, str):
            return self.whitespaces_remove_and_lowercase_convert(input_dictionary,
                                                                 value_strip=value_strip)
        elif isinstance(input_dictionary, list):
            return [
                self.clean_whitespace(o, key_strip=key_strip, value_strip=value_strip)
                for o in input_dictionary]
        elif isinstance(input_dictionary, tuple):
            return tuple(
                self.clean_whitespace(o, key_strip=key_strip, value_strip=value_strip)
                for o in input_dictionary)
        elif isinstance(input_dictionary, OrderedDict):
            return OrderedDict((self.whitespaces_remove_and_lowercase_convert_for_key(k, key_strip=key_strip),
                                self.clean_whitespace(v, key_strip=key_strip,
                                                      value_strip=value_strip)) for (k, v) in
                               input_dictionary.items())
        elif isinstance(input_dictionary, dict):
            return dict((self.whitespaces_remove_and_lowercase_convert_for_key(k, key_strip=key_strip),
                         self.clean_whitespace(v, key_strip=key_strip,
                                               value_strip=value_strip)) for (k, v) in
                        input_dictionary.items())
        else:
            return input_dictionary

    '''
            Part of clean_whitespace function
    '''

    @staticmethod
    def whitespaces_remove_and_lowercase_convert_for_key(get_input, key_strip=None):
        '''
        ..codeauthor:: Muthukumar Subramanian
          Removing leading and trailing spaces or much_spaces or lower case or
          upper case from the dictionary of each key(dict key)
        '''
        if isinstance(get_input, str):
            if key_strip == 'all':
                get_input = re.sub(r'^\s+|\s+$', '', get_input)
                get_input = re.sub(r'\s+', ' ', get_input)
            elif key_strip == 'all_with_lower_case':
                get_input = re.sub(r'^\s+|\s+$', '', get_input)
                get_input = re.sub(r'\s+', ' ', get_input)
                get_input = get_input.lower()
            elif key_strip == 'all_with_upper_case':
                get_input = re.sub(r'^\s+|\s+$', '', get_input)
                get_input = re.sub(r'\s+', ' ', get_input)
                get_input = get_input.upper()
            elif key_strip == 'lead_and_trail':
                get_input = re.sub(r'^\s+|\s+$', '', get_input)
            elif key_strip == 'much_spaces':
                get_input = re.sub(r'\s+', ' ', get_input)
            elif key_strip == 'lower_case':
                get_input = get_input.lower()
            elif key_strip == 'upper_case':
                get_input = get_input.upper()
            elif key_strip is None:
                get_input = get_input
            return get_input
        elif isinstance(get_input, int):
            return get_input

    '''
        Part of clean_whitespace function
    '''

    @staticmethod
    def whitespaces_remove_and_lowercase_convert(get_input, value_strip=None):
        '''
        ..codeauthor:: Muthukumar Subramanian
          Removing leading and trailing spaces or much_spaces or lower case or
          upper case from the dictionary of each value(dict value)
        '''

        if isinstance(get_input, str):
            if value_strip == 'all':
                get_input = re.sub(r'^\s+|\s+$', '', get_input)
                get_input = re.sub(r'\s+', ' ', get_input)
            elif value_strip == 'all_with_lower_case':
                get_input = re.sub(r'^\s+|\s+$', '', get_input)
                get_input = re.sub(r'\s+', ' ', get_input)
                get_input = get_input.lower()
            elif value_strip == 'all_with_upper_case':
                get_input = re.sub(r'^\s+|\s+$', '', get_input)
                get_input = re.sub(r'\s+', ' ', get_input)
                get_input = get_input.upper()
            elif value_strip == 'lead_and_trail':
                get_input = re.sub(r'^\s+|\s+$', '', get_input)
            elif value_strip == 'much_spaces':
                get_input = re.sub(r'\s+', ' ', get_input)
            elif value_strip == 'lower_case':
                get_input = get_input.lower()
            elif value_strip == 'upper_case':
                get_input = get_input.upper()
            else:
                get_input = get_input
            return get_input
        elif isinstance(get_input, int):
            return get_input


if __name__ == '__main__':
    '''
    Not mandatory below lines,below lines will work when you are executing this file.
    '''
    obj_wspace = CleanWhitespace()
    dict_1 = {' E123      yuyu': ' QWEerer', ' Qwerty   22': ' 89RThhjj ',
              'DDf     ': {' MuthUkU      fdf ': 'asdfgFG2 '}}
    ret_output = obj_wspace.clean_whitespace(dict_1, key_strip='much_spaces', value_strip='upper_case')
    print("ret_output from CleanWhitespace class: {}".format(ret_output))
else:
    print("script execution from imported file")
