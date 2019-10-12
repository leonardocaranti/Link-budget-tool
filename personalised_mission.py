from base_functions_and_constants import *

def pers_miss():

    P_down = decibel(float(input("Spacecraft transmitter power [W] = ")),1)             #Power in dBW for downlink
    P_up = decibel(float(input("Ground station transmitter power [W] = ")),1)           #Power in dBW for uplink

    L_l = decibel(float(input("Loss factor transmitter = ")),1)                         #Transmitter antenna loss factor in dB

    f_down = float(input("Downlink frequency [GHz] = "))*10**(9)                        #Downlink frequency in Hz
    turn_around_ratio = float(input("Turn around ratio (as decimal) ="))
    f_up = turn_around_ratio*f_down                                                     #Uplink frequency in Hz
    D_sc = float(input("Antenna diameter spacecraft [m] = "))                           #Spacecraft antenna diameter in m
    eff_sc = float(input("Spacecraft antenna efficiency (estimated) = "))               #Assumed spacecraft antenna efficiency
    G_t_down = decibel(pi*pi*D_sc*D_sc*eff_sc*f_down*f_down/(c*c), 1)                   #Transmitter antenna gain in dB for downlink
    G_r_up = decibel(pi*pi*D_sc*D_sc*eff_sc*f_up*f_up/(c*c), 1)                         #Transmitter antenna gain in dB for uplink

    L_a = decibel(float(input("Transmission path loss (estimated) = ")),1)              #Transmission path loss in dB

    D_gr = float(input("Antenna diameter ground [m] = "))                               #Ground antenna diameter in m
    eff_gr = float(input("Ground antenna efficiency (estimated) = "))                   #Assumed spacecraft antenna efficiency
    G_r_down = decibel(pi*pi *D_gr*D_gr * eff_gr* f_down*f_down / (c*c), 1)             #Transmitter antenna gain in dB for downlink
    G_t_up = decibel(pi*pi *D_gr*D_gr * eff_gr* f_up*f_up / (c*c), 1)                   #Transmitter antenna gain in dB for uplink

    mission_loc = str(input("Mission locations available: \n"
                        "1. Earth \n"
                        "2. Moon \n"
                        "3. Mars \n"
                        "4. Venus \n"
                        "5. Europa \n"
                        "Enter mission location number: "))

    h_planet = float(input("Orbit altutide [km] = ")) * 1000                            # Orbit altitude in m
    if mission_loc == "1":
        h, mu, R_= h_planet, mu_earth, Re
    elif mission_loc == "2":
        h, mu, R_ = min_dist_moon_earth-h_planet, mu_moon, Rmoon
    elif mission_loc == "3":
        e_angle = float(input("Minimum elongation angle [deg] ="))*pi/180
        h, mu, R_ = sqrt(1+dist_mars_sun*dist_mars_sun-2*dist_mars_sun*cos(e_angle))*AU-h_planet, mu_mars, Rmars
    elif mission_loc == "4":
        e_angle = float(input("Minimum elongation angle [deg] =")) * pi / 180
        h, mu, R_ = sqrt(1+dist_venus_sun*dist_venus_sun-2*dist_venus_sun*cos(e_angle))*AU-h_planet, mu_venus, Rvenus
    elif mission_loc == "5":
        e_angle = float(input("Minimum elongation angle [deg] =")) * pi / 180
        h, mu, R_ = sqrt(1+dist_europa_sun*dist_europa_sun-2*dist_europa_sun*cos(e_angle))*AU-h_planet, mu_europa, Reuropa

    S = sqrt((R_+h)**2-R_**2)                                                           #Worst-case distance to ground station
    L_s_down = decibel((c / (f_down * 4 * pi * S)) ** 2, 1)                             # Space loss in dB for downlink
    L_s_up = decibel((c / (f_up * 4 * pi * S)) ** 2, 1)                                 # Space loss in dB for uplink

    e_t = float(input("Pointing offset (spacecraft) [deg] = "))                         #Spacecraft pointing offset angle in deg
    L_pr_down = -12 * (e_t * (f_down / 10 ** 9) * D_sc / 21) ** 2                       # Spacecraft antenna pointing loss in dB for downlink
    L_pr_up = -12 * (e_t * (f_up / 10 ** 9) * D_gr / 21) ** 2                           # Spacecraft antenna pointing loss in dB for uplink

    L_r = decibel(float(input("Loss factor receiver = ")),1)                            #Loss factor receiver in dB

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

    sw_angle = float(input("Swath width angle [deg] = "))*pi/180                        #Swath width angle in rad
    payload_pix_size = float(input("Payload pixel size [deg] = "))*pi/180               #Payload pixes size in rad
    payload_bits_per_pix = float(input("Payload bits per pixel = "))                    #Payload bits per pixel
    pixel_line_depth = 2*tan(payload_pix_size/2)*h_planet                               #Pixel line depth
    Sw = 2 * tan(sw_angle / 2) * h_planet
    V_g = sqrt(mu / (R_ + h_planet)) * R_ / (R_ + h_planet)                             #Ground speed in m/s
    D_r = Sw * V_g * payload_bits_per_pix/ (pixel_line_depth*pixel_line_depth)          #Generated data rate
    D_c = float(input("Duty cycle [%] = "))/100                                         #Spacecraft duty cycle
    T_down = float(input("Downlink time [hrs/day] = "))/24                              #Spacecraft downlink time in sec
    R_down = decibel(D_r * D_c / T_down, 1)                                             #Data rate in dB(bit/s) for downlink
    R_up = decibel(float(input("Required uplink data rate [bit/s] =")),1)               #Data rate in dB(bit/s) for uplink

    k_ = decibel(float(k),1)                                                            #Bolztmann constant in dB(J/K)

    L_i = 0                                                                             #Implementation losses in dB

    return [P_down, L_l, G_t_down, L_a, G_r_down, L_s_down, L_pr_down, L_r, -T_s_down, -R_down, -k_, -L_i], \
           [P_up, L_l, G_t_up, L_a, G_r_up, L_s_up, L_pr_up, L_r, -T_s_up, -R_up, -k_, -L_i]
