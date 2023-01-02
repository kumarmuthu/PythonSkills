__version__ = "2023.01.02.01"
__author__ = "Muthukumar Subramanian"
'''
Test Windows 'systeminfo' command will be parsed into a dictionary
'''

import subprocess
import re
import sys
import argparse

# Argparse
arg_obj = argparse.ArgumentParser("systeminfo test")
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
    cmd = 'systeminfo'
elif sys.platform == 'linux':
    # TODO
    # cmd = 'lscpu'
    pass

# Hardcoded output from systeminfo cmd
return_output = '''
Host Name:                 DESKTOP-NQDJHVJ
OS Name:                   Microsoft Windows 10 Pro
OS Version:                10.0.19045 N/A Build 19045
OS Manufacturer:           Microsoft Corporation
OS Configuration:          Standalone Workstation
OS Build Type:             Multiprocessor Free
Registered Owner:          ADMIN
Registered Organization:
Product ID:                00331-10000-00001-AA058
Original Install Date:     24-09-2022, 10:29:30
System Boot Time:          25-12-2022, 17:20:59
System Manufacturer:       HP
System Model:              HP Pavilion Notebook
System Type:               x64-based PC
Processor(s):              1 Processor(s) Installed.
                           [01]: Intel64 Family 6 Model 61 Stepping 4 GenuineIntel ~2200 Mhz
BIOS Version:              Insyde F.41, 30-07-2015
Windows Directory:         C:\WINDOWS
System Directory:          C:\WINDOWS\system32
Boot Device:               \Device\HarddiskVolume6
System Locale:             en-us;English (United States)
Input Locale:              00004009
Time Zone:                 (UTC+05:30) Chennai, Kolkata, Mumbai, New Delhi
Total Physical Memory:     8,114 MB
Available Physical Memory: 2,378 MB
Virtual Memory: Max Size:  12,466 MB
Virtual Memory: Available: 5,665 MB
Virtual Memory: In Use:    6,801 MB
Page File Location(s):     C:\pagefile.sys
Domain:                    WORKGROUP
Logon Server:              \\DESKTOP-NQDJHVJ
Hotfix(s):                 10 Hotfix(s) Installed.
                           [01]: KB5020872
                           [02]: KB4562830
                           [03]: KB5003791
                           [04]: KB5007401
                           [05]: KB5012170
                           [06]: KB5015684
                           [07]: KB5021233
                           [08]: KB5016705
                           [09]: KB5018506
                           [10]: KB5020372
Network Card(s):           2 NIC(s) Installed.
                           [01]: Realtek PCIe FE Family Controller
                                 Connection Name: Ethernet
                                 Status:          Media disconnected
                           [02]: Realtek RTL8723DE 802.11b/g/n PCIe Adapter
                                 Connection Name: Wi-Fi 2
                                 DHCP Enabled:    Yes
                                 DHCP Server:     192.168.1.1
                                 IP address(es)
                                 [01]: 192.168.1.4
                                 [02]: fe80::8723:bbb0:1be:2c6c
                                 [03]: 2401:4900:1f20:a97:8d08:2985:cea3:ee7e
                                 [04]: 2401:4900:1f20:a97:9e06:ed83:77d7:1061
Hyper-V Requirements:      VM Monitor Mode Extensions: Yes
                           Virtualization Enabled In Firmware: Yes
                           Second Level Address Translation: Yes
                           Data Execution Prevention Available: Yes
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
primary_key = ''
primary_ip_key = ''
hyper_key = ''
nw_card_key = ''
hotfix_key = ''
processor_key = ''
virtual_key = ''
list_for_nw_primary_key_update = []

if parsed_output:
    for ind, each_line in enumerate(parsed_output):
        temp_list_for_each_line = []
        primary_common_lines_regex = re.search(r'^(?!Hotfix.*|Network.*|Hyper.*|Virtual.*|Processor.*)'
                                               r'([a-zA-Z0-9\-\s\\*)(]+)(?:[\s\\.]+)?:\s+(.*)$', each_line, flags=re.I)
        regex_for_hotfix_and_processor_child_lines = re.search(r'^\s+(\[\d+]):\s+(.*)$', each_line, flags=re.I)
        primary_virtual_mem_regex = re.search(r'^(Virtual\s+Memory).*:\s+(.*):\s+(.*)$', each_line, flags=re.I)
        primary_nw_cards_regex = re.search(r'^(Network\s+Card[a-zA-Z0-9\-\s\\*)(]+):\s+(.*)$', each_line, flags=re.I)
        primary_hotfix_regex = re.search(r'^(Hotfix[a-zA-Z0-9\-\s\\*)(]+):\s+(.*)$', each_line, flags=re.I)
        primary_hyper_regex = re.search(r'^(Hyper.*):\s+(.*):\s+(.*)$', each_line, flags=re.I)
        primary_processor_regex = re.search(r'^(Processor[a-zA-Z0-9\-\s\\*)(]+):\s+(.*)$',
                                            each_line, flags=re.I)

        # Dynamically get dict key after that appropriate key was created
        for k, v in final_dict.items():
            if re.search(r'Hyper.*', k, flags=re.I):
                hyper_key = k
            if re.search(r'Network\s+Card.*', k, flags=re.I):
                nw_card_key = k
            if re.search(r'Hotfix.*', k, flags=re.I):
                hotfix_key = k
            if re.search(r'Processor.*', k, flags=re.I):
                processor_key = k
            if re.search(r'Virtual.*', k, flags=re.I):
                virtual_key = k

        if primary_processor_regex:
            final_dict.update({primary_processor_regex.group(1).strip(): primary_processor_regex.group(2).strip()})
        elif primary_virtual_mem_regex:
            # Create/Update virtual memory key
            if virtual_key == '':
                final_dict.setdefault(primary_virtual_mem_regex.group(1).strip(), []).append(eval(str(
                    {primary_virtual_mem_regex.group(2).strip(): primary_virtual_mem_regex.group(3).strip()})))
            else:
                for key, value in final_dict.items():
                    if virtual_key == key:
                        value[-1].update(
                            {primary_virtual_mem_regex.group(2).strip(): primary_virtual_mem_regex.group(3).strip()})
        elif hyper_key != '' and primary_common_lines_regex:
            # Update primary key for hyper
            for key, value in final_dict.items():
                if hyper_key == key:
                    value[-1].update(
                        {primary_common_lines_regex.group(1).strip(): primary_common_lines_regex.group(2).strip()})
        elif primary_hotfix_regex:
            # Create primary key for hotfix
            final_dict.update({primary_hotfix_regex.group(1).strip(): primary_hotfix_regex.group(2).strip()})
        elif primary_nw_cards_regex:
            # Create primary key for network cards
            final_dict.update({primary_nw_cards_regex.group(1).strip(): primary_nw_cards_regex.group(2).strip()})
        elif primary_hyper_regex:
            # Create primary key for hyper
            final_dict.setdefault(primary_hyper_regex.group(1).strip(), []).append(eval(str(
                {primary_hyper_regex.group(2).strip(): primary_hyper_regex.group(3).strip()})))
        elif nw_card_key != '':
            # Create and update key for network cards key
            # This regex to find out the current line of parent line(dict key to update)
            nw_previous_line_check_regex = re.search(r'^\s+(\[\d+]):\s+(.*)$', parsed_output[ind - 1], flags=re.I)
            nw_current_line_regex = re.search(r'^\s+(\[\d+]):\s+(.*)$', each_line, flags=re.I)
            nw_common_line_regex = re.search(r'([a-zA-Z0-9\-\s\\*)(]+)(?:[\s\\.]+)?:\s+(.*)$', each_line, flags=re.I)
            ip_regex = re.search(r'^\s+(?!:)([a-zA-Z0-9\-\s\\*)(]+)(?:[\s\\.]+)?$', each_line, flags=re.I)

            if nw_current_line_regex and primary_ip_key == '':
                # Create ip-address key
                strip_op = each_line.strip().split(':')
                list_for_nw_primary_key_update.append({strip_op[0].strip(): strip_op[1].strip()})
            elif nw_previous_line_check_regex is None and nw_current_line_regex is None and nw_common_line_regex:
                # Update the dict of dict child key, example lines: Status: Media disconnected, DHCP Enabled: Yes
                strip_op = each_line.strip().split(':')
                for each_key, each_value in final_dict.get(nw_card_key)[-1].items():
                    if isinstance(each_value, list):
                        for each_dict_value in each_value:
                            if isinstance(each_dict_value, dict):
                                each_dict_value.update({strip_op[0].strip(): strip_op[1].strip()})
            elif nw_previous_line_check_regex and nw_common_line_regex and list_for_nw_primary_key_update:
                # This block to update the child key of value of 1st dict
                # Example lines: Connection Name: Ethernet, Connection Name: Wi-Fi 2
                child_dict_for_nw_cards = {nw_common_line_regex.group(1).strip(): nw_common_line_regex.group(2).strip()}
                nw_final_dict = {}
                nw_final_list = []
                nw_list_to_append_child_dict = []

                if isinstance(list_for_nw_primary_key_update[-1], dict):
                    for k, v in list_for_nw_primary_key_update[-1].items():
                        nw_list_to_append_child_dict.append(v)
                        nw_list_to_append_child_dict.append(child_dict_for_nw_cards)
                        nw_final_dict[k] = nw_list_to_append_child_dict
                for key, val in final_dict.items():
                    if nw_card_key == key:
                        if isinstance(val, list):
                            nw_final_list.extend(val)
                        elif isinstance(val, str):
                            nw_final_list.append(val)
                        nw_final_list.append(nw_final_dict)
                if nw_final_list:
                    # Overwrite existing key
                    final_dict[nw_card_key] = nw_final_list
            elif ip_regex is not None and nw_previous_line_check_regex is None and \
                    nw_current_line_regex is None and nw_common_line_regex is None:
                # Get primary ip-address key
                primary_ip_key = ip_regex.group(1)
            elif primary_ip_key != '':
                # Create primary ip-address key and update all the ip-addresses of dict into the primary ip-address key
                nw_dict_for_update = {}
                # Replace 1st occurrence of ':'
                replace_1st_occurrence = each_line.replace(':', '-', 1)
                strip_op = replace_1st_occurrence.strip().split('-')
                if not any(x is True for x in [True if primary_ip_key in each_item[-1] else False
                                               for each_item in list(final_dict.get(nw_card_key)[-1].values())]):
                    # When the primary_ip_key is not exists in final_dict
                    nw_dict_for_update = {primary_ip_key: {strip_op[0].strip(): strip_op[1].strip()}}
                    # final_dict.get(nw_card_key).append(eval(str(nw_dict_for_update)))
                    for key, value in final_dict.get(nw_card_key)[-1].items():
                        if isinstance(value, list):
                            for each_item in value:
                                if isinstance(each_item, dict):
                                    each_item.update(eval(str(nw_dict_for_update)))
                else:
                    # When the primary_ip_key is exists in final_dict
                    for each_item in final_dict.get(nw_card_key):
                        if isinstance(each_item, dict):
                            for key_1, val_1 in each_item.items():
                                if primary_ip_key in val_1[-1]:
                                    val_1[-1][primary_ip_key].update({strip_op[0].strip(): strip_op[1].strip()})
        elif regex_for_hotfix_and_processor_child_lines:
            # Create/Update child key for hotfix and processor
            dict_for_hotfix_and_processor = {}
            strip_op = each_line.strip().split(':')
            dict_for_hotfix_and_processor.update({strip_op[0].strip(): strip_op[1].strip()})
            list_for_hf = []
            list_for_pr = []
            for key, val in final_dict.items():
                if hotfix_key == key:
                    if isinstance(val, list):
                        list_for_hf.extend(val)
                        for j in val:
                            if isinstance(j, dict):
                                j.update(dict_for_hotfix_and_processor)
                    elif isinstance(val, str):
                        list_for_hf.append(val)
                        list_for_hf.append(dict_for_hotfix_and_processor)
                        final_dict.update({hotfix_key: list_for_hf})
                elif processor_key == key and hotfix_key == '':
                    if isinstance(val, list):
                        list_for_pr.extend(val)
                        for j in val:
                            if isinstance(j, dict):
                                j.update(dict_for_hotfix_and_processor)
                    elif isinstance(val, str):
                        list_for_pr.append(val)
                        list_for_pr.append(dict_for_hotfix_and_processor)
                        final_dict.update({processor_key: list_for_pr})
        elif primary_common_lines_regex:
            # Create primary key for all common lines,
            # Example lines: OS Name: Microsoft Windows 10 Pro, OS Version: 10.0.19045 N/A Build 19045
            final_dict.update({
                primary_common_lines_regex.group(1).strip(): primary_common_lines_regex.group(2).strip()})

print('Final_dict: ', final_dict)
