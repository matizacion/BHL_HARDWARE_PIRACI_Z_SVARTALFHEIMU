import pandas as pd
import csv

data = b'H,6,23,31,5,5'

days = {1: "Mon", 2: "Tue", 3: "Wed", 4: "Thu", 5: "Fri", 6: "Sat", 7: "Sun"}


class CSVReadWrite:
    def __init__(self):
        self.sets_file = open("pills_sets.csv", "r")
        self.sets = [line.rstrip() for line in self.sets_file]
        self.sets_file.close()
        self.sets_file = open("pills_sets.csv", "w", newline='')

        print(self.sets)

        self.pills_file = open("pills_storage.csv", "r")
        self.pills = [line.rstrip() for line in self.pills_file]
        self.pills_file.close()
        self.pills_file = open("pills_storage.csv", "w", newline='')

        print(self.pills)

    def __del__(self):

        for line in self.sets:
            self.sets_file.write(line)
            self.sets_file.write('\n')

        for line in self.pills:
            self.pills_file.write(line)
            self.pills_file.write('\n')
        print("destruktor")

    def write(self, incoming_str):
        list_of_pills = incoming_str.split(",")
        with open('pills_storage.csv', 'w') as file:
            writer = csv.writer(file)
            writer.writerow(list_of_pills)

    def read(self):
        pills = pd.read_csv("pills_storage.csv", header=None)
        pills = pills.values.tolist()[0]
        return pills

    def write_set_of_pills(self, incoming_bytes):
        incoming_str = incoming_bytes.decode('UTF-8')
        sets_pills = incoming_str.split(",")
        date = days[int(sets_pills[1])] + " " + sets_pills[2] + sets_pills[3]
        empty_list = [0] * 6
        empty_list[0] = date
        print(date)
        # sets_pills.insert(0, date)
        # with open('pills_sets.csv', 'a', newline="") as file:
        #     writer = csv.writer(file)
        #     writer.writerow(sets_pills)

    def read_set_of_pills(self):
        pills = pd.read_csv("pills_sets.csv", header=None)
        pills = pills.values.tolist()
        pills_dict = {}
        for i in range(len(pills)):
            pills_dict[pills[i][0]] = pills[i][1:]

        return pills_dict


w = CSVReadWrite()
