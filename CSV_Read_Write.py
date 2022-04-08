import pandas as pd
import csv


class CSVReadWrite:
    def write(in_coming_str: str):
        list_of_pills = in_coming_str.split(",")
        with open('pills_storage.csv', 'w') as file:
            writer = csv.writer(file)
            writer.writerow(list_of_pills)


    def read():
        pills = pd.read_csv("pills_storage.csv", header=None)
        pills = pills.values.tolist()[0]
        return pills


    def write_set_of_pills(in_coming_str: str):
        sets_pills = in_coming_str.split(",")
        with open('pills_sets.csv', 'a', newline="") as file:
            writer = csv.writer(file)
            writer.writerow(sets_pills)


    def read_set_of_pills():
        pills = pd.read_csv("pills_sets.csv", header=None)
        pills = pills.values.tolist()
        return pills

