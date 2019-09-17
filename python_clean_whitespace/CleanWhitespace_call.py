from CleanWhitespace import CleanWhitespace

__version__ = "2019.09.17.01"
__author__ = 'Muthukumar Subramanian'

input_dict = {' E123      yuyu': ' QWEerer', ' Qwerty   22': ' 89RThhjj ',
              'DDf     ': {' MuthUkU      fdf ': 'asdfgFG2 '}}
obj = CleanWhitespace()
ret = obj.clean_whitespace(input_dict, key_strip='lower_case', value_strip='lead_and_trail')
print("Return output from calling file: {}".format(ret))
