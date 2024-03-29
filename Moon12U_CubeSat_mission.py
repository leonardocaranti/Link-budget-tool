from base_functions_and_constants import *


def Moon12U_CubeSat():
    P_down = decibel(8, 1)                                                              #Power in dBW for downlink
    P_up = decibel(400,1)                                                               #Power in dBW for uplink

    L_l = decibel(0.8, 1)                                                               #Transmitter antenna loss factor in dB

    f_down = 2.2 * 10 ** (9)                                                            #Downlink frequency in Hz
    turn_around_ratio = 221/240
    f_up = turn_around_ratio*f_down                                                     #Uplink frequency in Hz
    D_sc = 0.3                                                                          #Spacecraft antenna diameter in m
    eff_sc = 0.55                                                                       #Assumed spacecraft antenna efficiency
    G_t_down = decibel(pi*pi*D_sc*D_sc*eff_sc*f_down*f_down/(c*c), 1)                   #Transmitter antenna gain in dB for downlink
    G_r_up = decibel(pi*pi*D_sc*D_sc*eff_sc*f_up*f_up/(c*c), 1)                         #Transmitter antenna gain in dB for uplink

    print("Transmission frequency =", f_down/(10**9), "[GHz]")
    L_a = float(input("Transmission path loss (estimated) [dB] = "))                    #Transmission path loss in dB

    D_gr = 5                                                                            #Ground antenna diameter in m
    eff_gr = 0.55                                                                       #Assumed spacecraft antenna efficiency
    G_r_down = decibel(pi*pi *D_gr*D_gr * eff_gr* f_down*f_down / (c*c), 1)             #Transmitter antenna gain in dB for downlink
    G_t_up = decibel(pi*pi *D_gr*D_gr * eff_gr* f_up*f_up / (c*c), 1)                   #Transmitter antenna gain in dB for uplink

    h_moon = 1000 * 1000                                                                #Orbit altitude in m
    h = min_dist_moon_earth - h_moon
    S = sqrt((Re + h) ** 2 - Re ** 2)                                                   #Worst-case distance to ground station
    L_s_down = decibel((c / (f_down * 4 * pi * S)) ** 2, 1)                             #Space loss in dB for downlink
    L_s_up = decibel((c / (f_up * 4 * pi * S)) ** 2, 1)                                 #Space loss in dB for uplink

    e_t = 1                                                                             #Spacecraft pointing offset angle in deg
    L_pr_down_sc = -12 * (e_t * (f_down / 10 ** 9) * D_sc / 21) ** 2                    #Spacecraft antenna pointing loss in dB for downlink
    L_pr_down_gr = -12 * (0.1) ** 2                                                     #Ground antenna pointing loss in dB for downlink
    L_pr_up_sc = -12 * (e_t * (f_up / 10 ** 9) * D_sc / 21) ** 2                        #Spacecraft antenna pointing loss in dB for uplink
    L_pr_up_gr = -12 * (0.1) ** 2                                                       #Ground antenna pointing loss in dB for uplink

    L_r = decibel(0.7, 1)                                                               #Loss factor receiver in dB

    if f_down / (10 ** 9) <= 12 and f_down / (10 ** 9) >= 1.1:
        T_s_down = decibel(135, 1)
    if f_down / (10 ** 9) < 1.1:
        T_s_down = decibel(221, 1)
    if f_down / (10 ** 9) > 16:
        T_s_down = decibel(424, 1)                                                      #System temperature in dBK for downlink

    if f_up / (10 ** 9) <= 30 and f_up / (10 ** 9) >= 0.2:
        T_s_up = decibel(614, 1)
    if f_up / (10 ** 9) > 30:
        T_s_up = decibel(763, 1)                                                        #System temperature in dBK for uplink

    sw_angle = float(30) * pi / 180                                                     #Swath width angle in rad
    payload_pix_size = float(0.1/60) * pi / 180                                         #Payload pixel size in rad
    payload_bits_per_pix = float(8)                                                     #Payload bits per pixel
    pixel_line_depth = 2 * tan(payload_pix_size / 2) * h_moon                           #Pixel line depth
    Sw = 2 * tan(sw_angle / 2) * h_moon
    V_g = sqrt(mu_moon / (Rmoon + h_moon)) * Rmoon / (Rmoon + h_moon)                   #Ground speed in m/s
    D_r = Sw * V_g * payload_bits_per_pix/ (pixel_line_depth*pixel_line_depth)          #Generated data rate
    D_c = 50 / 100                                                                      #Spacecraft duty cycle
    T_down = 6 / 24                                                                     #Spacecraft downlink time in sec
    R_down = decibel(D_r * D_c / T_down, 1)                                             #Data rate in dB(bit/s) for downlink
    R_up = decibel(1e6,1)                                                               #Data rate in dB(bit/s) for uplink

    k_ = decibel(float(k), 1)                                                           #Bolztmann constant in dB(J/K)

    L_i = 0                                                                             #Implementation losses in dB

    return [P_down, L_l, G_t_down, L_a, G_r_down, L_s_down, L_pr_down_sc + L_pr_down_gr, L_r, -T_s_down, -R_down, -k_,
            -L_i], \
           [P_up, L_l, G_t_up, L_a, G_r_up, L_s_up, L_pr_up_gr + L_pr_up_sc, L_r, -T_s_up, -R_up, -k_, -L_i]
