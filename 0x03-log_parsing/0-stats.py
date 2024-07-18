#!/usr/bin/python3
"""Log parsing"""
import sys
import re
import signal

regex = (
    r'^\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3} - \[.*?\] '
    r'"GET /projects/260 HTTP/1.1" '
    r'(\d{3}) (\d+)$'
)

line_count = 0
total_size = 0
status_count = {200: 0, 301: 0, 400: 0, 401: 0, 403: 0, 404: 0, 405: 0, 500: 0}


def print_stats():
    """Print the computed statistics."""
    print(f"File size: {total_size}")
    for status in sorted(status_count):
        if status_count[status] > 0:
            print(f"{status}: {status_count[status]}")


try:
    for line in sys.stdin:
        match = re.match(regex, line)
        if match:
            file_size = int(match.group(2))
            status_code = int(match.group(1))

            total_size += file_size
            if status_code in status_count:
                status_count[status_code] += 1

            line_count += 1
            if line_count == 10:
                print_stats()
                line_count = 0

    print_stats()

except KeyboardInterrupt:
    print_stats()
    raise
