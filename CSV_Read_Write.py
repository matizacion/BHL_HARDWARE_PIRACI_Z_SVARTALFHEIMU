class CSVReadWrite:
    """
    Niezmiennik klasy -> słownik przyporządkujący liczbie porządkowej dzień tygodnia
    """
    days = {1: "Mon", 2: "Tue", 3: "Wed", 4: "Thu", 5: "Fri", 6: "Sat", 7: "Sun"}

    def __init__(self):
        """
        konstruktor klasy CSVReadWrite wczytujący dane z pliku csv
        """
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
        """
        Destruktor klasy CSVReadWrite zapisujący dane do pliku csv
        :return: None
        """
        for key in self.sets.keys():
            self.sets_file.write(key + "," + ",".join(self.sets[key]))
            self.sets_file.write('\n')

        self.pills_file.write(",".join(self.pills))
        self.pills_file.close()
        self.sets_file.close()

    def write(self, split_str):
        """
        metoda nadpisująca aktualną ilość tabletek
        :param split_str: List[str] -> każdy element to liczba tabletek odpowiedniego rodzaju
        :return: None
        """
        self.pills = split_str

    def write_set_of_pills(self, split_str):
        """
        metoda dopisująca/uaktualniająca dawki lekarstw na podawanych w określonym czasie
        :param split_str: List[str] -> pierwszym elementem jest data kolejne to liczby tabletek odpowiedniego rodzaju
        :return: None
        """
        date = self.days[int(split_str[0])] + " " + split_str[1] + split_str[2]
        if date in self.sets.keys():
            (self.sets[date])[int(split_str[3])] = split_str[4]
        else:
            zeros = 6 * ['0']
            zeros[int(split_str[3])] = split_str[4]
            self.sets[date] = zeros

    def which_write(self, incoming_bytes):
        """
        metoda sprawdzająca jakiego rodzaju dane są przetwarzane, a następnie wykonuje na nich odpowiednie metody zapisu
        :param incoming_bytes: przesłane dane w formie bajtowej
        :return: None
        """
        incoming_str = incoming_bytes.decode('UTF-8')
        split_str = incoming_str.split(",")
        if split_str[0] == 'S':
            self.write(split_str[1:])
        elif split_str[0] == 'H':
            self.write_set_of_pills(split_str[1:])
        else:
            pass
