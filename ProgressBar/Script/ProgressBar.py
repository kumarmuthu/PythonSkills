from tqdm import tqdm
import time
import threading
from colorama import Fore, Back, Style


class ProgressBar:
    def __init__(self, total_iteration):
        self.total_iterations = total_iteration
        self.original_total_iterations = total_iteration
        self.progress_bar = None

    def display_progress_bar(self):
        """
        Progress Bar display
        """
        break_while_loop = False
        ret_per = self.percentage_calculator(self.original_total_iterations)
        print(f"Calculated percentage(%): {ret_per}")
        total_per_val = self.original_total_iterations - ret_per
        print(f"Display percentage(%): {total_per_val}")
        while True:
            if self.total_iterations <= total_per_val:
                if break_while_loop:
                    break
                else:
                    if self.progress_bar.n >= 100:
                        self.progress_bar.set_description(desc="Finished task.")
                        break
                    self.progress_bar.update(100 - total_per_val)
                    for i in range(0, total_per_val):
                        # tqdm.write("Resume progress bar...")
                        # tqdm.write("\033[F\033[J")  # move cursor up and clear line
                        if self.total_iterations <= 1 and self.progress_bar.n >= 100:
                            break_while_loop = True
                            self.progress_bar.set_description(desc="Finished task.")
                            break
                        else:
                            time.sleep(1)
                            # update the progress bar
                            self.progress_bar.update(1)

    def calculate_elapse_time(self, elapse_time):
        """
        without sleep time
        :param elapse_time: Run the loop for x seconds
        :return:
        """
        start_time = time.monotonic()
        end_time = start_time + elapse_time
        while time.monotonic() <= end_time:
            # Check every second here
            print("Every sec!", time.monotonic())
            self.total_iterations -= 1
            # Wait for 1 second
            while time.monotonic() < start_time + 1:
                pass
            start_time += 1

    @staticmethod
    def percentage_calculator(input_value, percentage=90):
        """
        :param input_value: given second(s)
        :param percentage: calculate percentage, default is 90%
        Example: input_value = 25, percentage = 100%
        :return: int: calculated percentage
        """
        result = int((percentage * input_value) / 100)
        return result

    def create_progress_bar(self, get_func):
        """
        :param get_func: get function name
        :return:
        """
        # create a tqdm progress bar with total percentage as 100
        self.progress_bar = tqdm(total=100, desc="In-Progress...",
                                 bar_format="{l_bar}%s{bar}%s{r_bar}%s" % (Fore.GREEN, Fore.CYAN, Fore.BLUE))
        # Style.RESET_ALL(Fore.CYAN)
        # create a thread to run the 'display_progress_bar' function
        t3 = threading.Thread(target=get_func)
        # start the thread
        t3.start()
        # wait for the thread to complete
        t3.join()
        # close the progress bar
        self.progress_bar.close()

    def main(self, progress_bar_time):
        print("{:*^30}".format("\tStart\t"))
        t1 = threading.Thread(target=self.create_progress_bar, args=[self.display_progress_bar])
        t2 = threading.Thread(target=self.calculate_elapse_time, args=[progress_bar_time])
        t1.start()
        t2.start()
        t1.join()
        t2.join()
        print("{:*^10}".format("\tEnd\t"))


t_time = 30
cls_obj = ProgressBar(t_time)
cls_obj.main(t_time)
