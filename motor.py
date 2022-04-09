import RPi.GPIO as GPIO
import time

class Motor:
    
    def __init__(self,motor_pin_1,motor_pin_2,AIN_1,AIN_2,BIN_1,BIN_2,LED,time_1=5,time_2=1,pwm=80):
        self.motor_pin_1_=motor_pin_1
        self.motor_pin_2_=motor_pin_2
        self.AIN_1_=AIN_1
        self.AIN_2_=AIN_2
        self.BIN_1_=BIN_1
        self.BIN_2_=BIN_2
        self.LED_=LED
        self.time_1_=time_1
        self.time_2_=time_2
        self.pwm_=pwm
        
        self.setup()

    def setup(self):
    
        GPIO.setmode(GPIO.BOARD)
    
        GPIO.setup(self.AIN_1_, GPIO.OUT)
        GPIO.setup(self.AIN_2_, GPIO.OUT)
        GPIO.setup(self.motor_pin_1_, GPIO.OUT)
    
        GPIO.setup(self.BIN_1_, GPIO.OUT)
        GPIO.setup(self.BIN_2_, GPIO.OUT)
        GPIO.setup(self.motor_pin_2_, GPIO.OUT)
    
        GPIO.setup(self.LED_, GPIO.OUT)
        GPIO.output(self.LED_,GPIO.LOW)
        
        GPIO.output(self.AIN_1_, GPIO.HIGH)
        GPIO.output(self.AIN_2_, GPIO.LOW)
        GPIO.output(self.motor_pin_1_, GPIO.LOW)
        
        
        self.pwm_1=GPIO.PWM(self.motor_pin_1_, 1000)
        self.pwm_1.start(0)
        
        GPIO.output(self.BIN_1_, GPIO.HIGH)
        GPIO.output(self.BIN_2_, GPIO.LOW)
        GPIO.output(self.motor_pin_2_, GPIO.LOW)
        
        self.pwm_2=GPIO.PWM(self.motor_pin_2_, 1000)
        self.pwm_2.start(0)
        
    def go(self):
        
        self.pwm_1.ChangeDutyCycle(self.pwm_)
        self.pwm_2.ChangeDutyCycle(self.pwm_)
        
        time.sleep(self.time_1_)
        self.pwm_1.stop()
        self.pwm_2.stop()
        
        GPIO.output(self.LED_,GPIO.HIGH)
        
        time.sleep(self.time_2_)
        
        GPIO.output(self.LED_,GPIO.LOW)
        
        GPIO.cleanup()
    
     
if  __name__ == '__main__':
    motor_pin_1 = 32
    AIN_1=38
    AIN_2=40
    motor_pin_2 = 33
    BIN_1=35
    BIN_2=37
    LED=11
    motor=Motor(motor_pin_1,motor_pin_2,AIN_1,AIN_2,BIN_1,BIN_2,LED)
    motor.go()