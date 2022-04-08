import RPi.GPIO as GPIO
import time

motor_pin_1 = 32
AIN_1=38
AIN_2=40
motor_pin_2 = 33
BIN_1=35
BIN_2=37

def setup():
    global pwm_1
    global pwm_2
    
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(AIN_1, GPIO.OUT)
    GPIO.setup(AIN_2, GPIO.OUT)
    GPIO.setup(motor_pin_1, GPIO.OUT)
    
    GPIO.setup(BIN_1, GPIO.OUT)
    GPIO.setup(BIN_2, GPIO.OUT)
    GPIO.setup(motor_pin_2, GPIO.OUT)
    
    GPIO.output(AIN_1, GPIO.LOW)
    GPIO.output(AIN_2, GPIO.HIGH)
    GPIO.output(motor_pin_1, GPIO.LOW)
    pwm_1=GPIO.PWM(motor_pin_1, 1000)
    pwm_1.start(0)
    
    GPIO.output(BIN_1, GPIO.LOW)
    GPIO.output(BIN_2, GPIO.HIGH)
    GPIO.output(motor_pin_2, GPIO.LOW)
    pwm_2=GPIO.PWM(motor_pin_2, 1000)
    pwm_2.start(0)
    pwm_1.ChangeDutyCycle(80)
    pwm_2.ChangeDutyCycle(80)
    time.sleep(5)
    
    
def loop():
    pass

def destroy():
    pwm_1.stop()
    GPIO.output(motor_pin_1, GPIO.LOW)
    pwm_2.stop()
    GPIO.output(motor_pin_2, GPIO.LOW)
    GPIO.cleanup()
     
if  __name__ == '__main__':
    setup()
    try:
        loop()
    except KeyboardInterrupt:
        destroy()