from utime import localtime
from time import sleep
from machine import ADC

def GetTime():
    currentTime = localtime()
    hour = currentTime[3]
    minute = currentTime[4]
    second = currentTime[5]
    hourStr = ""
    minuteStr = ""
    secondStr = ""
    if len(str(hour)) == 1:
        hourStr = "0" + str(hour)
    else:
        hourStr = str(hour)
    if len(str(minute)) == 1:
        minuteStr = "0" + str(minute)
    else:
        minuteStr = str(minute)
    if len(str(second)) == 1:
        secondStr = "0" + str(second)
    else:
        secondStr = str(second)
    return hourStr + ":" + minuteStr + ":" + secondStr

def GetDate():
    currentTime = localtime()
    return str(currentTime[2]) + "/" + str(currentTime[1]) + "/" + str(currentTime[0])

def GetTemperature():
    adc = ADC(4)
    ADCVoltage = adc.read_u16() * (3.3 / (65535))
    tempC = 27 - (ADCVoltage - 0.706) / 0.001721
    return tempC

with open("results.txt", "w") as f:
    beginRecStr = "Temperature Readings  | Recorded on " + GetDate()
    print(beginRecStr)
    f.write(beginRecStr + "\n")
    for i in range(10):
        outputStr = "Reading " + str(i + 1) + ": " + str(GetTemperature()) + " C | Recorded at " + GetTime()
        print(outputStr)
        f.write(outputStr + "\n")
        sleep(1)
