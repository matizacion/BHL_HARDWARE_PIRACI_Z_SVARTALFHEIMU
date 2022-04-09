import maestro
from time import sleep
from CSV_Read_Write import CSVReadWrite
from dataclasses import dataclass


class PillBox:
    """
    Class representing one pill box with one pill server.
    """

    def __init__(self, controller, servo_no, start_capacity=0, wait_time=1, zero_pos=3000, delivery_position=1000):
        """
        Initialise one Pill Box
        :param controller: instance of a Controller class from maestro.py file.
        :param servo_no: number representing this pillbox (position at which servo is plugged into Polulu Maestro)
        :param start_capacity: amount of pills at start time (default 0)
        :param wait_time: time taken to deliver one pill to common container (default 1)
        :param zero_pos: position at which servo starts (int or float in us) (also position at which servo delivers pill to common container)
        :param delivery_position: position at which servo takes pill from container (int or float in us)
        """
        self.controller = controller
        self.servo_no = servo_no

        self.wait_time = wait_time

        self.capacity = start_capacity

        self.zero()

    def zero(self):
        """
        Zero servo on closed position (not accepting pills)
        :return: None
        """
        self.controller.setTarget(self.servo_no, 3000 * 4)

    def drop_pill(self):
        """
        Move servo to open position (accept pill) and deliver it to common container
        :return: None
        """
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
        """
        Repeat drop_pill action amount of times specified by amount_of_pills param
        :param amount_of_pills: specified amount of pills to be delivered (int)
        :return: None
        """
        for i in range(amount_of_pills):
            self.drop_pill()


######################################
######################################
######################################

class PillController:
    """
    Class that represent whole system of containers.
    """

    def __init__(self, tty_str):
        """
        Initalise pill controller
        :param tty_str: ACM string (for linux) or COM string (for Windows) for Polulu Maestro Controller
        """
        self.servo_controller = maestro.Controller(ttyStr=tty_str)

        self.pills_containers_num = 6
        self.pill_boxes = []
        self.csv_read_write = CSVReadWrite()
       # print(self.csv_read_write.sets)

        self.rotation = self.csv_read_write.sets
        # self.set_pill_rotation()

        for i in range(self.pills_containers_num):
            self.pill_boxes.append(PillBox(self.servo_controller, i))

        self.set_capacities()

    def drop_pills(self, drop_list_or_dict):
        """
        Drop set of pills from different containers specified by drop_list_or_dict
        :param drop_list_or_dict: index represents container (Pill Box) and ints value amount of pills from this container.
        :return:
        """
        for i in range(self.pills_containers_num):
            print(drop_list_or_dict[i],type(drop_list_or_dict[i]),drop_list_or_dict)
            self.pill_boxes[i].drop_more_pills(drop_list_or_dict[i])
            self.csv_read_write.pills[i] -= drop_list_or_dict[i]

    def set_capacities(self):
        capacity_list = self.csv_read_write.pills
        for i in range(self.pills_containers_num):
            self.pill_boxes[i].capacity = capacity_list[i]
    #
    # def set_pill_rotation(self):
    #     self.rotation = self.csv_read_write.read_set_of_pills()


if __name__ == '__main__':
    pass
    #pill_controler = PillController("COM5")


    # while True:
    #     for day in days:
    #         current_time.d = day
    #         for hour in range(24):
    #             current_time.h = hour
    #             if current_time.h < 10:
    #                 hour_string = f"0{current_time.h}"
    #             else:
    #                 hour_string = f"{current_time.h}"
    #
    #             for minute in range(60):
    #                 current_time.m = minute
    #
    #                 if current_time.m < 10:
    #                     minute_string = f"0{current_time.m}"
    #                 else:
    #                     minute_string = f"{current_time.m}"
    #
    #                 current_time_string = f"{current_time.d} " + hour_string + minute_string
    #
    #                 if current_time_string in pill_controler.rotation.keys():
    #                     print(pill_controler.rotation[current_time_string])
    #                     pill_controler.drop_pills(pill_controler.rotation[current_time_string])
    #
    #                 sleep(time_speed)
