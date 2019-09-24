# Example for import two classes

__version__ = "2019.09.24.01"
__author__ = 'Muthukumar Subramanian'


class muthu():
    def __init__(self):
        print("self: ", self)

    def connect(self):
        self.sess = '100'
        print("connected device")
        return True, self.sess

    def send(self):
        print("sending the cmd #####")
        return True

    def disconnect(self):
        print("disconnecting the device #####")
        return True


cls_obj = muthu()
if __name__ == '__main__':
    # execute all the def if run this file (class_1.py)
    try:
        count = 0
        while True:
            count = count + 1
            # creating session
            ret_code, session_obj = cls_obj.connect()
            if ret_code is True:
                cls_obj.send()
                cls_obj.disconnect()
                break
            else:
                # Break the loop when it is reached maximum login(3)
                if count >= 3:
                    print("device reached maximum login(3), so exiting")
                    break
    except Exception as err:
        print("Observed exception while creating session: {}".format(err))
else:
    # script execution from imported file (class_2.py)
    try:
        count = 0
        while True:
            count = count + 1
            # creating session
            ret_code, session_obj = cls_obj.connect()
            print("### Executing ELSE block ###")
            if ret_code is True:
                break
            else:
                # Break the loop when it is reached maximum login(3)
                if count >= 3:
                    print("device reached maximum login(3), so exiting")
                    break
    except Exception as err:
        print("Observed exception while creating session: {}".format(err))
