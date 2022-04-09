import RPi.GPIO as GPIO
import time


class Motor:

    def __init__(self, motor_pin_1, motor_pin_2, AIN_1, AIN_2, BIN_1, BIN_2, LED, time_1=5, time_2=1, pwm=80):
        """
        konstruktor klasy motor przyjmujący podstawowe wartości potrzebne do sterowania silnikami
        :param motor_pin_1: int -> numer pinu sterującego pwm1
        :param motor_pin_2: int -> numer pinu sterującego pwm2
        :param AIN_1: int -> numer pinu sterującego pierwszym wejściem dla pierwszego silnika
        :param AIN_2: int -> numer pinu sterującego drugim wejściem dla pierwszego silnika
        :param BIN_1: int -> numer pinu sterującego pierwszym wejściem dla drugiego silnika
        :param BIN_2: int -> numer pinu sterującego drugim wejściem dla drugiego silnika
        :param LED: int -> numer pinu sterującego LED
        :param time_1: int -> czas przez który ma jechać robot w sekundach
        :param time_2: int -> czas przez który ma się świecić LED
        :param pwm: int -> wartość % szerokości PWM
        """
        self.motor_pin_1_ = motor_pin_1
        self.motor_pin_2_ = motor_pin_2
        self.AIN_1_ = AIN_1
        self.AIN_2_ = AIN_2
        self.BIN_1_ = BIN_1
        self.BIN_2_ = BIN_2
        self.LED_ = LED
        self.time_1_ = time_1
        self.time_2_ = time_2
        self.pwm_ = pwm
        self.setup()

    def setup(self):
        """
        Metoda przeprowadzająca konfigurację GPIO Raspberry Pi
        :return: None
        """
        GPIO.setmode(GPIO.BOARD)

        GPIO.setup(self.AIN_1_, GPIO.OUT)
        GPIO.setup(self.AIN_2_, GPIO.OUT)
        GPIO.setup(self.motor_pin_1_, GPIO.OUT)

        GPIO.setup(self.BIN_1_, GPIO.OUT)
        GPIO.setup(self.BIN_2_, GPIO.OUT)
        GPIO.setup(self.motor_pin_2_, GPIO.OUT)

        GPIO.setup(self.LED_, GPIO.OUT)
        GPIO.output(self.LED_, GPIO.LOW)

        GPIO.output(self.AIN_1_, GPIO.HIGH)
        GPIO.output(self.AIN_2_, GPIO.LOW)
        GPIO.output(self.motor_pin_1_, GPIO.LOW)

        self.pwm_1 = GPIO.PWM(self.motor_pin_1_, 1000)
        self.pwm_1.start(0)

        GPIO.output(self.BIN_1_, GPIO.HIGH)
        GPIO.output(self.BIN_2_, GPIO.LOW)
        GPIO.output(self.motor_pin_2_, GPIO.LOW)

        self.pwm_2 = GPIO.PWM(self.motor_pin_2_, 1000)
        self.pwm_2.start(0)

    def go(self):
        """
        metoda odpowiedzialna za jazdę do przodu przez określony czas i zaświecenie diody
        :return: None
        """
        self.pwm_1.ChangeDutyCycle(self.pwm_)
        self.pwm_2.ChangeDutyCycle(self.pwm_)

        time.sleep(self.time_1_)
        self.pwm_1.stop()
        self.pwm_2.stop()

        GPIO.output(self.LED_, GPIO.HIGH)

        time.sleep(self.time_2_)

        GPIO.output(self.LED_, GPIO.LOW)

        GPIO.cleanup()


if __name__ == '__main__':
    motor_pin_1 = 32
    AIN_1 = 38
    AIN_2 = 40
    motor_pin_2 = 33
    BIN_1 = 35
    BIN_2 = 37
    LED = 11
    motor = Motor(motor_pin_1, motor_pin_2, AIN_1, AIN_2, BIN_1, BIN_2, LED)
    motor.go()
