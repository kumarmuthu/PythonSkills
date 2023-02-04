__version__ = "2023.02.24.01"
__author__ = "Muthukumar Subramanian"

"""
Utility, Calculate and Update all total runtime from child test, base test and main test.
All None value will be updated.
"""
import copy
import logging
import re
import sys
from functools import reduce


class CustomException(Exception):
    """
    Custom Exception
    """
    pass


def logger_function(file_name=None):
    """
    ..codeauthor:: Muthukumar Subramanian
    :return: logging object
     """
    formatter = logging.Formatter(fmt='%(asctime)s %(threadName)s %(module)s, %(funcName)s,'
                                      'line: %(lineno)d %(levelname)8s'
                                      ' | %(message)s', datefmt='%Y/%m/%d %H:%M:%S')
    if file_name is None:
        s1 = re.search(r'(.*).py', __file__)
        file_name = s1.group(1)
    else:
        s1 = re.search(r'(.*).py', str(file_name))
        file_name = s1.group(1)
    logging.basicConfig(filename='%s.log' % file_name,
                        format='%(asctime)s %(threadName)s %(module)s, %(funcName)s,'
                               'line: %(lineno)d %(levelname)8s | %(message)s',
                        datefmt='%Y/%m/%d %H:%M:%S', filemode='w', level=logging.INFO)
    # File handler will create a file
    log_obj = logging.getLogger(file_name)
    file_name_with_extension = '%s.log' % file_name
    file_handler = logging.FileHandler(file_name_with_extension, mode='w')
    file_handler.setFormatter(formatter)
    logging.getLogger(file_name).addHandler(file_handler)

    # File handler written data will display on the console window
    screen_handler = logging.StreamHandler(stream=sys.stdout)
    screen_handler.setFormatter(formatter)
    logging.getLogger(file_name).addHandler(screen_handler)

    log_obj.info("Logger object is initiated...")
    return log_obj


def runtime_converter(log_obj, user_given_runtime, arg_obj=None):
    """
    ..codeauthor:: Muthukumar Subramanian
    :param log_obj: logger object
    :param user_given_runtime: user given runtime from argparse
    :param arg_obj: argparse object
    :return: int(any to seconds)
    """
    seconds = 0
    minutes = 0
    hours = 0
    days = 0
    test_timeout_value = 0
    # seconds mapping
    date_str_map = {
        'decades': 311040000,  # 60 * 60 * 24 * 30 * 12 * 10 - decades
        'years': 31104000,  # 60 * 60 * 24 * 30 * 12 - years
        'months': 2592000,  # 60 * 60 * 24 * 30 - months
        'd': 86400,  # 60 * 60 * 24 - days
        'h': 3600,  # 60 * 60 - hours
        'm': 60,  # 60 - minutes
        's': 1  # 1 - seconds
    }

    s1 = re.search(r'^(\d+)(\w)$', user_given_runtime, flags=re.I)
    if s1 is not None:
        if s1.group(2) == 's':
            seconds = date_str_map['s'] * int(s1.group(1))
            test_timeout_value = seconds
        elif s1.group(2) == 'm':
            minutes = date_str_map['m'] * int(s1.group(1))
            test_timeout_value = minutes
        elif s1.group(2) == 'h':
            hours = date_str_map['h'] * int(s1.group(1))
            test_timeout_value = hours
        elif s1.group(2) == 'd':
            days = date_str_map['d'] * int(s1.group(1))
            test_timeout_value = days
        log_obj.info("Days:Hours:Minutes:Seconds-> %d:%d:%d:%d" % (days, hours, minutes, seconds))
    else:
        if arg_obj is not None:
            arg_obj.print_help()
            sys.exit(0)
        else:
            raise CustomException("Given runtime format is invalid!, Example: '1s, 1m, 1h, 1d'")
    return test_timeout_value


# create logging object
get_log_obj = logger_function(__file__)
get_log_obj.info("{:*^30}".format('TEST START'))

original_input_dict = {
    'main_test': {
        'main_test_total_run_time': None,
        'base_test': {
            'base_test_total_run_time': None,
            'base_test1': {
                'child_test_total_run_time': None,
                'child_test1': {
                    'child_test_run_time': '5m'
                },
                'child_test2': {
                    'child_test_run_time': '10m'
                },
                'child_test3': {
                    'child_test_run_time': '20m'
                }
            },
            'base_test2': {
                'child_test_total_run_time': None,
                'child_test1': {
                    'child_test_run_time': '2m'
                },
                'child_test2': {
                    'child_test_run_time': '4m'
                },
                'child_test4': {
                    'child_test_run_time': '8m'
                },
            }
        }
    }
}
# OR this format
"""original_input_dict = {
    'main_test': {
        'base_test': {
            'base_test1': {
                'child_test1': {
                    'child_test_run_time': '5m'
                },
                'child_test2': {
                    'child_test_run_time': '10m'
                },
                'child_test3': {
                    'child_test_run_time': '20m'
                },
                'child_test_total_run_time': None
            },
            'base_test2': {
                'child_test1': {
                    'child_test_run_time': '2m'
                },
                'child_test2': {
                    'child_test_run_time': '4m'
                },
                'child_test4': {
                    'child_test_run_time': '8m'
                },
                'child_test_total_run_time': None
            },
            'base_test_total_run_time': None,
        },
        'main_test_total_run_time': '1h',
    }
}"""

# Original dict is copied
final_dict = copy.deepcopy(original_input_dict)

base_total_time = 0
child_total_time = 0
main_total_time = 0

for key, value in original_input_dict.items():
    if isinstance(value, dict):
        for key_1, value_1 in value.items():
            if isinstance(value_1, dict):
                # Calculate child test runtime
                for key_2, value_2 in value_1.items():
                    if isinstance(value_2, dict):
                        child_time_list = []
                        for key_3, value_3 in value_2.items():
                            if isinstance(value_3, dict):
                                child_time_list.extend(list(value_3.values()))
                        if child_time_list:
                            list_temp = []
                            for i in child_time_list:
                                child_test_runtime_str_format = runtime_converter(get_log_obj, i)
                                list_temp.append(child_test_runtime_str_format)
                            child_total_time = reduce(lambda m, n: m + n, list_temp)
                            final_dict[key][key_1][key_2]["child_test_total_run_time"] = child_total_time  # OR
                            # update 'child_test_total_run_time' key in the same dict
                            for key_4, value_4 in value_2.items():
                                if key_4 == "child_test_total_run_time":
                                    original_input_dict[key][key_1][key_2].update({key_4: child_total_time})
                # Calculate base test runtime
                base_time_list = []
                for base_test_key_1, base_test_value_1 in value_1.items():
                    if isinstance(base_test_value_1, dict):
                        for base_test_key_2, base_test_value_2 in base_test_value_1.items():
                            if isinstance(base_test_value_2, int):
                                base_time_list.append(base_test_value_2)
                if base_time_list:
                    base_total_time = reduce(lambda m, n: m + n, base_time_list)
                    final_dict[key][key_1]["base_test_total_run_time"] = base_total_time  # OR
                    # update 'base_test_total_run_time' key in the same dict
                    for base_test_key_3, base_test_value_3 in value_1.items():
                        if base_test_key_3 == "base_test_total_run_time":
                            original_input_dict[key][key_1].update({base_test_key_3: base_total_time})
# Calculate main test runtime
for main_test_key, main_test_value in original_input_dict.items():
    for main_test_key_1, main_test_value_2 in main_test_value.items():
        if not isinstance(main_test_value_2, dict):
            if main_test_value_2 is None:
                main_test_total_time = base_total_time + 5
            else:
                main_test_total_time = runtime_converter(get_log_obj, main_test_value_2)
                if base_total_time > main_test_total_time:
                    raise Exception(f"Currently, the Main test total runtime is less than Base test runtime!, "
                                    f"But Main test runtime is always greater than Base test runtime. \n"
                                    f"Main test runtime: {main_test_total_time} sec, "
                                    f"Base test runtime: {base_total_time} sec")
            final_dict[main_test_key][main_test_key_1] = main_test_total_time  # OR
            # update 'main_test_total_run_time' key in the same dict
            original_input_dict[main_test_key].update({main_test_key_1: main_test_total_time})

get_log_obj.info(f"Original dict after update: {original_input_dict}")
get_log_obj.info("{:*^30}".format('*'))
get_log_obj.info(f"Final dict after update: {final_dict}")  # OR
get_log_obj.info("{:*^30}".format('TEST END'))
