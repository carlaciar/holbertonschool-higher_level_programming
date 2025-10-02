#!/usr/bin/env
"""
this module reads data from one format (CSV) and converting it
into another format (JSON) using serialization techniques.
"""

import csv
import json


def convert_csv_to_json(csv_filename):
    try:
        data = []
        # Open CSV file to read
        with open(csv_filename, "r") as csv_file:
            reader = csv.DictReader(csv_file)  # reads each row as a dictionary
            for row in reader:
                data.append(row)

        # Open JSON file to write
        with open("data.json", "w") as json_file:
            json.dump(data, json_file, indent=4)

        return True

    except FileNotFoundError:
        return False
