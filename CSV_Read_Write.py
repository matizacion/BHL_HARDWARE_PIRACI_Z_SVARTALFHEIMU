class CSVReadWrite:
    days = {1: "Mon", 2: "Tue", 3: "Wed", 4: "Thu", 5: "Fri", 6: "Sat", 7: "Sun"}

    def __init__(self):
        self.sets_file = open("pills_sets.csv", "r")
        self.sets = [(line.rstrip().split(',')) for line in self.sets_file]

        self.sets = {elem[0]: elem[1:] for elem in self.sets}

        self.sets_file.close()
        self.sets_file = open("pills_sets.csv", "w", newline='')

        self.pills_file = open("pills_storage.csv", "r")
        self.pills = self.pills_file.read()
        self.pills_file.close()

        self.pills_file = open("pills_storage.csv", "w", newline='')
        self.pills = self.pills.split(",")

    def __del__(self):
        for key in self.sets.keys():
            self.sets_file.write(key + "," + ",".join(self.sets[key]))
            self.sets_file.write('\n')

        self.pills_file.write(",".join(self.pills))
        self.pills_file.close()
        self.sets_file.close()

    def write(self, split_str):
        self.pills = split_str

    def write_set_of_pills(self, split_str):
        date = self.days[int(split_str[0])] + " " + split_str[1] + split_str[2]
        if date in self.sets.keys():
            (self.sets[date])[int(split_str[3])] = split_str[4]
        else:
            zeros = 6 * ['0']
            zeros[int(split_str[3])] = split_str[4]
            self.sets[date] = zeros

    def which_write(self, incoming_bytes):
        incoming_str = incoming_bytes.decode('UTF-8')
        split_str = incoming_str.split(",")
        if split_str[0] == 'S':
            self.write(split_str[1:])
        elif split_str[0] == 'H':
            self.write_set_of_pills(split_str[1:])
        else:
            pass