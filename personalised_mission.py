from base_functions_and_constants import *

def pers_miss():

    P = decibel(float(input("Transmitter power [W] = ")),1)                             #Power in dBW

    L_l = decibel(float(input("Loss factor transmitter = ")),1)                         #Transmitter antenna loss factor in dB

    f_down = float(input("Downlink frequency [GHz] = "))*10**(9)                        #Downlink frequency in Hz
    D_sc = float(input("Antenna diameter spacecraft [m] = "))                           #Spacecraft antenna diameter in m
    eff_sc = float(input("Spacecraft antenna efficiency (estimated) = "))               #Assumed spacecraft antenna efficiency
    G_t = decibel(float(pi*pi*D_sc*D_sc*eff_sc*f_down*f_down/(c*c)),1)                  #Transmitter antenna gain in dB

    L_a = decibel(float(input("Transmission path loss (estimated) = ")),1)              #Transmission path loss in dB

    D_gr = float(input("Antenna diameter ground [m] = "))                               #Ground antenna diameter in m
    eff_gr = float(input("Ground antenna efficiency (estimated) = "))                   #Assumed spacecraft antenna efficiency
    G_r = decibel(float(pi*pi*D_gr*D_gr*eff_gr*f_down*f_down/(c*c)),1)                  #Transmitter antenna gain in dB

    h = float(input("Orbit altutide (from Earth) [km] = "))*1000                        #Orbit altitude in m
    S = sqrt((Re+h)**2-Re**2)                                                           #Worst-case distance to ground station
    L_s = decibel((c/(f_down*4*pi*S))**2,1)                                             #Space loss in dB

    e_t = float(input("Pointing offset (spacecraft) [deg] = "))                         #Spacecraft pointing offset angle in deg
    L_pr = float(-12*(e_t*(f_down/10**9)*D_sc/21)**2)                                   #Spacecraft antenna pointing loss in dB

    L_r = decibel(float(input("Loss factor receiver = ")),1)                            #Loss factor receiver in dB

    if f_down/(10**9) <= 12 and f_down/(10**9) >= 2:
        T_s = decibel(135,1)
    if f_down/(10**9) < 2:
        T_s = decibel(135,1)
    if f_down/(10**9) > 12:
        T_s = decibel(424,1)                                                            #System temperature in dBK

    sw_angle = float(input("Swath width angle [deg] = "))*pi/180                        #Swath width angle in rad
    payload_pix_size = float(input("Payload pixel size [deg] = "))*pi/180               #Payload pixes size in rad
    payload_bits_per_pix = float(input("Payload bits per pixel = "))                    #Payload bits per pixel
    pixel_line_depth = 2*tan(payload_pix_size/2)*h                                      #Pixel line depth
    b_l = sw_angle/payload_pix_size*payload_bits_per_pix                                #Number of bits per line
    V_g = sqrt(mu/(Re+h))*Re/(Re+h)                                                     #Ground speed in m/s
    D_r = b_l*V_g/pixel_line_depth                                                      #Generated data rate
    D_c = float(input("Duty cycle [%] = "))/100                                         #Spacecraft duty cycle
    T_down = float(input("Downlink time [hrs/day] = "))/24                              #Spacecraft downlink time in sec
    R = decibel(D_r*D_c/T_down,1)                                                       #Data rate in dB(bit/s)

    k_ = decibel(float(k),1)                                                            #Bolztmann constant in dB(J/K)

    L_i = 2                                                                             #Implementation losses in dB

    return [P, L_l, G_t, L_a, G_r, L_s, L_pr, L_r, -T_s, -R, -k_, -L_i]
