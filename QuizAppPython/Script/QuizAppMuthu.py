__version__ = '2020.03.08.01'
__author__ = 'muthukumar subramanian'

import json
import random
import argparse
import re
import sys
import os


class QuizAppMuthu(object):
    def __init__(self, *args, **kwargs):
        self.user_default_play_count = 5
        self.append_list = []
        self.all_question = {}
        self.all_correct_answer = {}
        self.json_question_file_directory = 'F:\\Python\\Quiz_json_question_file.json'
        self.json_answer_file_directory = 'F:\\Python\\Quiz_json_answer_file.json'
        self.default_ans_mapping_sheet = {1: '10',
                                          2: 'Australia',
                                          3: 'All of the above',
                                          4: 'Sachin Tendulkar',
                                          5: '1975',
                                          6: 'Mujeeb ur Rahman'}

        self.default_question = {1: {'qus': 'How many teams are participating in the ICC World Cup 2019?',
                                     'ans': ['8', '9', '10', '12']},
                                 2: {'qus': 'Which cricket team has won most ICC Cricket World Cup titles?',
                                     'ans': ['West Indies', 'India', 'England', 'Australia']},
                                 3: {
                                     'qus': 'Which of the following country did not won the ICC Cricket'
                                            ' World Cup (50 over format) title so far?',
                                     'ans': ['South Africa', 'New zealand', 'England', 'All of the above']
        },
            4: {'qus': 'Which of the following Indian player have got first'
                ' “Man of the Tournament” Award in the ICC Cricket World Cup?',
                                     'ans': ['Sachin Tendulkar', 'Yuvraj Singh', 'Mohinder Amarnath', 'M.S. Dhoni']},
            5: {'qus': 'When was first ICC cricket World Cup started?',
                                     'ans': ['1972', '1975', '1985', '1979']},
            6: {'qus': 'Who is the youngest player in the ICC Cricket World Cup 2019?',
                                     'ans': ['Jonny Blaze Bairstow', 'Yuzvendra chahal', 'Mujeeb ur Rahman',
                                             'Kagiso Rabada']},
        }
        if os.path.exists(self.json_question_file_directory):
            if self.default_question:
                # dict overridden
                # new = { 10: {'qus': 'my name is',
                #                      'ans': ['muthu', 'kumar', 'msd', 'raina']},}
                self.all_question = self.update_dict(self.json_question_file_directory, old_dict=self.default_question)
                print(self.all_question)
        else:
            # JSON write
            write_bool = self.json_write(self.default_question, file_directory=self.json_question_file_directory)
            self.all_question = self.default_question
            print(self.all_question)

        if os.path.exists(self.json_answer_file_directory):
            if self.default_question:
                # dict overridden
                # new = { 10: 'muthu'}
                self.all_correct_answer = self.update_dict(self.json_answer_file_directory,
                                                           old_dict=self.default_ans_mapping_sheet)
                print(self.all_correct_answer)
        else:
            # JSON write
            write_bool = self.json_write(self.default_ans_mapping_sheet, file_directory=self.json_answer_file_directory)
            self.all_correct_answer = self.default_ans_mapping_sheet
            print(self.all_correct_answer)

    def update_dict(self, file_location, old_dict=None, new_dict=None):
        return_dict = {}
        # JSON/dict read and write
        with open(file_location, 'r+') as json_file_rdandwd:
            json_format_data = json.load(json_file_rdandwd)
            temp_dict = {}
            for each_key, each_value in json_format_data.items():
                if isinstance(each_key, str):
                    each_key = int(each_key)
                temp_dict.update({each_key: each_value})
            json_file_rdandwd.seek(0)
            json_file_rdandwd.truncate()
            if temp_dict:
                if old_dict is not None and isinstance(old_dict, dict):
                    old_dict.update(temp_dict)
                    json.dump(old_dict, json_file_rdandwd)
                if new_dict is not None and isinstance(new_dict, dict):
                    temp_dict.update(new_dict)
                    json.dump(temp_dict, json_file_rdandwd)
        for each_key, each_value in temp_dict.items():
            if isinstance(each_key, str):
                each_key = int(each_key)
            return_dict.update({each_key: each_value})
        return return_dict

    def delete_dict(self, file_location, delete_dict):
        return_dict = {}
        temp_dict = {}
        # JSON/dict delete and read
        with open(file_location, 'r+') as json_file_rdandwd:
            json_file_rdandwd.seek(0)
            json_file_rdandwd.truncate()
            json.dump(delete_dict, json_file_rdandwd)
        with open(file_location, 'r') as json_file_rd:
            temp_dict = json.load(json_file_rd)
        for each_key, each_value in temp_dict.items():
            if isinstance(each_key, str):
                each_key = int(each_key)
            return_dict.update({each_key: each_value})
        return return_dict

    def json_write(self, get_input_dict, file_directory):
        # JSON write
        with open(file_directory, 'w') as json_file_wd:
            json.dump(get_input_dict, json_file_wd)
        return True

    def json_read(self, json_file_directory):
        # JSON read
        with open(json_file_directory, 'r') as json_file_rd:
            json_read_data = json.load(json_file_rd)
        # if isinstance(json_question_data, dict):
        #     # w = json.dumps(json_data)  # dict to json
        #     # x = json.loads(w)          # json to dict
        return json_read_data

    def display_all_question(self):
        print("Displaying all the questions and answers are below!!")
        for each_key, each_value in self.all_question.items():
            for each_key_1, eac_value_1 in each_value.items():
                if each_key_1 == 'qus':
                    print("{}. Question is: {}\n Answer list is here: \n\t{}"
                          .format(each_key, eac_value_1, '\n\t'.join(list(str(each)
                                                                          for each in
                                                                          self.all_question.get(each_key).get(
                                                                              'ans')))))
        return True

    def admin(self):
        count_admin_head = 1
        while True:
            if count_admin_head > 3:
                print("you have reached maximum attempt for admin access rights!, so breaking this execution")
                break
            print("Dear admin what action you are looking: insert or update or delete or exit quiz")
            if count_admin_head == 3:
                print("This is your last attempt for admin access!")
            if count_admin_head == 1:
                print("Admin can access 3 times")
            admin_answer = sys.stdin.readline()
            admin_answer = admin_answer.strip()
            if admin_answer == 'insert':
                print("Selected option is '{}'".format(admin_answer))
                print("Please insert your quiz question:")
                get_question_count = 0
                while True:
                    found_duplicate = False
                    if get_question_count > 2:
                        raise Exception("You have reached maximum attempt for your quiz question insert!")
                    if get_question_count == 2:
                        print("This is your last attempt!")
                    get_question = sys.stdin.readline()
                    get_question = get_question.strip()
                    for each_k, each_v in self.all_question.items():
                        if get_question == each_v.get('qus'):
                            print("Can't duplicate the question!,please try another question!!!")
                            found_duplicate = True
                    if found_duplicate:
                        get_question_count += 1
                    else:
                        break
                print("Please provide your four option of answer for above question:")
                count = 1
                space_variable = ' '
                while True:
                    if count > 4:
                        break
                    get_answer = sys.stdin.readline()
                    get_answer = get_answer.strip()
                    space_variable += ' ' + get_answer
                    count += 1

                splited_list = space_variable.split(' ')
                option_of_ans = [e for e in splited_list if e != '']
                keys = self.all_question.keys()
                len_keys = len(keys)
                len_keys = len_keys + 1
                self.all_question = self.update_dict(self.json_question_file_directory,
                                                     new_dict={len_keys: {'qus': get_question, 'ans': option_of_ans}})
                # self.all_question.update({len_keys: {'qus': get_question, 'ans': option_of_ans}})
                print("Please insert your correct answer here:")
                correct_answer = sys.stdin.readline()
                correct_answer = correct_answer.strip()

                if len_keys in self.all_question:
                    answer_list = self.all_question.get(len_keys).get('ans')
                    if not answer_list:
                        raise Exception("Please check your question list")
                    if correct_answer in answer_list:
                        self.all_correct_answer = self.update_dict(self.json_answer_file_directory,
                                                                   new_dict={len_keys: correct_answer})
                        # self.all_correct_answer.update({len_keys: correct_answer})
                        # print("Given answer is updated on Quiz correct answer "
                        #       "mapping sheet: {}".format(self.all_correct_answer))
                        print("Given answer is updated on Quiz correct answer mapping sheet")
                    else:
                        raise Exception("Got mismatched answer %s, so please provide the correct answer "
                                        "if it is existing on default_ans_map_dict mapping sheet" % (correct_answer))
                else:
                    raise Exception("Unable to insert given answer on Quiz correct answer mapping sheet")
                self.display_all_question()
            elif admin_answer == 'delete':
                self.display_all_question()
                print("Please selected question number to delete the quiz question")
                admin_delete_answer = sys.stdin.readline()
                admin_delete_answer = admin_delete_answer.strip()
                if admin_delete_answer != '' and admin_delete_answer.isnumeric():
                    admin_delete_answer = int(admin_delete_answer)
                if admin_delete_answer:
                    if admin_delete_answer == 'exit':
                        print("Exiting quiz question delete")
                        break
                    if self.all_question.get(admin_delete_answer):
                        del self.all_question[admin_delete_answer]
                        self.all_question = self.delete_dict(self.json_question_file_directory, self.all_question)
                        print("Question is deleted successfully")
                        del self.all_correct_answer[admin_delete_answer]
                        self.all_correct_answer = self.delete_dict(self.json_answer_file_directory,
                                                                   self.all_correct_answer)
                        print("Answer is deleted successfully")
                        self.display_all_question()
                    else:
                        print("Given question number is not found on quiz question")
            elif admin_answer == 'update':
                def all_answer_correct_sheet_update(key):
                    if self.all_correct_answer.get(key):
                        print("Please update/change the correct answer of the current quiz question")
                        change_ans_sheet = sys.stdin.readline()
                        change_ans_sheet = change_ans_sheet.strip()
                        if change_ans_sheet in self.all_question.get(key).get('ans'):
                            self.all_correct_answer.update({admin_update_answer: change_ans_sheet})
                            print("Correct answer sheet is updated successfully: {}".format(self.all_correct_answer))
                        else:
                            print("Given answer is not there on question sheet!, please update an appropriate answer")
                    else:
                        print("Given question number is not exists on 'correct answer sheet'")
                    self.all_correct_answer = self.update_dict(self.json_answer_file_directory,
                                                               new_dict=self.all_correct_answer)
                    return True

                self.display_all_question()
                print("Please selected question number to update the quiz question and answer")
                admin_update_answer = sys.stdin.readline()
                admin_update_answer = admin_update_answer.strip()
                if admin_update_answer != '' and admin_update_answer.isnumeric():
                    admin_update_answer = int(admin_update_answer)
                if self.all_question.get(admin_update_answer):
                    update_count = 0
                    while True:
                        retry_enable = False
                        skip_question_and_answer_update = False
                        if update_count > 2:
                            break
                        if update_count == 2:
                            print("This is your last attempt for question or answer update!")
                        # for_loop_break = False
                        print("Please selected option(yes or no or exit update) to update all the sheet values("
                              "quiz question ,quiz answer and quiz correct answer map). "
                              "Else, correct answer sheet will be update")
                        admin_update_qa = sys.stdin.readline()
                        admin_update_qa = admin_update_qa.strip()
                        if re.match(r'Yes|y', admin_update_qa, flags=re.I):
                            print("Will update all the sheet")
                        elif re.match(r'No|n', admin_update_qa, flags=re.I):
                            print("Will update the correct answer sheet")
                            skip_question_and_answer_update = True
                        else:
                            if admin_update_qa == 'exit':
                                print("Exiting quiz Qus and Ans update")
                                break
                            print("Invalid selection!!!,please select yes or no")
                            retry_enable = True
                        if not skip_question_and_answer_update and not retry_enable:
                            for each_update_key, each_update_value in self.all_question.get(
                                    admin_update_answer).items():
                                if each_update_key == 'qus':
                                    print("Please update/change the quiz question")
                                    change_qus = sys.stdin.readline()
                                    change_qus = change_qus.strip()
                                    self.all_question.get(admin_update_answer).update({'qus': change_qus})
                                    print("Question is updated successfully")
                                    self.display_all_question()
                                elif each_update_key == 'ans':
                                    print("Please update/change the quiz answer")
                                    print("Please provide your four option of answer for above question:")
                                    count = 1
                                    space_variable = ' '
                                    while True:
                                        if count > 4:
                                            break
                                        get_answer = sys.stdin.readline()
                                        get_answer = get_answer.strip()
                                        space_variable += ' ' + get_answer
                                        count += 1

                                    split_list = space_variable.split(' ')
                                    update_option_of_ans = [e for e in split_list if e != '']
                                    self.all_question.get(admin_update_answer).update({'ans': update_option_of_ans})
                                    print("Answer is updated successfully")
                                    self.display_all_question()
                            self.all_question = self.update_dict(self.json_question_file_directory,
                                                                 new_dict=self.all_question)
                            # update/change the correct answer of the current quiz question
                            all_answer_correct_sheet_update(admin_update_answer)
                        else:
                            # update/change the correct answer of the current quiz question
                            all_answer_correct_sheet_update(admin_update_answer)
                        update_count += 1
                else:
                    print("Given question number is not found on our mapping sheet, please check it once")
                # self.all_question = self.update_dict(self.json_question_file_directory, self.all_question)
                # del self.all_correct_answer[admin_delete_answer]
                # self.all_correct_answer = self.update_dict(self.json_answer_file_directory, self.all_correct_answer)
            else:
                if admin_answer == 'exit':
                    print("Exiting quiz app")
                    break
                print("Selected option is invalid!!! please try again")
            count_admin_head += 1
        return True

    def display_question(self, user_ans):
        # verify
        def verify_answer(q_num, ver_ans):
            q_num = int(q_num)
            for each_key, each_value in self.all_question.items():
                if q_num == each_key:
                    for each_key_1, each_value_1 in each_value.items():
                        if each_key_1 == 'ans':
                            if ver_ans in each_value_1:
                                if ver_ans == self.all_correct_answer.get(q_num):
                                    print("Your answer is correct")
                                    return True
                                else:
                                    print("Your answer is wrong")
                                    return False
                            else:
                                print("Your answer is wrong(not found)")
                                return False

        temp_list = ["qus", "ans"]
        if not self.all_question:
            print("Questions are not found on our data base!!! {} \t.please try again".format(self.all_question))
            return False
        if self.all_question.get(user_ans):
            for each_key, each_value in self.all_question.get(user_ans).items():
                for each in temp_list:
                    if each_key == 'qus' and each_key == each:
                        db_qus = each_value
                        print('Question is: {}'.format(db_qus))
                    elif each_key == 'ans' and each_key == each:
                        db_ans = each_value
                        print('Options are: {}'.format(db_ans))
            try:
                print("Please provided your answer:")
                final_ans = sys.stdin.readline()
                final_ans = str(final_ans.strip())
            except Exception as Err:
                print("Observed exception as: {}".format(Err))
            else:
                print("Given Answer is: {}".format(final_ans))
                ret_bool = verify_answer(user_ans, final_ans)
                self.append_list.append(ret_bool)
        else:
            print("Your option is not found on our data base!!!.please try again")
            return False
        return True

    def test_question(self):
        if not self.all_question:
            print("Questions are not found on our data base!!! {} \t.please try again".format(self.all_question))
            return False
        # sequence = [i for i in range(1, random.randint(1, 2))]   # TODO
        # def myfunction():
        #     return 2.0
        # random_return = random.shuffle(sequence, myfunction)

        sequence = [i for i in range(1, len(self.all_question) + 1)]
        random_return = random.shuffle(sequence)
        print("Random order questions as {}".format(sequence))
        if sequence:
            count_in_test_question_func = 1
            for each_int in sequence:
                if count_in_test_question_func > self.user_default_play_count:
                    break
                if count_in_test_question_func == self.user_default_play_count:
                    print("This is your last question!")
                ret_code = self.display_question(each_int)
                count_in_test_question_func += 1

            length = len([e for e in self.append_list if e is True])
            print("{} answer(s) are correct".format(length))
            length = len([e for e in self.append_list if e is False])
            print("{} answer(s) are incorrect".format(length))
            print("Total questions are: {}".format(len(self.append_list)))

        return True


if __name__ == '__main__':
    arg = argparse.ArgumentParser("Game inline argument")
    arg.add_argument('--start-game', type=str, required=True,
                     help="Please you should give your decision start this game")
    parser = arg.parse_args()
    get_start_game = None
    get_start_game = parser.start_game
    if not re.match(r'yes|y', get_start_game, flags=re.I):
        print("You should give Yes or y option on inline argument(argparser)")
    else:
        obj = QuizAppMuthu()
        count_in_main_func = 1
        while True:
            if count_in_main_func > 3:
                break
            if count_in_main_func == 3:
                print("This is your last attempt!")
            print("please select any on of the option, admin or user")
            admin_or_user_answer = sys.stdin.readline()
            admin_or_user_answer = admin_or_user_answer.strip()
            if admin_or_user_answer == 'admin':
                ret_val = obj.admin()
                if ret_val or not ret_val:
                    break
            elif admin_or_user_answer == 'user':
                print("Are you play with default quiz question(Five)? (Yes/y or No/n)")
                quiz_question_of_count = sys.stdin.readline()
                quiz_question_of_count = quiz_question_of_count.strip()
                regex_quiz_question_of_count = re.match(r'^(?:(Yes|y)|(No|n))$', quiz_question_of_count, flags=re.I)
                if regex_quiz_question_of_count is not None:
                    if regex_quiz_question_of_count.group(1) is not None:
                        print("Your are proceeding with default count(Five) of quiz question")
                    else:
                        total_question = len(obj.all_question)
                        print("Your can play maximum {} question(s)".format(total_question))
                        print("Please selected number of question to start your game:")
                        user_defined_count = sys.stdin.readline()
                        user_defined_count = user_defined_count.strip()
                        if user_defined_count != '' and user_defined_count.isnumeric():
                            user_defined_count = int(user_defined_count)
                        if isinstance(user_defined_count, int):
                            if user_defined_count < total_question:
                                obj.user_default_play_count = user_defined_count
                            else:
                                raise Exception("You cant play {} above number of question(s)".format(total_question))
                        else:
                            print("Invalid value(data type)captured!")
                            print("Your are proceeding with default count(Five) of quiz question")
                else:
                    print("Selected option is wrong,so proceeding with default count(Five) of quiz question")
                print("The game is start now!")
                ret = obj.test_question()
                if ret or not ret:
                    break
            count_in_main_func += 1
