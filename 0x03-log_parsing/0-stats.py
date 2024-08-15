#!/usr/bin/python3
"""
This script reads stdin line by line and computes metrics.
It processes log entries in the format:
<IP Address> - [<date>] "GET /projects/260 HTTP/1.1" <status code> <file size>
After every 10 lines or upon receiving a keyboard interruption (CTRL + C),
it prints the total file size and the count of each status code.
"""

import sys
import signal

# Initialize variables
status_codes = ['200', '301', '400', '401', '403', '404', '405', '500']
cache = {code: 0 for code in status_codes}
total_size = 0
line_count = 0

def print_stats():
    """Prints the accumulated statistics."""
    print(f"File size: {total_size}")
    for code in sorted(cache.keys()):
        if cache[code] > 0:
            print(f"{code}: {cache[code]}")

def signal_handler(sig, frame):
    """Handles keyboard interruption (CTRL + C) to print statistics."""
    print_stats()
    sys.exit(0)

# Register the signal handler
signal.signal(signal.SIGINT, signal_handler)

try:
    for line in sys.stdin:
        line_list = line.split()
        if len(line_list) > 6:  # Ensure the line contains all necessary parts
            code = line_list[-2]
            try:
                size = int(line_list[-1])
                total_size += size
            except ValueError:
                continue  # Skip lines where file size is not a valid integer

            if code in cache:
                cache[code] += 1

            line_count += 1

            if line_count == 10:
                print_stats()
                line_count = 0

except Exception as e:
    print(f"An error occurred: {e}")

finally:
    print_stats()

