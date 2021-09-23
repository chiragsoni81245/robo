try:
    import RPi.GPIO as gpio
    import time
    from enum import Enum

    class PIROBO:

        def __init__(self):    
            gpio.setmode(gpio.BCM)
            gpio.setup(17, gpio.OUT)
            gpio.setup(22, gpio.OUT)
            gpio.setup(23, gpio.OUT)
            gpio.setup(24, gpio.OUT)
            self.stop()

        
        def send_action(self, action):
            if action.lower()=="up":
                self.forward()
            elif action.lower()=="down":
                self.reverse()
            elif action.lower()=="left":
                self.left_turn()
            elif action.lower()=="right":
                self.right_turn()
            elif action.lower()=="stop":
                self.stop()
            else:
                self.stop()
                return False
            return True

        def stop(self):
            gpio.output(17, False)
            gpio.output(22, False)
            gpio.output(23, False)
            gpio.output(24, False)

        def forward(self):
            gpio.output(17, True)
            gpio.output(22, False)
            gpio.output(23, True)
            gpio.output(24, False)

        def reverse(self):
            gpio.output(17, False)
            gpio.output(22, True)
            gpio.output(23, False)
            gpio.output(24, True)

        def left_turn(self):
            gpio.output(17, True)
            gpio.output(22, False)
            gpio.output(23, False)
            gpio.output(24, False)

        def right_turn(self):
            gpio.output(17, False)
            gpio.output(22, True)
            gpio.output(23, True)
            gpio.output(24, False)

except ModuleNotFoundError:
    
    class PIROBO:

        def __init__(self):
            print("Warning: RPi.GPIO is not present")

        def send_action(self, action):
            return True




