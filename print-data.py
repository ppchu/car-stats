import json
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# s to hold data
accel_pos = []
ignition = []
headlamp = []
fuel_use = []
windshield_wiper = []
door = []
torque = []
longitude = []
odometer = []
veh_spd = []
brake_status = []
latitude = []
fuel_level = []
eng_spd = []
button = []
steering_angle = []

# dictionary with data_name as key and s as value
# TODO eventually put into for line
data_dict = {"accelerator_pedal_position": [],
             "ignition_status": [],
             "headlamp_status": [],
             "fuel_consumed_since_restart": [],
             "windshield_wiper_status": [],
             "door_status": [],
             "torque_at_transmission": [],
             "longitude": [],
             "odometer": [],
             "vehicle_speed": [],
             "transmission_gear_position": [],
             "brake_pedal_status": [],
             "latitude": [],
             "fuel_level": [],
             "engine_speed": [],
             "button_state": [],
             "steering_wheel_angle": []}
    

# add values and time_stamp to corresponding array
with open("downtown-crosstown.json") as f:
    for line in f:
        data = json.loads(line)
        data_dict[data["name"]].append([data["timestamp"], data["value"]])

np_accel_pos = np.array(data_dict["accelerator_pedal_position"])
np_eng_spd = np.array(data_dict["engine_speed"])
np_veh_spd = np.array(data_dict["vehicle_speed"])
np_torque = np.array(data_dict["torque_at_transmission"])
np_fuel_use = np.array(data_dict["fuel_consumed_since_restart"])
np_odometer = np.array(data_dict["odometer"])

# calculate time spent in each gear
gear_times = {}
gears = data_dict["transmission_gear_position"]

for gear_i in xrange(len(gears)):
    
    key = gears[gear_i][1]
    value = gear_times.setdefault(key)
    
    if  value != None:
        # key in dictionary
        if gear_i + 1 < len(gears):
            # there is another gear change
            added_time = gears[gear_i + 1][0] - gears[gear_i][0]
            value += added_time
            #print "added " + str(added_time) + " to " + key
        else:
            # no more gear change, take the last data timestamp
            value += data["timestamp"] - gears[gear_i][0]
    else:
        # key not in dictionary
        if gear_i + 1 < len(gears):
            # there is another gear change
            value = gears[gear_i + 1][0] - gears[gear_i][0]
            #print "first segment of " + key + " gear is " + str(value)
        else:
            # no more gear change, take the last data timestamp
            value = data["timestamp"] - gears[gear_i][0]

    gear_times[key] = value

#print gear_times
total_gear_time = sum(gear_times.values())
gear_percentage = []
gear_percentage.append(gear_times["neutral"] / total_gear_time)
gear_percentage.append(gear_times["first"] / total_gear_time)
gear_percentage.append(gear_times["second"] / total_gear_time)
gear_percentage.append(gear_times["third"] / total_gear_time)
gear_percentage.append(gear_times["fourth"] / total_gear_time)
gear_percentage.append(gear_times["fifth"] / total_gear_time)
gear_percentage.append(gear_times["sixth"] / total_gear_time)

print "neutral gear % = " + str(gear_times["neutral"] / total_gear_time)
print "first gear % = " + str(gear_times["first"] / total_gear_time)
print "second gear % = " + str(gear_times["second"] / total_gear_time)
print "third gear % = " + str(gear_times["third"] / total_gear_time)
print "fourth gear % = " + str(gear_times["fourth"] / total_gear_time)
print "fifth gear % = " + str(gear_times["fifth"] / total_gear_time)
print "sixth gear % = " + str(gear_times["sixth"] / total_gear_time)

# figure 1 - vehicle speed
plt.figure(1)
plt.plot(np_veh_spd[:,0], np_veh_spd[:,1])

# figure 2 - engine speed
plt.figure(2)
plt.plot(np_eng_spd[:,0], np_eng_spd[:,1])

# figure 3 - accelerator pedal %
plt.figure(3)
plt.plot(np_accel_pos[:,0], np_accel_pos[:,1])

# figure 4 - fuel consumed since start
plt.figure(4)
plt.plot(np_fuel_use[:,0], np_fuel_use[:,1])

# figure 5 - torque
plt.figure(5)
plt.plot(np_torque[:,0], np_torque[:,1])

# figure 6 - odometer
plt.figure(6)
plt.plot(np_odometer[:,0], np_odometer[:,1])

# figure 7 - gear time percentage
plt.figure(7)
plt.bar(range(len(gear_times)), gear_percentage)

#plt.figure(3)
#plt.hist(gears_num)
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
