__version__ = "2023.01.28.01"
__author__ = "Muthukumar Subramanian"

"""
Utility, this utility will help to run tests with a specific runtime.
The test will stop the execution when reaching the elapsed runtime.
Available Singleton utility, ThreadWithReturnValue utility, Two thread monitors.
"""

import inspect
import time
import threading
import ctypes
import copy
from threading import Thread, Event
from Utility import *
import re


class Singleton(type):
    """
    ..codeauthor:: Muthukumar Subramanian
    """
    # Inherit from "type" in order to gain access to method __call__
    def __init__(cls, *args, **kwargs):
        # cls._instance = None
        cls._instance = {}
        # Create a variable to store the object reference
        super().__init__(*args, **kwargs)

    def __new__(mcs, name, bases, class_dict, **kwargs):
        class_ = super().__new__(mcs, name, bases, class_dict)
        if kwargs:
            for name, value in kwargs.items():
                setattr(class_, name, value)
        return class_

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instance:
            # if the object has not already been created
            cls._instance[cls] = super().__call__(*args, **kwargs)
            # Call the __init__ method of the subclass (FrameworkAbstractClass) and save the reference
            return cls._instance[cls]
        elif kwargs.get('update'):
            # update the new object
            cls._instance[cls] = super().__call__(*args, **kwargs)
            # Call the __init__ method of the subclass (FrameworkAbstractClass) and update the reference
            return cls._instance[cls]
        else:
            # if object (FrameworkAbstractClass) reference already exists; return it
            return cls._instance[cls]


class ThreadWithReturnValue(Thread):
    """
    Thread with return value
    ..codeauthor:: Muthukumar Subramanian
    """

    def __init__(self, group=None, target=None, name=None, interval=None, args=(), kwargs=None, *, daemon=None):
        Thread.__init__(self, group, target, name, args, kwargs, daemon=daemon)
        self.interval = interval
        self._return = None
        self.killed = False
        self.lock = threading.Lock()

    def start(self):
        Thread.start(self)

    def run(self):
        """
        ..codeauthor:: Muthukumar Subramanian
        :return:
        """
        # print("RUN method")
        if self._target is not None:
            self._return = self._target(*self._args, **self._kwargs)

    def join(self, *args):
        Thread.join(self, *args)
        return self._return

    def get_id(self):
        if hasattr(self, 'thread_id'):
            return self._thread_id
        for thread_id, thread in threading._active.items():
            if thread is self:
                self._thread_id = thread_id
                return thread_id

    def kill(self):
        thread_id = self.get_id()
        self.killed = True
        response = ctypes.pythonapi.PyThreadState_SetAsyncExc(thread_id, ctypes.py_object(SystemExit))
        if response > 1:
            ctypes.pythonapi.PyThreadState_SetAsyncExc(thread_id, 0)
            print("Exception in kill method")


class RuntimeBasedScriptExecution(metaclass=Singleton, update=None):
    """
    Utility class - RuntimeBasedScriptExecution
    """

    def __init__(self, get_logging_obj, update=False):
        self.event = Event()
        self.total_video_count = 0
        self.executed_video_count = 0
        self.log_obj = get_logging_obj

    def run_dummy_test(self):
        self.log_obj.info("Testing the utility without child test...")
        for i in range(1, 11):
            self.log_obj.info(f"Iter count: {i}")
            time.sleep(1)

    def run_test(self, *args, **kwargs):
        self.run_utility_test(**kwargs)

    def run_utility_test(self, *args, **kwargs):
        """
        ..codeauthor:: Muthukumar Subramanian
        User defined functions
        :return:
        """
        # Call child job function
        ret_time_for_child_job = self.child_job(**kwargs)
        return True

    def child_job(self, **kwargs):
        """
        ..codeauthor:: Muthukumar Subramanian
        # Do your testcase stuff here
        :param kwargs: child job related kwargs
        :return: Boolean
        """
        self.log_obj.info("Child job is running...")
        child_func_test_start_time = test_start_time()

        def run_child_job(**kwargs):
            """
            ..codeauthor:: Muthukumar Subramanian
            Run actual test scenario here
            :param kwargs: job related kwargs
            :return: None
            """
            for i in range(1, 21):
                self.log_obj.info(f"Iter count: {i}")
                time.sleep(1)

        try:
            calculate_executed_job_time = 0
            # Call run_child_job function based on the loop requirement
            if kwargs.get("loop_test"):
                # With Loop test
                calculate_executed_job_time, self.total_video_count = self.run_loop_test(
                    child_func_test_start_time, run_child_job, self.total_video_count, **kwargs)
            else:
                # Without Loop test
                RuntimeBasedScriptExecution(self.log_obj).child_method(kwargs.get('child_test_runtime'),
                                                                       run_child_job, **kwargs)
                end_time = test_end_time(child_func_test_start_time)
                calculate_executed_job_time = (calculate_executed_job_time + int(
                    end_time.total_seconds()) - calculate_executed_job_time)
                self.log_obj.info(f"Summary for Non-Loop test  - Job spent time(s): {calculate_executed_job_time}")
            # child_func_test_total_time = test_end_time(child_func_test_start_time)
        except CustomException as err:
            self.log_obj.error(f"Observed exception in run_child_job function, Exception: {err}")
            raise "Observed exception in run_child_job function"
        return True

    def run_loop_test(self, loop_test_start_time, job_function_name, total_video_count, **kwargs):
        """
        ..codeauthor:: Muthukumar Subramanian
        :param total_video_count: total_video_count
        :param loop_test_start_time: loop test start time
        :param job_function_name: which job need to run
        :param kwargs: needed
        :return: job runtime
        """
        calculate_executed_job_time = 0
        self.total_video_count = total_video_count
        while not self.event.is_set():
            ret_job_exec_time = RuntimeBasedScriptExecution(
                self.log_obj).child_method(kwargs.get('child_test_runtime'), job_function_name, **kwargs)
            self.log_obj.info(f"Job Total Time: {ret_job_exec_time}")
            if ret_job_exec_time is None or ret_job_exec_time == 0:
                end_time = test_end_time(loop_test_start_time)
                calculate_executed_job_time = (calculate_executed_job_time + int(
                    end_time.total_seconds()) - calculate_executed_job_time)
                break
            calculate_executed_job_time = calculate_executed_job_time + int(ret_job_exec_time.total_seconds())
            self.total_video_count = self.total_video_count + self.total_video_count
        self.log_obj.info(f"Summary for Loop test - Job spent time(s): {calculate_executed_job_time}")
        return calculate_executed_job_time, self.total_video_count

    def main_test_runtime_monitor(self, thread_obj, monitor_start_time, test_elapse_runtime=1, *args, **kwargs):
        """
        ..codeauthor:: Muthukumar Subramanian
        :param thread_obj: 1st thread object to kill the 1st thread's operation when reach elapse time
        :param monitor_start_time: main test start time
        :param test_elapse_runtime: User given script's end of runtime
        :param args: not used
        :param kwargs: need for Post test
        :return: main test's total time
        """
        end_time = None
        original_monitor_start_time = copy.deepcopy(monitor_start_time)
        try:
            self.log_obj.info(f"Test will exit after: {test_elapse_runtime} sec...")
            while True:
                # convert from datetime to timestamp
                if not isinstance(monitor_start_time, int):
                    monitor_start_time = int(monitor_start_time.timestamp())
                current_time = test_start_time()
                if not isinstance(current_time, int):
                    current_time = int(current_time.timestamp())

                elapse_time = monitor_start_time + test_elapse_runtime
                if current_time + 1 >= elapse_time:
                    # Setting the Event and killing the child thread operation before kill the main test
                    self.event.set()
                    for i in threading.enumerate():
                        if re.search(r'<ThreadWithReturnValue.*child.*>', str(i), flags=re.I):
                            i.kill()
                    if kwargs.get('run_post_test'):
                        # Run post test for imported class
                        self.log_obj.info("{:*^60}".format("Main test - POST TEST - Start"))
                        try:
                            getattr(kwargs.get('cls_obj'), 'run_post_test')()
                        except Exception as Err:
                            self.log_obj.error(f"Observed exception while executing the POST TEST!, "
                                               f"Exception: {Err}")
                        else:
                            self.log_obj.info("Successfully executed the POST TEST...")
                        self.log_obj.info("{:*^60}".format("Main test - POST TEST - End"))
                    time.sleep(1)
                    # Kill the main test execution, elapsed run time
                    thread_obj.kill()
                    end_time = test_end_time(original_monitor_start_time)
                    self.log_obj.info(f"Main test - Reached the script's timeout value, "
                                      f"So killing/Stopping the script execution!.")
                    self.log_obj.info(f"Main test - Elapsed runtime!: {elapse_time}")
                    self.log_obj.info(f"Main test - Time Summary Report:: Start time: {monitor_start_time}, "
                                      f"Current time: {current_time}, Elapsed runtime: {elapse_time}")
                    break
        except CustomException as err:
            self.log_obj.error(f"Observed exception in CountDown function, Exception: {err}")
            raise "Observed exception in CountDown function"
        return end_time

    def child_runtime_monitor(self, thread_obj, monitor_start_time, test_elapse_runtime=1, *args, **kwargs):
        """
        ..codeauthor:: Muthukumar Subramanian
        :param thread_obj: 1st thread object to kill the 1st thread's operation when reach elapse time
        :param monitor_start_time: child test start time
        :param test_elapse_runtime: User given child test's end of runtime
        :param args: not used
        :param kwargs: need for Post test
        :return: child test's total time
        """
        end_time = None
        original_monitor_start_time = copy.deepcopy(monitor_start_time)
        try:
            self.log_obj.info(f"Job Test will exit after: {test_elapse_runtime} sec...")
            while True:
                # convert from datetime to timestamp
                if not isinstance(monitor_start_time, int):
                    monitor_start_time = int(monitor_start_time.timestamp())
                current_time = test_start_time()
                if not isinstance(current_time, int):
                    current_time = int(current_time.timestamp())

                elapse_time = monitor_start_time + test_elapse_runtime
                if current_time >= elapse_time:
                    # Kill the child test execution, elapsed run time
                    thread_obj.kill()
                    end_time = test_end_time(original_monitor_start_time)
                    self.log_obj.info(f"Job - Reached the timeout value!.")
                    self.log_obj.info(f"Job - Elapsed runtime!: {elapse_time}")
                    self.log_obj.info(f"Job - Summary Report:: Start time: {monitor_start_time}, "
                                      f"Current time: {current_time}, Elapsed runtime: {elapse_time}")
                    break
        except CustomException as err:
            self.log_obj.error(f"Observed exception in CountDown function, Exception: {err}")
            raise "Observed exception in CountDown function"
        return end_time

    def main_method(self, user_elapse_runtime, obj=None, **kwargs):
        """
        ..codeauthor:: Muthukumar Subramanian
        :param user_elapse_runtime: User given main test's max runtime
        :param obj: object
        :return: main test total run time
        """
        kwargs.update({'cls_obj': obj})
        main_test_start_time = test_start_time()
        if obj is None:
            t1 = ThreadWithReturnValue(target=self.run_dummy_test)
        else:
            if inspect.isfunction(obj):
                t1 = ThreadWithReturnValue(target=obj, kwargs=kwargs)
            else:
                t1 = ThreadWithReturnValue(target=getattr(obj, kwargs.get('run_function')), kwargs=kwargs)
        t2 = ThreadWithReturnValue(target=self.main_test_runtime_monitor, args=[t1, main_test_start_time,
                                                                                user_elapse_runtime], kwargs=kwargs)
        # starting thread 1
        t1.start()
        # starting thread 2
        t2.start()
        # ending thread 2
        main_test_total_time = t2.join()
        t1.join()
        table_for_execution_total_time(main_test_total_time, self.log_obj)
        return main_test_total_time

    def child_method(self, child_test_elapse_runtime, obj=None, **kwargs):
        """
        ..codeauthor:: Muthukumar Subramanian
        :param child_test_elapse_runtime: User given child test's max runtime
        :param obj: object
        :return: child test total run time
        """
        assert kwargs.get('child_test_runtime') <= kwargs.get('main_test_runtime'), \
            f"Main test runtime: {kwargs.get('main_test_runtime')} " \
            f"should be greater than job's runtime: {kwargs.get('child_test_runtime')}"
        child_test_total_time = 0
        if self.event.is_set() is False:
            child_test_start_time = test_start_time()
            if obj is None:
                t1 = ThreadWithReturnValue(target=self.run_utility_test, daemon=True)
            else:
                if inspect.isfunction(obj):
                    t1 = ThreadWithReturnValue(target=obj, daemon=True, kwargs=kwargs)
                else:
                    t1 = ThreadWithReturnValue(target=getattr(obj, kwargs.get('run_function')), daemon=True,
                                               kwargs=kwargs)
            t1.name = 'child1'
            t2 = ThreadWithReturnValue(target=self.child_runtime_monitor,
                                       args=[t1, child_test_start_time, child_test_elapse_runtime], daemon=True,
                                       kwargs=kwargs)
            t2.name = 'child2'
            # starting thread 1
            t1.start()
            # starting thread 2
            t2.start()
            # ending thread 2
            child_test_total_time = t2.join()
            t1.join()
        return child_test_total_time

    def run_post_test(self):
        self.log_obj.info(f"Video Summary Report:: Total video count: {self.total_video_count}, "
                          f"Executed video count: {self.executed_video_count}")


if __name__ == '__main__':
    # Call Logger function
    get_log_obj = logger_function(__file__)
    get_log_obj.info("{:*^60}".format("Utility - Start"))
    # Scenario-1 - Test without kwargs
    # RuntimeBasedScriptExecution(get_log_obj).main_method(5)
    # Scenario-2 - Test without kwargs and with attribute update
    # RuntimeBasedScriptExecution(get_log_obj, update=True).main_method(3)

    # Scenario-3 - Test with kwargs
    dict_for_job = {}
    cls_obj = RuntimeBasedScriptExecution(get_log_obj)
    dict_for_job.update({'run_function': 'run_test',
                         'run_post_test': False,
                         'child_test_runtime': 4,
                         'main_test_runtime': 30,
                         'loop_test': False})
    cls_obj.main_method(dict_for_job.get('main_test_runtime'), cls_obj, **dict_for_job)
    get_log_obj.info("{:*^60}".format("Utility - End"))
