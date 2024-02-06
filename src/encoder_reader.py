
class Encoder:
    """"""
    def __init__(self, pinA, pinB, timer, chan_A, chan_B):
        self.pinA = pinA
        self.pinB = pinB
        self.timer = timer
        self.chan_A = chan_A
        self.chan_B = chan_B
        self.position = 0
    
    def read(self):
        
        ######
        return self.timer.counter()
    
    def zero(self):
        
        return self.timer.counter()
        

if __name__ == "__main__":
    
    import utime
    pinA = pyb.Pin(pyb.Pin.board.PB6, pyb.Pin.AF_PP, pull=pyb.Pin.PULL_NONE, af=pyb.Pin.AF1_TIM2)
    pinB = pyb.Pin(pyb.Pin.board.PB7, pyb.Pin.AF_PP, pull=pyb.Pin.PULL_NONE, af=pyb.Pin.AF1_TIM2)

    timer = pyb.Timer(4, prescaler=1, period=100000)
    chan_A = timer.channel(1, pyb.Timer.ENC_AB, pin=pinA)
    chan_B = timer.channel(2, pyb.Timer.ENC_AB, pin=pinB)
    
    enc1 = Encoder(pinA, pinB, timer, chan_A, chan_B)
    
    pinA_2 = pyb.Pin(pyb.Pin.board.PC6, pyb.Pin.AF_PP, pull=pyb.Pin.PULL_NONE, af=pyb.Pin.AF1_TIM2)
    pinB_2 = pyb.Pin(pyb.Pin.board.PC7, pyb.Pin.AF_PP, pull=pyb.Pin.PULL_NONE, af=pyb.Pin.AF1_TIM2)

    timer_2 = pyb.Timer(8, prescaler=1, period=100000)
    chan_A_2 = timer_2.channel(1, pyb.Timer.ENC_AB, pin=pinA_2)
    chan_B_2 = timer_2.channel(2, pyb.Timer.ENC_AB, pin=pinB_2)
    
    enc2 = Encoder(pinA_2, pinB_2, timer_2, chan_A_2, chan_B_2)
    
    while True:
        print(enc2.read())
        utime.sleep(0.2)
        
    
    
    