from pillcontroler import PillControler

if __name__ == '__main__':
    pc = PillControler(tty_str='COM5')
    pc.take_pill()
