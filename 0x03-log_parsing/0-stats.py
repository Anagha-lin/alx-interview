mport sys
import signal

# Initialize variables
total_file_size = 0
status_code_count = {}

def print_stats():
    """Prints the accumulated statistics."""
    print(f"File size: {total_file_size}")
    for code in sorted(status_code_count.keys()):
        print(f"{code}: {status_code_count[code]}")

def signal_handler(sig, frame):
    """Handles the keyboard interrupt signal (CTRL + C)."""
    print_stats()
    sys.exit(0)

# Register the signal handler
signal.signal(signal.SIGINT, signal_handler)

try:
    for i, line in enumerate(sys.stdin, 1):
        # Parse the line to extract necessary information
        parts = line.split()
        if len(parts) < 7:
            continue
        
        try:
            file_size = int(parts[-1])
            status_code = int(parts[-2])
            total_file_size += file_size
            if status_code in [200, 301, 400, 401, 403, 404, 405, 500]:
                if status_code in status_code_count:
                    status_code_count[status_code] += 1
                else:
                    status_code_count[status_code] = 1
        except ValueError:
            continue

        # Print stats every 10 lines
        if i % 10 == 0:
            print_stats()
except Exception as e:
    print(f"Error: {e}")
finally:
    print_stats()

