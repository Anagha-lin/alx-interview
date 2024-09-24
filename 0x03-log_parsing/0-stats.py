#!/usr/bin/python3
"""
0-stats.py: Reads log lines from stdin and computes metrics.

Usage:
    ./0-stats.py

The script reads each line from standard input, parses it, and computes:
- Total file size.
- Number of lines by status code.

After every 10 lines and/or upon keyboard interruption (CTRL + C),
the script prints the computed metrics.
"""

import sys
import signal
import re

# Initialize counters
total_size = 0
status_codes = [200, 301, 400, 401, 403, 404, 405, 500]
status_counts = {code: 0 for code in status_codes}
line_count = 0

# Compile regex pattern for performance
log_pattern = re.compile(
    r'^(\d{1,3}\.){3}\d{1,3} - \[.+\] "GET /projects/260 HTTP/1\.1" (\d{3}) (\d+)$'
)

def print_stats():
    """
    Prints the accumulated metrics.
    """
    print(f"File size: {total_size}")
    for code in sorted(status_codes):
        count = status_counts.get(code, 0)
        if count:
            print(f"{code}: {count}")

def signal_handler(sig, frame):
    """
    Handles keyboard interruption (CTRL + C).
    Prints the stats before exiting.
    """
    print_stats()
    sys.exit(0)

# Register the signal handler for CTRL + C
signal.signal(signal.SIGINT, signal_handler)

def main():
    global total_size, line_count
    try:
        for line in sys.stdin:
            line = line.strip()
            line_count += 1

            # Match the line against the regex pattern
            match = log_pattern.match(line)
            if match:
                try:
                    status_code = int(match.group(2))
                    file_size = int(match.group(3))
                    
                    if status_code in status_counts:
                        status_counts[status_code] += 1
                    total_size += file_size
                except ValueError:
                    # Skip lines with non-integer status codes or file sizes
                    pass

            # After every 10 lines, print the stats
            if line_count % 10 == 0:
                print_stats()
    except Exception:
        # In case of unexpected exceptions, ensure stats are printed
        print_stats()
        sys.exit(1)
    
    # After processing all lines, print the stats
    print_stats()

if __name__ == "__main__":
    main()

