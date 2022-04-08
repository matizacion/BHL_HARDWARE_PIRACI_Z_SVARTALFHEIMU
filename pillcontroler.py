import maestro
from time import sleep


class PillBox:
    def __init__(self, controller, servo_no):
        self.controller = controller
        self.servo_no = servo_no

        self.zero()

    def zero(self):
        self.controller.setTarget(self.servo_no, 1000 * 4)

    def take_pill(self):
        self.controller.setTarget(self.servo_no, 3000 * 4)
        sleep(1)
        self.controller.setTarget(self.servo_no, 1000 * 4)


class PillController:
    def __init__(self, tty_str):
        self.servo_controller = maestro.Controller(ttyStr=tty_str)

        self.pills_containers_num = 6
        self.pill_boxes = []

        for i in range(self.pills_containers_num):
            self.pill_boxes.append(PillBox(self.servo_controller, i))


