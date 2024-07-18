#!/usr/bin/python3
"""Log parsing"""
import sys
import re
import signal

regex = re.compile(
    r'^\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3} - \[.*?\] '
    r'"GET /projects/260 HTTP/1.1" '
    r'(\d{3}) (\d+)$'
)

line_count = 0
total_size = 0
status_count = {200: 0, 301: 0, 400: 0, 401: 0, 403: 0, 404: 0, 405: 0, 500: 0}


def parse_line(line):
    try:
        parts = line.split()
        status_code = int(parts[-2])
        file_size = int(parts[-1])
        return status_code, file_size
    except (IndexError, ValueError):
        return None


def is_valid_line(line):
    return regex.match(line)


def update_stats(status_code, file_size):
    global total_size
    total_size += file_size
    if status_code in status_count:
        status_count[status_code] += 1


def print_stats():
    """Print the computed statistics."""
    print(f"File size: {total_size}")
    for status in sorted(status_count.keys()):
        if status_count[status] > 0:
            print(f"{status}: {status_count[status]}")


def signal_handler(sig, frame):
    """Handle keyboard interruption (CTRL + C)."""
    print_stats()
    sys.exit(0)


signal.signal(signal.SIGINT, signal_handler)

try:
    for line in sys.stdin:
        line_count += 1
        if is_valid_line(line):
            data = parse_line(line)
            if data:
                status_code, file_size = data
                update_stats(status_code, file_size)

        if (line_count % 10) == 0:
            print_stats()

except Exception as e:
    print(f"Error: {e}")
