from pillcontroler import PillController
from maestro import Controller

if __name__ == '__main__':
    pc = PillController(tty_str='COM5')

    pc.pill_boxes[5].drop_pill()
    # con = Controller('COM5')
    # print("start")
    # con.setTarget(1, 1500)
