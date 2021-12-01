"""Where I solve the puzzle yo"""

import os


def read_file(filename: str) -> str:
    """Reads contents of given file"""
    with open(filename, "r") as content_file:
        return content_file.read()


def main():
    measurements = [int(m) for m in read_file("input.txt").split("\n") if m]

    total = 0
    prev_measurement = measurements[0]
    for measurement in measurements[1:]:
        if measurement > prev_measurement:
            total += 1
        prev_measurement = measurement

    print(total)


main()
