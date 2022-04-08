import maestro
from time import sleep
from CSV_Read_Write import CSVReadWrite


class PillBox:
    def __init__(self, controller, servo_no, start_capacity=0, wait_time=1):
        self.controller = controller
        self.servo_no = servo_no

        self.wait_time = wait_time

        self.capacity = start_capacity

        self.zero()

    def zero(self):
        self.controller.setTarget(self.servo_no, 1000 * 4)

    def drop_pill(self):
        if self.capacity <= 0:
            raise "ERROR! BRAK NARKOTYKOW"

        self.controller.setTarget(self.servo_no, 3000 * 4)
        sleep(self.wait_time)
        self.controller.setTarget(self.servo_no, 1000 * 4)
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

        self.rotation = {}

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
        self.rotation = CSVReadWrite.read_set_of_pills()
