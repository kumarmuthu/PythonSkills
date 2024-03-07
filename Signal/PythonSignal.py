__version__ = "2024.03.07.01"
__author__ = "Muthukumar Subramanian"

'''
Signal
History:
2024.03.07.01 - Initial Draft
'''

import signal
import sys
import time


def signal_handler(sig, frame):
    if sig == signal.SIGINT:
        print("\nReceived SIGINT (Ctrl+C), exiting gracefully")
        sys.exit(0)
    elif sig == signal.SIGTERM:
        print("\nReceived SIGTERM (close button), exiting gracefully")
        sys.exit(0)


def main():
    # Install the signal handlers for SIGINT (Ctrl+C) and SIGTERM (close button)
    signal.signal(signal.SIGINT, signal_handler)
    signal.signal(signal.SIGTERM, signal_handler)

    # Your main application logic goes here
    count = 0
    while count <= 10:
        count += 1
        time.sleep(1)
        print(f"Count: {count}")
    print("Completed script execution")


if __name__ == "__main__":
    main()
