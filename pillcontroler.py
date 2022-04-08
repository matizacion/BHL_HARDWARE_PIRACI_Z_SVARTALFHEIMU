import maestro
from time import sleep
from CSV_Read_Write import CSVReadWrite
from dataclasses import dataclass


@dataclass
class Time:
    d: str = "Mon"
    h: int = 0
    m: int = 0


current_time = Time()
days = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
time_speed = 0.001  # ile czasu w sekundach trwa minuta


class PillBox:
    def __init__(self, controller, servo_no, start_capacity=0, wait_time=1):
        self.controller = controller
        self.servo_no = servo_no

        self.wait_time = wait_time

        self.capacity = start_capacity

        self.zero()

    def zero(self):
        self.controller.setTarget(self.servo_no, 3000 * 4)

    def drop_pill(self):
        if self.capacity <= 0:
            raise "ERROR! BRAK NARKOTYKOW"

        self.controller.setTarget(self.servo_no, 1000 * 4)
        sleep(self.wait_time)
        self.controller.setTarget(self.servo_no, 3000 * 4)
        sleep(self.wait_time)

        self.capacity -= 1

        if self.capacity <= 0:
            print("ERROR! BRAK NARKOTYKOW")

    def drop_more_pills(self, amount_of_pills):
        for i in range(amount_of_pills):
            self.drop_pill()


######################################
######################################
######################################

class PillController:
    def __init__(self, tty_str):
        self.servo_controller = maestro.Controller(ttyStr=tty_str)

        self.pills_containers_num = 6
        self.pill_boxes = []
        self.csv_read_write = CSVReadWrite()

        self.rotation = {}
        self.set_pill_rotation()

        for i in range(self.pills_containers_num):
            self.pill_boxes.append(PillBox(self.servo_controller, i))

        self.set_capacities()

    def drop_pills(self, drop_list_or_dict):
        for i in range(self.pills_containers_num):
            self.pill_boxes[i].drop_more_pills(drop_list_or_dict[i])

    def set_capacities(self):
        capacity_list = [156, 145, 142, 23, 15, 6, 17]  # CSVReadWrite.read_set_of_pills()
        for i in range(self.pills_containers_num):
            self.pill_boxes[i].capacity = capacity_list[i]

    def set_pill_rotation(self):
        self.rotation = self.csv_read_write.read_set_of_pills()


if __name__ == '__main__':
    pill_controler = PillController("COM5")

    while True:
        for day in days:
            current_time.d = day
            for hour in range(24):
                current_time.h = hour
                if current_time.h < 10:
                    hour_string = f"0{current_time.h}"
                else:
                    hour_string = f"{current_time.h}"

                for minute in range(60):
                    current_time.m = minute

                    if current_time.m < 10:
                        minute_string = f"0{current_time.m}"
                    else:
                        minute_string = f"{current_time.m}"

                    current_time_string = f"{current_time.d} " + hour_string + minute_string

                    if current_time_string in pill_controler.rotation.keys():
                        print(pill_controler.rotation[current_time_string])
                        pill_controler.drop_pills(pill_controler.rotation[current_time_string])

                    sleep(time_speed)
