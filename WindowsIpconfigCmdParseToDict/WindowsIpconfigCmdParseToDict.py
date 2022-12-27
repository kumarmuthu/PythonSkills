__version__ = "2022.12.27.01"
__author__ = "Muthukumar Subramanian"
'''
Test Windows 'ipconfig' command will be parsed into a dictionary
'''

import subprocess
import re
import sys
import argparse

# Argparse
arg_obj = argparse.ArgumentParser("ipconfig test")
arg_obj.add_argument('--run-hardcoded-output', type=str, choices=['true', 'false'],
                     dest='run_hardcoded_output', required=False, default='true',
                     help='Default as true, Run only test hardcoded output if argument as "true", '
                          'Run the actual cmd on system if argument as "false"')
get_parse = arg_obj.parse_args()
hardcoded_output = get_parse.run_hardcoded_output
print("Hardcoded_output(Args Value): ", hardcoded_output)

return_output = None
parsed_output = None
cmd = None

# Check system type
if sys.platform == 'win32':
    cmd = 'ipconfig'
elif sys.platform == 'linux':
    cmd = 'ifconfig'

# hardcoded output from ipconfig cmd
return_output = '''
Windows IP Configuration


Ethernet adapter Ethernet:

   Media State . . . . . . . . . . . : Media disconnected
   Connection-specific DNS Suffix  . :

Wireless LAN adapter Local Area Connection* 11:

   Media State . . . . . . . . . . . : Media disconnected
   Connection-specific DNS Suffix  . :

Wireless LAN adapter Local Area Connection* 12:

   Media State . . . . . . . . . . . : Media disconnected
   Connection-specific DNS Suffix  . :

Wireless LAN adapter Wi-Fi 2:

   Connection-specific DNS Suffix  . :
   IPv6 Address. . . . . . . . . . . : 2401:4900:1f20:70bc:4d0c:6832:6903:327f
   Temporary IPv6 Address. . . . . . : 2401:4900:1f20:70bc:4dda:2b74:18c5:314
   Link-local IPv6 Address . . . . . : fe80::8723:bbb0:1be:2c6c%8
   IPv4 Address. . . . . . . . . . . : 192.168.1.5
   Subnet Mask . . . . . . . . . . . : 255.255.255.0
   Default Gateway . . . . . . . . . : fe80::1%8
                                       192.168.1.1

'''

if hardcoded_output == 'false':
    print("Executing the test with actual cmd on system")
    try:
        return_output = subprocess.check_output(['cmd.exe', "/c", cmd], stderr=subprocess.PIPE)
    except subprocess.CalledProcessError as err:
        print(f'Error code: {err.returncode}, cmd: {err.cmd}, Output: {err.output}')
    else:
        parsed_output = return_output.decode("utf-8").replace('\r', '').split('\n')
        parsed_output = [k for k in parsed_output if k != '']
        print("Parsed_output: ", parsed_output)
else:
    print("Executing the test with hardcoded output")
    parsed_output = return_output.split('\n')
    parsed_output = [k for k in parsed_output if k != '']
    print("Parsed_output: ", parsed_output)

final_dict = {}
final_dict_ret = {}
primary_key = None
temp_dict = {}
header_key = None

for ind, i in enumerate(parsed_output):
    s1 = re.search(r'^(?!\s+)([a-zA-Z\-\s0-9\\*]+)(?:[\s\\.]+)?:$', i, flags=re.I)
    s2 = re.search(r'^\s+([a-zA-Z\-\s0-9\\*]+)(?:[\s\\.]+)?:(.*)?$', i, flags=re.I)
    s3 = re.search(r'^(\s+[0-9\\.]+)$', i, flags=re.I)
    s4 = re.search(r'^(?!\s+)([\d\w\s]+)$', i, flags=re.I)
    if s1:
        primary_key = s1.group(1).strip()
        temp_dict = {}
    if s2 and s1 is None:
        if s2.group(1) is not None:
            temp_dict.update({s2.group(1).strip(): (lambda x: None if x == '' else x)(s2.group(2).strip())})
        else:
            temp_dict.update({s2.group(1).strip(): None})
    if primary_key:
        final_dict.update({primary_key: temp_dict})
    if s3:
        # print("Previous line: ", parsed_op[ind - 1])
        s5 = re.search(r'^(?:\s+)?([a-zA-Z\-\s0-9\\*]+)(?:[\s\\.]+)?:(.*)?$', parsed_output[ind - 1], flags=re.I)
        for key, val in final_dict.items():
            for key_2, val_2 in val.items():
                if s5.group(2).strip() == val_2:
                    temp_list = []
                    temp_list.append(val_2)
                    temp_list.append(s3.group(1).strip())
                    final_dict[key][key_2] = temp_list
    if s4:
        header_key = s4.group(1)
if header_key:
    final_dict_ret[header_key] = final_dict
print("Final_dict: ", final_dict_ret)
