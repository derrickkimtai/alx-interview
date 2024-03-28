#!/usr/bin/python3
"""Log parsing"""
import sys

status_codes = {"200": 0, "301": 0, "400": 0, "401": 0, "403": 0, "404": 0, "405": 0, "500": 0}
file_size = 0
counter = 0


def print_stats():
    """Print stats"""
    print("File size: {}".format(file_size))
    for code in sorted(status_codes.keys()):
        if status_codes[code] > 0:
            print("{}: {}".format(code, status_codes[code]))

try:
    for line in sys.stdin:
        try:
            parts = line.split()
            size = int(parts[-1])
            code = parts[-2]
            if code in status_codes:
                status_codes[code] += 1
                file_size += size
        except:
            continue

        counter += 1
        if counter % 10 == 0:
            print_stats()
except KeyboardInterrupt:
    print_stats()
    raise
finally:
    print_stats()
