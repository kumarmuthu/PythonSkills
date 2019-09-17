import threading
import time
import pyotp
import time
import msvcrt
import sys

global exitFlag
global timeout
timeout = 60
exitFlag = False
global break_val
break_val = False
global collected_otp
collected_otp = None
global byte_arr
byte_arr = None

__version__ = "2019.09.17.01"
__author__ = 'Muthukumar Subramanian'

'''
Generating pyotp key and verifying here.

Note: It is works on PyCharm latest version(tested on: 2018.3.5).
It will not work on Linux. Because 'msvcrt' package does't support.
'''


class otp_verify_with_multithread(object):
    def __init__(self):
        pass

    '''
    generate an otp key
    Usage:
            Required argument(s):
                :param :obj otp object
            Optional argument(s):
                   None

    '''

    def generate(self, *args, **kwargs):
        '''
        ..codeauthor:: Muthukumar Subramanian
        '''
        totp_key = kwargs.get('obj')
        Current_otp = totp_key.now()
        print("Current OTP:", Current_otp)
        return True

    '''
    Displaying countdown time
        Usage:
            Required argument(s):
                :param :timeout required timeout value, it is depends on user
                :param :exitFlag exit timer countdown
            Optional argument(s):
                   None

    '''

    def countdown(self, *args, **kwargs):
        '''
        ..codeauthor:: Muthukumar Subramanian
        '''
        global timeout
        try:
            print('After {} seconds OTP will expired...'.format(timeout))
            global exitFlag
            if timeout:
                while timeout >= 0:
                    if exitFlag:
                        break
                    if timeout == 0:
                        print("timeout with '0' sec")
                        break
                    else:
                        if collected_otp is not None:
                            exitFlag = True
                        else:
                            if byte_arr is None:
                                # print(timeout, end='...\r')
                                print("You have: {} sec".format(timeout))
                                time.sleep(1)
                                timeout -= 1
                            else:
                                timeout = 0
                                break
        except ValueError as err:
            pass
        return True

    '''
    verifying generated otp here
    Usage:
            Required argument(s):
                :param :obj otp object
            Optional argument(s):
                   None

    '''

    def verify_otp(self, *args, **kwargs):
        '''
        ..codeauthor:: Muthukumar Subramanian
        '''
        totp_key = kwargs.get('obj')

        def readInput(caption, default, timeout=5):
            global byte_arr
            start_time = time.time()
            sys.stdout.write('%s %s' % (caption, default))
            sys.stdout.flush()
            input = ''
            while True:
                # detect keyboard key is currently press
                if msvcrt.kbhit():
                    # read char from keyboard after key press
                    byte_arr = msvcrt.getche()
                    if ord(byte_arr) == 13:  # enter_key
                        break
                    elif ord(byte_arr) >= 32:  # space_char
                        input += "".join(map(chr, byte_arr))
                if len(input) == 0 and (time.time() - start_time) > timeout:
                    print("timing out, using default value.")
                    break

            if len(input) > 0:
                return input
            else:
                return default

        time.sleep(1)
        global collected_otp
        collected_otp = readInput('', '', timeout=timeout)
        if collected_otp == '':
            collected_otp = None
        print('Entered OTP is: ** %s **' % collected_otp)
        if collected_otp is not None and collected_otp != '':
            # OTP verified
            c = totp_key.verify(collected_otp, valid_window=1)
            if c is True:
                print("OTP verification is pass")
                return True
            else:
                print("OTP verification is fail: **{}**".format(collected_otp))
                return False


if __name__ == '__main__':
    object_otp = otp_verify_with_multithread()
    totp = pyotp.TOTP('base32secret3232')
    dict_k = {'obj': totp}
    t1 = threading.Thread(target=object_otp.generate, args=('list'), kwargs=dict_k)
    t2 = threading.Thread(target=object_otp.countdown, kwargs=dict_k)
    t3 = threading.Thread(target=object_otp.verify_otp, kwargs=dict_k)
    # starting thread 1
    t1.start()
    # ending thread 1
    t1.join()
    # starting thread 2
    t2.start()
    # starting thread 3
    t3.start()
    # ending thread 2
    t2.join()
    # ending thread 3
    t3.join()
