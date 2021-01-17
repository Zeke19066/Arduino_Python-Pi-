
from pyfirmata2 import Arduino
import time

PORT = Arduino.AUTODETECT
# PORT = '/dev/ttyACM0'
# prints data on the screen at the sampling rate of 50Hz
# can easily be changed to saving data to a file
# It uses a callback operation so that timing is precise and
# the main program can just go to sleep.

PINS = [2,3,4,5,6,7,] #list power pins

class AnalogPrinter:

    def __init__(self):
        self.samplingRate = 2 #sampling frequency in Hz
        self.timestamp = 0
        self.board = Arduino(PORT)

    def start(self):
        for PIN in PINS:
            self.board.digital[PIN].write(1)  # Set the LED pin to 1 (HIGH)
        time.sleep(.5)
        self.board.analog[1].register_callback(self.S1PrintCallback)
        self.board.analog[2].register_callback(self.S2PrintCallback)
        self.board.analog[3].register_callback(self.S3PrintCallback)
        self.board.analog[4].register_callback(self.S4PrintCallback)
        self.board.analog[5].register_callback(self.S5PrintCallback)
        #self.board.analog[6].register_callback(self.S6PrintCallback)

        self.board.samplingOn(1000 / self.samplingRate)
        self.board.analog[1].enable_reporting()
        self.board.analog[2].enable_reporting()
        self.board.analog[3].enable_reporting()
        self.board.analog[4].enable_reporting()
        self.board.analog[5].enable_reporting()
        #self.board.analog[6].enable_reporting()

    def S1PrintCallback(self, data):
        rounded_data = int(data * 1000)
        readout1.append(rounded_data)
        print(f"{self.timestamp}")
        self.timestamp += (1 / self.samplingRate)
    
    def S2PrintCallback(self, data):
        rounded_data2 = int(data * 1000)
        readout2.append(rounded_data2)

    def S3PrintCallback(self, data):
        rounded_data3 = int(data * 1000)
        readout3.append(rounded_data3)

    def S4PrintCallback(self, data):
        rounded_data4 = int(data * 1000)
        readout4.append(rounded_data4)

    def S5PrintCallback(self, data):
        rounded_data5 = int(data * 1000)
        readout5.append(rounded_data5)
    
    #def S6PrintCallback(self, data):
    #    rounded_data6 = int(data * 1000)
    #    readout6.append(rounded_data6)
    #    print(f"{rounded_data6}")

    def stop(self):
        self.board.samplingOff()
        for PIN in PINS:
            self.board.digital[PIN].write(0)  # Set the LED pin to 0 (LOW)
        self.board.exit()

"""
class Timer:
    def __init__(self):
        self._start_time = None

    def start(self):
        self._start_time = time.perf_counter()
        print("Start")
        return

    def stop(self):
        elapsed_time = time.perf_counter() - self._start_time
        if elapsed_time > 10:
            self._start_time = None
            AnalogPrinter.stop()# let's stop it
            print("Done")
        return
"""

def map(x):
    result = ((x-1028)*(100-0)/(430-1028) + 0)
    return result

def average(input_readout):
    avg = sum(input_readout)/len(input_readout)
    return avg

readout1 = []
readout2 = []
readout3 = []
readout4 = []
readout5 = []
readout6 = []

#print("Begin Analog Readout")

def update_values():
    analogPrinter = AnalogPrinter()# Let's create an instance
    analogPrinter.start()# begin
    time.sleep(2)# let's acquire data for 10secs. We could do something else but we just sleep!
    analogPrinter.stop()# let's stop it
    print(f"Average 1 = {average(readout1)}  {int(map(average(readout1)))}%")
    print(f"Average 2 = {average(readout2)}  {int(map(average(readout2)))}%")
    print(f"Average 3 = {average(readout3)}  {int(map(average(readout3)))}%")
    print(f"Average 4 = {average(readout4)}  {int(map(average(readout4)))}%")
    print(f"Average 5 = {average(readout5)}  {int(map(average(readout5)))}%")



"""
Timer = Timer()# Let's create an instance
Timer.start()
analogPrinter.start()# and start DAQ
Timer.stop()
"""
analogPrinter = AnalogPrinter()# Let's create an instance
analogPrinter.start()# begin
time.sleep(2)# let's acquire data for 10secs. We could do something else but we just sleep!
analogPrinter.stop()# let's stop it
print(f"Average 1 = {average(readout1)}  {int(map(average(readout1)))}%")
print(f"Average 2 = {average(readout2)}  {int(map(average(readout2)))}%")
print(f"Average 3 = {average(readout3)}  {int(map(average(readout3)))}%")
print(f"Average 4 = {average(readout4)}  {int(map(average(readout4)))}%")
print(f"Average 5 = {average(readout5)}  {int(map(average(readout5)))}%")

"""
for PIN in PINS:
    print(f"Average {PIN-1} = {average(readout1)}")
    #del readout1
"""