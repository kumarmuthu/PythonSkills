from random import randint, choice
from string import hexdigits

__version__ = "2019.10.30.01"
__author__ = "Muthukumar Subramanian"


class RandomIpaddress():
    def __init__(self, existing_ip=None):
        self.previous_ip = existing_ip

    def random_ip(self, ip_type=None):
        '''
        ..codeauthor:: Muthukumar Subramanian
        Usage:
            Required argument(s):
                :param ip_type: required str '4'| int 4 for ipv4
                                or str '6'| int 6 for ipv6
                                or str 'all'
                                or None <default ipv4>
            Optional argument(s):
                None
        :return: return_dict
        '''
        return_dict = {}
        if isinstance(ip_type, int):
            ip_type = str(ip_type)
        list_for_type = []
        if ip_type == 'all':
            list_for_type = ['4', '6']
        else:
            if ip_type is None:
                ip_type = '4'
            list_for_type.append(ip_type.strip())
        try:
            if list_for_type:
                for each_ip_type in list_for_type:
                    final_ip = None
                    if each_ip_type == '4':
                        while True:
                            final_ip = '.'.join(str(randint(0, 255)) for _ in range(4))
                            if self.previous_ip != final_ip:
                                break
                            else:
                                print("Generated ip-address is matched with "
                                      "existing ip-address: {}".format(self.previous_ip))
                        return_dict['ipv4'] = final_ip
                    elif each_ip_type == '6':
                        while True:
                            final_ip = ':'.join(''.join(choice(hexdigits).lower() for _ in range(4))
                                                for _ in range(8))
                            if self.previous_ip != final_ip:
                                break
                            else:
                                print("Generated ip-address is matched with "
                                      "existing ip-address: {}".format(self.previous_ip))
                        return_dict['ipv6'] = final_ip
        except Exception as err:
            print("Observed exception is: {}".format(err))
        return return_dict


if __name__ == '__main__':
    # For example existing ip-address is '83.210.115.205'
    # cls_obj = RandomIpaddress('83.210.115.205')

    # Non-existing ip-address to create a constructor
    cls_obj = RandomIpaddress()
    # Ipv6 and Ipv4
    ipv_6_and_ipv4 = cls_obj.random_ip('all')
    print("ipv_6_and_ipv4: {}".format(ipv_6_and_ipv4))

    # Ipv6 str '6' with leading|trailing spaces
    ipv_6 = cls_obj.random_ip(' 6')
    print("ipv_6: {}".format(ipv_6))

    # Ipv6 str '6' without leading|trailing spaces
    ipv_6 = cls_obj.random_ip('6')
    print("ipv_6: {}".format(ipv_6))

    # Ipv6 int '6'
    ipv_6 = cls_obj.random_ip(6)
    print("ipv_6: {}".format(ipv_6))

    # Ipv4 str '4' with leading|trailing spaces
    ipv_4 = cls_obj.random_ip('4 ')
    print("ipv_4: {}".format(ipv_4))

    # Ipv4 str '4' without leading|trailing spaces
    ipv_4 = cls_obj.random_ip('4')
    print("ipv_4: {}".format(ipv_4))

    # Ipv4 int '4'
    ipv_4 = cls_obj.random_ip(4)
    print("ipv_4: {}".format(ipv_4))

    # Default ip-address type
    ipv_4 = cls_obj.random_ip()
    print("Default ip-address type: {}".format(ipv_4))

    # Invalid ip-address
    ipv_4 = cls_obj.random_ip(42)
    print("Invalid ipaddress: {}".format(ipv_4))
