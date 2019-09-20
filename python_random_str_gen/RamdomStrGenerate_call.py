from RamdomStrGenerate import RamdomStrGenerate

__version__ = "2019.09.17.01"
__author__ = 'Muthukumar Subramanian'

obj = RamdomStrGenerate()
ret = obj.random_str_gen(list_range=[10, 25], generate_type='list', list_count=5, option='all')
print("Return output from calling file: {}".format(ret))
