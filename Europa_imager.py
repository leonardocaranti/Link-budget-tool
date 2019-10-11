from base_functions_and_constants import *

min_dist_europa_earth = 3.93 #[AU]

def Europa_imager():
    P = decibel(150, 1)                                                                 #Power in dBW

    L_l = decibel(0.9, 1)                                                               #Transmitter antenna loss factor in dB

    f_down = 8.4 * 10 ** (9)                                                            #Downlink frequency in Hz
    D_sc = 3                                                                            #Spacecraft antenna diameter in m
    eff_sc = 0.55                                                                       #Assumed spacecraft antenna efficiency
    G_t = decibel(float(pi*pi*D_sc*D_sc*eff_sc*f_down*f_down/(c*c)), 1)                 #Transmitter antenna gain in dB

    L_a = decibel(float(input("Transmission path loss (estimated) = ")), 1)             #Transmission path loss in dB

    D_gr = 70                                                                           #Ground antenna diameter in m
    eff_gr = 0.55                                                                       #Assumed spacecraft antenna efficiency
    G_r = decibel(float(pi * pi * D_gr * D_gr * eff_gr * f_down * f_down / (c * c)),
                  1)                                                                    #Transmitter antenna gain in dB

    h_europa = 500 * 1000                                                               #Orbit altitude in m
    h = min_dist_europa_earth*AU - h_europa
    S = sqrt((Re + h) ** 2 - Re ** 2)                                                   #Worst-case distance to ground station
    L_s = decibel((c / (f_down * 4 * pi * S)) ** 2, 1)                                  #Space loss in dB

    e_t = 0.05                                                                          #Spacecraft pointing offset angle in deg
    L_pr = float(-12 * (e_t * (f_down / 10 ** 9) * D_sc / 21) ** 2)                     #Spacecraft antenna pointing loss in dB

    L_r = decibel(0.7, 1)                                                               #Loss factor receiver in dB

    if f_down / (10 ** 9) <= 12 and f_down / (10 ** 9) >= 2:
        T_s = decibel(135, 1)
    if f_down / (10 ** 9) < 2:
        T_s = decibel(221, 1)
    if f_down / (10 ** 9) > 12:
        T_s = decibel(424, 1)                                                           #System temperature in dBK

    sw_angle = float(45) * pi / 180                                                     #Swath width angle in rad
    payload_pix_size = float(0.01/60) * pi / 180                                        #Payload pixel size in rad
    payload_bits_per_pix = float(8)                                                     #Payload bits per pixel
    pixel_line_depth = 2 * tan(payload_pix_size / 2) * h_europa                         #Pixel line depth
    b_l = sw_angle / payload_pix_size * payload_bits_per_pix                            #Number of bits per line
    V_g = sqrt(mu_europa / (Re + h_europa)) * Reuropa / (Reuropa + h_europa)            #Ground speed in m/s
    D_r = b_l * V_g / pixel_line_depth                                                  #Generated data rate
    D_c = 75 / 100                                                                      #Spacecraft duty cycle
    T_down = 24 / 24                                                                    #Spacecraft downlink time in sec
    R = decibel(D_r * D_c / T_down, 1)                                                  #Data rate in dB(bit/s)

    k_ = decibel(float(k), 1)                                                           #Bolztmann constant in dB(J/K)

    L_i = 0                                                                             #Implementation losses in dB

    return [P, L_l, G_t, L_a, G_r, L_s, L_pr, L_r, -T_s, -R, -k_, -L_i]
