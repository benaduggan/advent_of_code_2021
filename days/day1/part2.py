"""Where I solve the puzzle yo"""

import os


def read_file(filename: str) -> str:
    """Reads contents of given file"""
    with open(filename, "r") as content_file:
        return content_file.read()


def build_combined(measurements: list) -> list:
    """Builds a combined list of measurements"""
    combined = []
    for i in range(len(measurements)):
        if i + 2 < len(measurements):
            combined.append(measurements[i] + measurements[i + 1] + measurements[i + 2])
    return combined


def main():
    measurements = [int(m) for m in read_file("input.txt").split("\n") if m]
    # measurements = [int(m) for m in read_file("example_input.txt").split("\n") if m]

    total = 0
    measurements = build_combined(measurements)
    print(measurements)
    prev_measurement = measurements[0]
    for measurement in measurements[1:]:
        if measurement > prev_measurement:
            total += 1
        prev_measurement = measurement
    print(total)


main()
