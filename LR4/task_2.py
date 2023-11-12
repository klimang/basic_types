import json
import csv

INPUT = "input.csv"
OUTPUT = "output.json"


def convert_csv_to_json(csv_filename,json_filename) -> None:
    with open(csv_filename, "r") as csv_file:
        csv_data = list(csv.DictReader(csv_file,
                                       delimiter=',',
                                       lineterminator='\n'))

    with open(json_filename, "w") as json_file:
        json.dump(csv_data, json_file, indent=4)


if __name__ == '__main__':
    convert_csv_to_json(INPUT,OUTPUT)

    with open(OUTPUT) as output_f:
        for line in output_f:
            print(line, end="")