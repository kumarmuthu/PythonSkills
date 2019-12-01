from datetime import datetime, date, timedelta
from dateutil.relativedelta import *
import re

__version__ = "2019.12.01.01"
__author__ = "Muthukumar Subramanian"


class DateDifferenceCalculate(object):
    def __init__(self):
        pass

    @staticmethod
    def date_compatibility_fucn(exact_date_and_month=None, before_month_count=None, before_days_count=None,
                                increment_type=None):
        '''
        ..codeauthor:: Muthukumar Subramanian
        :param exact_date_and_month: pass YES|Yes|yes or NO|No|no if you need exact date and month difference
        :param before_month_count: default month count is <type int> '1'
        :param before_days_count: default day count is <type int> '30'
        :param increment_type: pre increment for previous data or post increment for future data
        :return: return_dict
                Example:  {'current_date': '2019-11-01', 'datetime_format_current':
                datetime.datetime(2019, 11, 1, 0, 0), 'string_of_months': '2019-10-01', 'string_of_days': None,
                'datetime_format_before': datetime.datetime(2019, 10, 1, 0, 0)}
        '''

        return_dict = {}
        final_before_days = None
        final_before_months = None
        string_of_months = None
        string_of_days = None

        # condition check for increment_type
        if increment_type is None:
            inc_type = 'pre'
        else:
            if increment_type == 'pre':
                inc_type = 'pre'
                print("Date difference for 'pre' increment for previous data")
            elif increment_type == 'post':
                inc_type = 'post'
                print("Date difference for 'post' increment for future data")
            else:
                raise Exception("Only the pre or post value is supported. Please provide the valid data on "
                                "'increment_type' variable")

        # condition check for exact_date_and_month
        if exact_date_and_month is None:
            exact_date = True
        else:
            regx = re.match(r'([Yy](?:ES|es))|([Nn](?:O|o))', exact_date_and_month)
            if regx is not None:
                g1 = regx.group(1)
                g2 = regx.group(2)
                if g1 is not None:
                    exact_date = True
                elif g2 is not None:
                    exact_date = False
            else:
                # regex will not break here
                regx = re.match('([YyEeSs]+)|([NnOo]+)', exact_date_and_month)
                if regx is not None:
                    g1 = regx.group(1)
                    g2 = regx.group(2)
                    if g1 is not None:
                        exact_date = True
                    elif g2 is not None:
                        exact_date = False
        # condition check for before_month_count and before_days_count
        month_count = None
        days_count = None
        if before_month_count is not None and before_days_count is not None:
            raise Exception("User can give either before_month_count or before_days_count")
        elif before_month_count is None and before_days_count is None:
            print("Both Days and Months is None, so default 'months count' as '1'")
            month_count = 1
        elif before_month_count is not None:
            if before_month_count is None:
                month_count = 1
            else:
                month_count = int(before_month_count)
        elif before_days_count is not None:
            if before_days_count is None:
                print("Both Days and Months is None, so default 'days count' as '30'")
                days_count = 30
            else:
                days_count = before_days_count

        # Today date and time
        current_date = datetime.today()
        # current_date = '2019-11-01 12:49:00.710802'  # hard code
        print("Initial Date and Time: {}".format(current_date))
        regex_date = re.match(r'(\d{4}-\d{2}-\d{2})\s+(\d{2}:\d{2}:\d{2}).*', str(current_date))
        if regex_date is not None:
            date_val = regex_date.group(1)
            time_val = regex_date.group(2)  # As of now unused
            date_val_r = regex_date.group(1).split('-')
            time_val_r = regex_date.group(2).split(':')
        current_date_and_time = datetime(int(date_val_r[0]), int(date_val_r[1]), int(
            date_val_r[2]), int(time_val_r[0]), int(time_val_r[1]), int(time_val_r[2]))

        print("current_date is: {}".format(date_val))
        current_date_and_time_without_msec = datetime.strptime(str(current_date_and_time), '%Y-%m-%d %H:%M:%S')
        current_date_and_time_without_msec = str(current_date_and_time_without_msec)
        current_date_list = current_date_and_time_without_msec.split(' ')
        date_str_format = current_date_list[0]
        time_str_format = current_date_list[1]  # As of now unused

        # Getting the current date here
        current_date_now = None
        regex_date_c = re.match(r'(\d{4}-\d{2}-\d{2})', date_str_format)
        if regex_date_c is not None:
            current_date_conv = regex_date_c.group().split('-')
            if exact_date is False and before_days_count is not None:
                current_date_now = '%s-%s-%s' % (current_date_conv[0], current_date_conv[1], current_date_conv[2])
            elif exact_date is True:
                current_date_now = '%s-%s-%s' % (current_date_conv[0], current_date_conv[1], current_date_conv[2])
            elif exact_date is False and before_days_count is None:
                current_date_now = '%s-%s-%s' % (current_date_conv[0], current_date_conv[1], '01')
        final_date = datetime.strptime(str(current_date_now), '%Y-%m-%d')

        # Getting a days difference here
        if days_count is not None:
            print("days_count enabled!!!")
            if inc_type == 'pre':
                days_before = (final_date - timedelta(days=int('%d' % (days_count))))
            else:
                days_before = (final_date + timedelta(days=int('%d' % (days_count))))
            days_before = days_before.isoformat().split(' ')
            regex_date = re.match(r'(\d{4}-\d{2}-\d{2})', days_before[0])
            if regex_date is not None:
                before_date_conv = regex_date.group().split('-')
                if exact_date is False and before_days_count is not None:
                    string_of_days = '%s-%s-%s' % (before_date_conv[0], before_date_conv[1], before_date_conv[2])
                    print("We cant set satrt date as '01',So we are disabling this variable exact_date_and_month'")
                elif exact_date is True:
                    string_of_days = '%s-%s-%s' % (before_date_conv[0], before_date_conv[1], before_date_conv[2])
                elif exact_date is False and before_days_count is None:
                    string_of_days = '%s-%s-%s' % (before_date_conv[0], before_date_conv[1], '01')
            final_before_days = datetime.strptime(str(string_of_days), '%Y-%m-%d')
        else:
            print("months_count enabled!!!")
            if inc_type == 'pre':
                update_prev_mon = (current_date_and_time - relativedelta(months=int('+%d' % (month_count))))
            else:
                update_prev_mon = (current_date_and_time + relativedelta(months=int('+%d' % (month_count))))
            update_prev_mon = str(update_prev_mon)
            months_before = update_prev_mon.split(' ')
            regex_date = re.match(r'(\d{4}-\d{2}-\d{2})', months_before[0])
            if regex_date is not None:
                before_months_conv = regex_date.group().split('-')
                if exact_date is False and before_days_count is not None:
                    string_of_months = '%s-%s-%s' % (before_months_conv[0], before_months_conv[1],
                                                     before_months_conv[2])
                elif exact_date is True:
                    string_of_months = '%s-%s-%s' % (before_months_conv[0], before_months_conv[1],
                                                     before_months_conv[2])
                elif exact_date is False and before_days_count is None:
                    string_of_months = '%s-%s-%s' % (before_months_conv[0], before_months_conv[1], '01')
            final_before_months = datetime.strptime(str(string_of_months), '%Y-%m-%d')
        if final_before_months:
            datetime_format_before = final_before_months
            before_data = string_of_months
        else:
            datetime_format_before = final_before_days
            before_data = string_of_days
        # 'string_of_months': string_of_months, 'string_of_days': string_of_days,
        return_dict = {'current_date': current_date_now, 'datetime_format_current': final_date,
                       'before_data': before_data, 'datetime_format_before': datetime_format_before}
        return True, return_dict


if __name__ == '__main__':
    cls_obj = DateDifferenceCalculate()
    # ret_code, ret_dict = cls_obj.date_compatibility_fucn(increment_type='pre')
    # ret_code, ret_dict = cls_obj.date_compatibility_fucn()
    ret_code, ret_dict = cls_obj.date_compatibility_fucn(exact_date_and_month='y', before_month_count=None,
                                                         before_days_count=70, increment_type='post')
    print("Current date now: {}".format(ret_dict.get('current_date')))
    print("Before Data: {}".format(ret_dict.get('before_data')))
