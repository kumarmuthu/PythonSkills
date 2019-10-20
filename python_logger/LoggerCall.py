from LoggerLib import LoggerLib

__version__ = "2019.10.20.01"
__author__ = "Muthukumar Subramanian"

# You can refer this link also
# https://stackoverflow.com/questions/6386698/how-to-write-to-a-file-using-the-logging-python-module


# Calling **LoggerLib** function
file_name = 'muthu'
lib_obj = LoggerLib()
log_obj = lib_obj.Logger(file_name)
log_obj.info("I am from loggercall class".format())
log_obj.critical("CRIC".format())
log_obj.error("ERR".format())
log_obj.warning("WARN".format())
log_obj.debug("debug".format())
log_obj.info("qwerty".format())
log_obj.info("asdfghjkl".format())
log_obj.info("End".format())
# closing file
log_obj.handlers.clear()
