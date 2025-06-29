"""
Copyright 2025 mas0yama [oyamamas]

wrote this to be able to use gobuster output data for input
"""


def parse_gobuster_dir_output(input_file):
    """
    :param input_file:
    :return: dict[path] = statuscode
    """

    # data laundry goes here
    raw_data = []
    with open(input_file, "rt") as f:
        raw_data = f.read().split('\n')

    raw_data = [x.strip() for x in raw_data if x != ""]

    # remove size column
    raw_data = [x.split('[')[0] for x in raw_data]

    # parse path and status code
    data = {}
    for line in raw_data:
        path, blank, statuscode = line.split()
        data[path] = int(statuscode[:3])

    return data






