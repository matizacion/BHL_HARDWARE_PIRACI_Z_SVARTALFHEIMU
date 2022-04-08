import maestro
from time import sleep


class PillBox:
    def __init__(self, controller, servo_no, wait_time = 1):
        self.controller = controller
        self.servo_no = servo_no

        self.wait_time = wait_time

        self.zero()

    def zero(self):
        self.controller.setTarget(self.servo_no, 1000 * 4)

    def drop_pill(self):
        self.controller.setTarget(self.servo_no, 3000 * 4)
        sleep(self.wait_time)
        self.controller.setTarget(self.servo_no, 1000 * 4)
        sleep(self.wait_time)

    def drop_more_pills(self, amount_of_pills):
        for i in range(amount_of_pills):
            self.drop_pill()


class PillController:
    def __init__(self, tty_str):
        self.servo_controller = maestro.Controller(ttyStr=tty_str)

        self.pills_containers_num = 6
        self.pill_boxes = []

        for i in range(self.pills_containers_num):
            self.pill_boxes.append(PillBox(self.servo_controller, i))

    def drop_pills(self, drop_list_or_dict):
        for i in range(self.pills_containers_num):
            self.pill_boxes[i].drop_more_pills(drop_list_or_dict[i])


