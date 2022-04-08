import pandas as pd
import csv


class CSVReadWrite:
    def write(self,in_coming_str: str):
        list_of_pills = in_coming_str.split(",")
        with open('pills_storage.csv', 'w') as file:
            writer = csv.writer(file)
            writer.writerow(list_of_pills)

    def read(self):
        pills = pd.read_csv("pills_storage.csv", header=None)
        pills = pills.values.tolist()[0]
        return pills

    def write_set_of_pills(self,in_coming_str, date):
        sets_pills = in_coming_str.split(",")
        sets_pills.insert(0, date)
        with open('pills_sets.csv', 'a', newline="") as file:
            writer = csv.writer(file)
            writer.writerow(sets_pills)

    def read_set_of_pills(self):
        pills = pd.read_csv("pills_sets.csv", header=None)
        pills = pills.values.tolist()
        pills_dict = {}
        for i in range(len(pills)):
            pills_dict[pills[i][0]] = pills[i][1:]

        return pills_dict






