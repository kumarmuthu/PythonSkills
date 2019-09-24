# Example for import two classes

__version__ = "2019.09.24.01"
__author__ = 'Muthukumar Subramanian'

from class_1 import *


class muthu_2():
    def __init__(self):
        print("self: ", self)

    def vlan_config(self, session):
        cli = 'cofig -p 1/10'
        print("session id: {} config vlan: {}".format(session, cli))
        return True, cli


cls_obj_2 = muthu_2()
if __name__ == '__main__':
    # execute all the def if run this file (lass_1.py)
    try:
        if session_obj:
            ret, ret_output = cls_obj_2.vlan_config(session_obj)
    except Exception as err:
        print("Observed exception while executing vlan_config function: {}".format(err))
    # disconnect the device
    if ret_code is True:
        cls_obj.disconnect()
else:
    # script execution from imported file (class_2.py)
    print("nothing print")
