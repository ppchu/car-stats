import json
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#with open('downtown-crosstown-short.json') as f:
#    for line in f:
#        if json.loads(line)

# make an array for every measurement type
# TODO 2D array better?
accel_pos = []
eng_spd = []
veh_spd = []
torque = []
fuel_use = []
odometer = []
gears_str = []
gears_num = []


# add values and time_stamp to corresponding array
with open("downtown-crosstown.json") as f:
    for line in f:
        data = json.loads(line)
        if data["name"] == "accelerator_pedal_position":
            accel_pos.append([data["timestamp"], data["value"]])
        elif data["name"] == "engine_speed":
            eng_spd.append([data["timestamp"], data["value"]])
        elif data["name"] == "vehicle_speed":
            veh_spd.append([data["timestamp"], data["value"]])
        elif data["name"] == "torque_at_transmission":
            torque.append([data["timestamp"], data["value"]])
        elif data["name"] == "fuel_consumed_since_restart":
            fuel_use.append([data["timestamp"], data["value"]])
        elif data["name"] == "odometer":
            odometer.append([data["timestamp"], data["value"]])
        elif data["name"] == "transmission_gear_position":
            gears_str.append(data["value"])
            

np_accel_pos = np.array(accel_pos)
np_eng_spd = np.array(eng_spd)
np_veh_spd = np.array(veh_spd)
np_torque = np.array(torque)
np_fuel_use = np.array(fuel_use)
np_odometer = np.array(odometer)

for x in gears_str:
    if x == "neutral":
        gears_num.append(0)
    if x == "first":
        gears_num.append(1)
    if x == "second":
        gears_num.append(2)
    if x == "third":
        gears_num.append(3)
    if x == "fourth":
        gears_num.append(4)
    if x == "fifth":
        gears_num.append(5)
    if x == "sixth":
        gears_num.append(6)

#print np_veh_spd.shape
plt.figure(1)
plt.plot(np_veh_spd[:,0], np_veh_spd[:,1])
plt.figure(2)
plt.plot(np_eng_spd[:,0], np_eng_spd[:,1])
plt.figure(3)
plt.hist(gears_num)
plt.show()

#print(type(data))

#print(data["name"])

# numpy 2D array
# array per name
# array dimesions are [value, time], both of type float
# 
# ex:
# vehicle_speed
# array([value, time],
#       [value, time],
#       ...,
#       [value, time])
#
# loop into dictionary then turn into array
# pandas!!!
