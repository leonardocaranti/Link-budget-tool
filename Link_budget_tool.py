from math import *

def decibel(value,unit):
    value_dB=10*log(value/unit, 10)
    return value_dB

def val(value_dB,unit):
    value=unit*10**(value_dB/10)
    return value

#Constants
Re = 6371*1000   #[m]
k = 1.38e-23     #[J/K]
c = 3e8          #[m/s]


# Inputs
P = decibel(float(input("Transmitter power [W] = ")),1)                             #Power in dBW
L_l = decibel(float(input("Transmitter to antenna loss factor = ")),1)              #Transmitter antenna loss factor in dB
G_t = decibel(float(input("Transmitter antenna gain = ")),1)                        #Transmitter antenna gain in dB
L_a = decibel(float(input("Transmission path loss = ")),1)                          #Transmission path loss in dB
G_r = decibel(float(input("Receiving antenna gain = ")),1)                          #Transmitter antenna gain in dB
L_s = decibel(float(input("Space loss = ")),1)                                      #Space loss in dB
L_pr = decibel(float(input("Antenna pointing loss = ")),1)                          #Antenna pointing loss in dB
L_r = decibel(float(input("Reception feeder loss = ")),1)                           #Reception feeder loss in dB
T_s = decibel(float(input("System temperature [K] = ")),1)                          #System temperature in dBK
R = decibel(float(input("Data rate [bit/s] = ")),1)                                 #Data rate in dB(bit/s)
k_ = decibel(float(k),1)                                                            #Bolztmann constant in dB(J/K)
L_i = 2

#Signal to noise ratio
SNR = P + L_l + G_t + L_a + G_r + L_s + L_pr + L_r - T_s - R - k_ - L_i
print("SNR in [dB]", round(SNR,2))
SNR = val(SNR,1)
print("SNR in [units]", round(SNR,2))

