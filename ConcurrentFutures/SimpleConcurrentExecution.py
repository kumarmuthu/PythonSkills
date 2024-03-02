__version__ = "2024.03.02.01"
__author__ = "Muthukumar Subramanian"

'''
SimpleConcurrentExecution
History:
2024.03.02.01 - Initial Draft
'''

import time
import concurrent.futures
from selenium import webdriver


def run_selenium_test(server_config, test_case):
    # Simulating test execution
    # driver = webdriver.Chrome()
    print(f"Running Selenium test, server_config: {server_config}, test_case: {test_case}")
    for i in range(5):
        time.sleep(1)
        print(f"Sleep: {i}, server_config: {server_config}, test_case: {test_case}")
    # driver.quit()


def run_suite(suite_name, test_cases, server_config, test_parallel=True):
    # Ensure tests are executed in parallel if test_parallel is True
    if test_parallel:
        with concurrent.futures.ThreadPoolExecutor() as executor:
            executor.map(lambda test_case: run_selenium_test(server_config, test_case), test_cases)
    else:
        for test_case in test_cases:
            run_selenium_test(server_config, test_case)


def run_parallel_test_suites(server_config, test_suites, test_parallel):
    # suite_tasks = []
    for suite_name, test_cases in test_suites.items():
        # Ensure tests within each suite are executed sequentially if test_parallel is False
        if test_parallel:
            with concurrent.futures.ThreadPoolExecutor() as executor:
                executor.submit(run_suite, suite_name, test_cases, server_config, test_parallel)
        else:
            run_suite(suite_name, test_cases, server_config, test_parallel)


def main(server_configs, test_suites, suite_parallel=True, test_parallel=True):
    start_time = time.time()  # Record start time
    # suite_tasks = []
    for server_config in server_configs:
        if suite_parallel:
            # Run suites in parallel
            with concurrent.futures.ThreadPoolExecutor() as executor:
                executor.submit(run_parallel_test_suites, server_config, test_suites, test_parallel)
        else:
            # Run suites sequentially
            for suite_name, test_cases in test_suites.items():
                run_suite(suite_name, test_cases, server_config, test_parallel)

    end_time = time.time()  # Record end time

    # Calculate total execution time
    total_time = end_time - start_time
    print(f"Total execution time: {total_time} seconds")


if __name__ == "__main__":
    test_suites = {
        "testsuite-1": ["tc-1", "tc-2", "tc-3"],
        "testsuite-2": ["tc-5", "tc-6"]
    }
    server_configs = ["Excel_sheet_1", "Excel_sheet_2", "Excel_sheet_3"]
    suite_parallel_execution = False
    test_parallel_execution = False

    main(server_configs, test_suites, suite_parallel=suite_parallel_execution, test_parallel=test_parallel_execution)
