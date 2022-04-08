from pillcontroler import PillControler
from maestro import Controller

if __name__ == '__main__':
    pc = PillControler(tty_str='COM5')
    pc.take_pill(1)
    # con = Controller('COM5')
    # print("start")
    # con.setTarget(1, 1500)
