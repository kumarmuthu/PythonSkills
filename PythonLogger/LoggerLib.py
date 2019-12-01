import sys
import logging
import logging.config

__version__ = "2019.10.20.01"
__author__ = "Muthukumar Subramanian"

# You can refer this link also
# https://stackoverflow.com/questions/6386698/how-to-write-to-a-file-using-the-logging-python-module


class LoggerLib(object):
    def __init__(self):
        pass

    def Logger(self, file_name):
        '''
        ..codeauthor:: Muthukumar Subramanian
        Usage:
            Required argument(s):
                :param file_name: File handler name is required
            Optional argument(s):
                None
        :return:
        '''
        formatter = logging.Formatter(fmt='%(asctime)s %(module)s,line: %(lineno)d %(levelname)8s | %(message)s',
                                      datefmt='%Y/%m/%d %H:%M:%S')  # %I:%M:%S %p AM|PM format
        # we can use .txt or .log file extension
        logging.basicConfig(filename='%s.txt' % (file_name),
                            format='%(asctime)s %(module)s,line: %(lineno)d %(levelname)8s | %(message)s',
                            datefmt='%Y/%m/%d %H:%M:%S', filemode='w', level=logging.DEBUG)
        log_obj = logging.getLogger()
        log_obj.setLevel(logging.DEBUG)
        # log_obj = logging.getLogger().addHandler(logging.StreamHandler())

        # console printer
        screen_handler = logging.StreamHandler(stream=sys.stdout)  # stream=sys.stdout is similar to normal print
        screen_handler.setFormatter(formatter)
        logging.getLogger().addHandler(screen_handler)

        log_obj.info("Logger object is created successfully..")
        return log_obj
