import os
import xlsxwriter
from time import localtime, strftime
import re

__version__ = "2019.12.01.01"
__author__ = "Muthukumar Subramanian"


class ExcelSheetWrite(object):
    def __init__(self):
        pass

    def excel_sheet_write_func(self, file_dir, input_dict, headers_1, sub_header_1, sub_header_2):
        '''
        ..codeauthor:: Muthukumar Subramanian
        Excel sheet will form used by dictionary input
        Usage:
            Required argument(s):
                :param file_dir: Required directory for excel sheet save
                :param input_dict: Required dictionary <dict of list>
                :param headers_1: Required header name
                :param sub_header_1: Required sub-header-1 name
                :param sub_header_2: Required sub-header-2 name
            Optional argument(s):
                None
        :return: None
        '''
        current_time = strftime("%H_%M_%S", localtime())
        get_current_date = strftime("%d_%m_%Y", localtime())
        date_and_time = get_current_date + '_' + current_time
        pid = str(os.getpid())
        end_stamp = '_' + date_and_time + '_' + pid
        # condition for file_dir variable
        #     Below format will work
        #     file_dir = 'F:\\Python\\script\\excel_write'
        #     file_dir = 'F:\\Python\\script\\excel_write\\'
        #     file_dir = 'F:/Python/script/excel_write'
        regex_dir = re.sub(r'\/', '\\\\', file_dir)
        split_list = regex_dir.split('\\')
        split_list = [x for x in split_list if x != '']
        split_list_to_str = '\\'.join(split_list)
        filename = '%s\\MyExcel%s.xlsx' % (split_list_to_str, end_stamp)

        # Create a workbook and add a worksheet.
        workbook = xlsxwriter.Workbook(filename)
        worksheet = workbook.add_worksheet("MyExcel sheet")

        # formats for excel sheet cell
        bg_format1 = workbook.add_format({'bg_color': '#78B0DE', 'bold': True, 'font_size': 20, 'align': 'center',
                                          'indent': True})
        bg_format2 = workbook.add_format({'bg_color': '#FFFFFF', 'bold': True, 'font_color': 'block', 'font_size': 24,
                                          'indent': True, 'align': 'center', 'text_wrap': True})
        bg_format3 = workbook.add_format({'bold': False, 'font_size': 20, 'border': True, 'indent': True,
                                          'font_color': 'green'})
        bg_format31 = workbook.add_format({'bold': False, 'font_size': 20, 'border': True, 'indent': True,
                                           'font_color': 'orange'})
        bg_format4 = workbook.add_format({'bg_color': '#33cc33', 'bold': False, 'font_size': 16, 'border': True,
                                          'indent': True})
        bg_format41 = workbook.add_format({'bg_color': '#ff9933', 'bold': False, 'font_size': 16, 'border': True,
                                           'indent': True})

        # Tuple and list combination support logic here
        column_len = 0
        headers_1_len = len(headers_1)
        for key, value in input_dict.items():
            for key1, value2 in value.items():
                if isinstance(value2, list) or isinstance(value2, tuple):
                    # list of list
                    if isinstance(value2[0], list):
                        column_len = len(value2[0])
                    # list of list
                    elif isinstance(value2[0], tuple):
                        column_len = len(value2[0])
                    # single dimension list or tuple
                    else:
                        modified_value2 = []
                        for i in range(0, len(value2), headers_1_len):
                            tuple_or_list = value2[i:i + headers_1_len]
                            if isinstance(tuple_or_list, tuple):
                                # tuple to list conversion
                                tuple_or_list = list(tuple_or_list)
                            else:
                                tuple_or_list = tuple_or_list
                            modified_value2.append(tuple_or_list)
                        if modified_value2:
                            # Equalizing row and column for single dimension list or tuple.
                            # Example Matrix: 2x2, 16x16 64x64.
                            # Invalid matrix as Row 4 and column have 2
                            for index_mod, j in enumerate(modified_value2):
                                column_len = len(modified_value2[index_mod])
                                if column_len != headers_1_len:
                                    raise Exception("Please check this key1: '%s', key2: '%s' "
                                                    "single dimension list/tuple,Is it missed some value "
                                                    "on that list!!!" % (key, key1))
                            input_dict[key].update({key1: modified_value2})

        # Increasing cell width here, this will apply for headers column and row
        worksheet.set_column(0, (column_len - 1), 18)
        # Headers: 1
        worksheet.write_row(0, 0, headers_1, bg_format1)
        header_3_row_count = 1
        final_val_row_count = 1

        list_author = input_dict.keys()
        # Headers: 2
        for index_0, each_auth in enumerate(sub_header_1):
            for li_auth in list_author:
                if each_auth == li_auth:
                    if header_3_row_count != 1:
                        header_3_row_count += 1
                    worksheet.write_string(header_3_row_count, 0, each_auth, bg_format2)
                    # Headers: 3
                    for index_1, each_tic in enumerate(sub_header_2):
                        if index_1 == 0 and index_0 == 0:
                            header_2_row_count = header_3_row_count + 1
                        elif index_1 == 0 and index_0 > 0:
                            header_2_row_count = header_3_row_count + 1
                        else:
                            header_2_row_count = final_val_row_count + 1
                        if each_tic == 'action_1':
                            font_f = bg_format31
                            font_f1 = bg_format41
                        else:
                            font_f = bg_format3
                            font_f1 = bg_format4
                        worksheet.write_string(header_2_row_count, 0, each_tic, font_f)
                        final_val_row_count = header_2_row_count + 1
                        for final_key, final_val in input_dict.get(each_auth).items():
                            if final_key == each_tic:
                                print("Console O/P: {} {} {}".format(each_auth, each_tic, final_val))
                                for each_column in final_val:
                                    worksheet.write_row(final_val_row_count, 0, each_column, font_f1)
                                    if list(input_dict.get(each_auth).get(each_tic))[-1] == each_column:
                                        final_val_row_count = final_val_row_count
                                        if sub_header_2[-1] == each_tic:
                                            header_3_row_count = final_val_row_count + 1
                                    else:
                                        final_val_row_count += 1
                else:
                    continue
        workbook.close()


if __name__ == '__main__':
    # tuple and list
    tuple_data1 = (['id_1', 'Anand', '1', 'http://a'],
                   ['id_2', 'Bala', '2', 'http://b'],
                   ['id_3', 'Cholan', '3', 'http://c'],
                   ['id_4', 'Deepan', '4', 'http://d'])
    # list and tuple
    tuple_data2 = [('id_5', 'Eshaan', '5', 'http://e'),
                   ('id_6', 'Franklin', '6', 'http://f'),
                   ('id_7', 'Gajendra', '7', 'http://g')
                   ]
    # tuple and tuple
    tuple_data3 = (('id_8', 'Hari', '8', 'http://h'),
                   ('id_9', 'Ilayaraja', '9', 'http://i'),
                   ('id_10', 'John', '10', 'http://j'),
                   ('id_11', 'Karan', '11', 'http://k'))
    # list and list
    tuple_data4 = [['id_12', 'Lakhmipati', '12', 'http://l'],
                   ['id_13', 'Muthu', '13', 'http://m'],
                   ['id_14', 'Nakul', '14', 'http://n'],
                   ['id_15', 'Oja', '15', 'http://o'],
                   ['id_16', 'Praveen', '16', 'http://p']]
    # tuple with single dimension
    tuple_data5 = ('id_17', 'Raghav', '17', 'http://r',
                   'id_18', 'Suriya', '18', 'http://s',
                   'id_19', 'Tamilan', '19', 'http://t',)
    # list with single dimension
    tuple_data6 = ['id_20', 'Umesh', '20', 'http://u',
                   'id_21', 'Vikram', '21', 'http://v',
                   'id_22', 'Williamson', '22', 'http://w',
                   'id_23', 'Xavier', '23', 'http://x']

    # list with single dimension
    # Invalid single dimension list, here missed few column. Row and column value should be equal otherwise
    # exception will throw.
    # tuple_data5 = ('id_17', 'Raghav', '17', 'http://r',
    #                'id_18', 'Suriya',
    #                'id_19', 'Tamilan', '19', 'http://t',)
    # tuple_data6 = ['id_20',
    #                'id_21', 'Vikram', '21', 'http://v',
    #                'id_22', 'Williamson', '22', 'http://w',
    #                'id_23', 'Xavier', '23', 'http://x']

    sheet_dict = {'karthi': {'action_2': tuple_data1, 'action_1': tuple_data2},
                  'kumar': {'action_1': tuple_data3, 'action_2': tuple_data4},
                  'muthu': {'action_1': tuple_data5, 'action_2': tuple_data6},
                  }
    header1_list = ['header_column_1', 'header_column_2', 'header_column_3', 'header_column_4']
    header2_list = ['muthu', 'karthi', 'kumar']
    header3_list = ['action_1', 'action_2']

    cls_obj = ExcelSheetWrite()
    sheet_save_dir = 'F:\\Python\\script\\excel_write\\log'
    cls_obj.excel_sheet_write_func(file_dir=sheet_save_dir, input_dict=sheet_dict, headers_1=header1_list,
                                   sub_header_1=header2_list, sub_header_2=header3_list)
else:
    cls_obj = ExcelSheetWrite()
