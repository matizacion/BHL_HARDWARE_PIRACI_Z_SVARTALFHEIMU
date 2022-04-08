import maestro
from time import sleep


class PillControler:
    def __init__(self, tty_str):
        self.servo_controller = maestro.Controller(ttyStr=tty_str)

    def take_pill(self):
        self.servo_controller.setTarget(1, maestro.deg2us(90))
        sleep(1)
        self.servo_controller.setTarget(1, maestro.deg2us(0))
