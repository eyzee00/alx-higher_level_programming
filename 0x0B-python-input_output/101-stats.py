#!/usr/bin/python3
"""Module: defines script that reads
stdin line by line and computes metrics"""

import sys


if __name__ == "__main__":
    total_size = 0
    status_codes = {
        '200': 0,
        '301': 0,
        '400': 0,
        '401': 0,
        '403': 0,
        '404': 0,
        '405': 0,
        '500': 0
    }
    count = 0
    try:
        for line in sys.stdin:
            count += 1
            line = line.split()
            if len(line) > 2:
                status_code = line[-2]
                if status_code in status_codes:
                    status_codes[status_code] += 1
                total_size += int(line[-1])
        print("File size: {}".format(total_size))
        for key in sorted(status_codes):
            if status_codes[key] > 0:
                print("{}: {}".format(key, status_codes[key]))
    except:
        pass
