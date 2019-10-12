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


#Inputs 
if quest == "1":
    SNR_values_down, SNR_values_up = Earth3U_CubeSat()

if quest == "2":
    SNR_values_down, SNR_values_up = Moon12U_CubeSat()

if quest == "3":
    SNR_values_down, SNR_values_up = Mars6U_CubeSat()

if quest == "4":
    SNR_values_down, SNR_values_up = Venus_explorer()

if quest == "5":
    SNR_values_down, SNR_values_up = Europa_imager()

if quest == "6":
    SNR_values_down, SNR_values_up = pers_miss()


#Signal to noise ratios
SNR_down, SNR_up = sum(SNR_values_down), sum(SNR_values_up)
SNR_down_units, SNR_up_units = val(SNR_down,1), val(SNR_up,1)

print()
print("Downlink SNR in [dB]", round(SNR_down,5))
print("Uplink SNR in [dB]", round(SNR_up,5))
print("Downlink SNR in [units]", round(SNR_down_units,5))
print("Uplink SNR in [units]", round(SNR_up_units,5))
