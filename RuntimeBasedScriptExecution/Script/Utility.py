__version__ = "2023.01.28.01"
__author__ = "Muthukumar Subramanian"

"""
Utility - logger function, runtime converter, table_for_execution_total_time,
test_start_time, test_end_time and get_execution_total_runtime
"""

import re
import sys
import logging
from datetime import datetime
from prettytable import PrettyTable


class CustomException(Exception):
    """
    Custom Exception
    """
    pass


# Utility - logger
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


# Utility - runtime converter
def runtime_converter(log_obj, arg_obj, user_given_runtime):
    """
    ..codeauthor:: Muthukumar Subramanian
    :param log_obj: logger object
    :param arg_obj: argparse object
    :param user_given_runtime: user given runtime from argparse
    :return: int(any to seconds)
    """
    seconds = 0
    minutes = 0
    hours = 0
    days = 0
    test_timeout_value = 0
    # seconds mapping
    date_str_map = {
        'decades': 311040000,   # 60 * 60 * 24 * 30 * 12 * 10 - decades
        'years': 31104000,      # 60 * 60 * 24 * 30 * 12 - years
        'months': 2592000,      # 60 * 60 * 24 * 30 - months
        'd': 86400,             # 60 * 60 * 24 - days
        'h': 3600,              # 60 * 60 - hours
        'm': 60,                # 60 - minutes
        's': 1                  # 1 - seconds
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
        arg_obj.print_help()
        sys.exit(0)
    return test_timeout_value


def table_for_execution_total_time(t_time, get_log_obj, *args, **kwargs):
    """
    ..codeauthor:: Muthukumar Subramanian
     Usage:
        Required argument(s):
            :param t_time: executed total time
            :param get_log_obj: logging object
            :param kwargs: it's an additional support for log. need 'log_obj' key for logging
        Optional argument(s):
            :param args: default list
    :return: Boolean
    """
    log_obj = kwargs.get('log_obj_kwargs') if kwargs.get('log_obj_kwargs') else get_log_obj
    list_app = []
    try:
        pretty_table_for_end_time = PrettyTable()
        col = "Test's Total Execution Time"
        pretty_table_for_end_time.hrules = 1
        pretty_table_for_end_time.field_names = ['%64s' % col, '%16s' % t_time]
        list_app.append(['DEL', 'DEL'])
        if list_app:
            for j in list_app:
                pretty_table_for_end_time.add_row(j)
                pretty_table_for_end_time.del_row(0)
        log_obj.info('\n{}'.format(pretty_table_for_end_time))
    except Exception as err:
        log_obj.error('Observed error while print total runtime, Exception: {}'.format(err))
        return False
    return True


def test_start_time():
    starting_timestamp = datetime.now()
    return starting_timestamp


def test_end_time(start_time, log_obj=None, *args, **kwargs):
    """
    ..codeauthor:: Muthukumar Subramanian
    :param start_time: test start time
    :param log_obj: logging object
    :param args:
    :param kwargs: optional log object
    :return:total time
    """
    # Total execution time
    ending_timestamp = datetime.now()
    total_time, t1, t2 = get_execution_total_runtime(str(start_time), str(ending_timestamp))
    # table_for_execution_total_time(total_time, log_obj, *args, **kwargs)
    return total_time


def get_execution_total_runtime(time1, time2):
    """
     ..codeauthor:: Muthukumar Subramanian
     Usage:
            Required argument(s):
                :param time1: we can get start time
                :param time2: we can get end time
    :return: t, t1, t2
    """
    from datetime import datetime
    regex_date = re.match(r'(\d{4}-\d{2}-\d{2})\s+(\d{2}:\d{2}:\d{2})', time1)
    date_val = None
    date_val2 = None
    time_val = None
    time_val2 = None

    if regex_date is not None:
        date_val = regex_date.group(1).split('-')
        time_val = regex_date.group(2).split(':')
    regex_date_2 = re.match(r'(\d{4}-\d{2}-\d{2})\s+(\d{2}:\d{2}:\d{2})', time2)
    if regex_date_2 is not None:
        date_val2 = regex_date_2.group(1).split('-')
        time_val2 = regex_date_2.group(2).split(':')
    t1 = datetime(int(date_val[0]), int(date_val[1]), int(
        date_val[2]), int(time_val[0]), int(time_val[1]), int(time_val[2]))
    t2 = datetime(int(date_val2[0]), int(date_val2[1]), int(
        date_val2[2]), int(time_val2[0]), int(time_val2[1]), int(time_val2[2]))
    t = t2 - t1
    return t, t1, t2
