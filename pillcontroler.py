import maestro
from time import sleep


class PillControler:
    def __init__(self, tty_str):
        self.servo_controller = maestro.Controller(ttyStr=tty_str)

        self.pills_containers_num = 6

        # zerowanie
        for i in range(6):
            self.servo_controller.setTarget(i, 1000*4)

    def take_pill(self, pill_type_no):
        self.servo_controller.setTarget(pill_type_no, 3000*4)
        sleep(1)
        self.servo_controller.setTarget(pill_type_no, 1000*4)
