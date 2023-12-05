#!/usr/bin/python3
"""Reads from standard input and computes metrics"""

from sys import stdin


def statusprint(size = 0, status_codes = {}):
    """Print accumulated metrics"""
    print("File size: {}".format(size))
    for key in sorted(status_codes):
        print("{}: {}".format(key, status_codes[key]))


if __name__ == "__main__":
    """Reads from standard input and computes metrics"""
    targetcodes = ['200', '301', '400', '401', '403', '404', '405', '500']
    linecount = 0
    status_codes = {}
    size = 0
# Execute this code unless there is a keyboard interrupt
    try:
        for line in stdin:
            if linecount == 10:
                statusprint(size, status_codes)
                linecount = 1
            else:
                linecount += 1

            line = line.split()
# Skip empty lines
            try:
                size += int(line[-1])
            except (IndexError, ValueError):
                pass
# Check for status code
            try:
                if line[-2] in targetcodes:
                    if status_codes.get(line[-2], -1) == -1:
                        status_codes[line[-2]] = 1
                    else:
                        status_codes[line[-2]] += 1
            except IndexError:
                pass
# Print accumulated metrics
        statusprint(size, status_codes)
# Handle keyboard interrupt
    except KeyboardInterrupt:
        statusprint(size, status_codes)
        raise
