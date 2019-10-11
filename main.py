from personalised_mission import *
from Earth3U_CubeSat_mission import *
from Moon12U_CubeSat_mission import *
from Mars6U_CubeSat_mission import *
from Venus_explorer_mission import *
from Europa_imager import *

# Mission choice
quest = str(input("Choose mission: \n"
              "1. Earth 3U CubeSat \n"
              "2. Moon 12U CubeSat \n"
              "3. Mars 6U CubeSat \n"
              "4. Venus explorer \n"
              "5. Europa imager \n"
              "6. Personalised mission \n"
              "Mission number:"))
print()

#Inputs for downlink
if quest == "1":
    SNR_values = Earth3U_CubeSat()

if quest == "2":
    SNR_values = Moon12U_CubeSat()

if quest == "3":
    SNR_values = Mars6U_CubeSat()

if quest == "4":
    SNR_values = Venus_explorer()

if quest == "5":
    SNR_values = Europa_imager()

if quest == "6":
    SNR_values = pers_miss()



#Signal to noise ratio for downlink
SNR = sum(SNR_values)
print()
print("Downlink SNR in [dB]", round(SNR,5))
SNR = val(SNR,1)
print("Downlink SNR in [units]", round(SNR,5))

