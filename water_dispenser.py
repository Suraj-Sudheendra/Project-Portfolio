# START

#Team 20_DP3_code
#...............................................................................

from sensor_library import *

from gpiozero import LED, Servo, Button 
import time
import sys
import math

#...............................................................................
def water_dispenser(ori_dist,sensor,water_h,counter,servo,blue_led,red_led,r):
    sensor_data=[]
    while ori_dist-(sensor.distance()-50) < water_h: #      -50 is to account for sensor error. if height of water being poured is less than it's calculated height 
        time.sleep(1)
        servo.max() #                               latch opens
        red_led.off() 
        time.sleep(1)
        blue_led.on() #                             water starts pouring 
        print("pouring...")
        for i in range(counter*8): #                value of 8 is num of sec for 1 cup to be filled 
            sensor_data.append(sensor.distance())
        

    time.sleep(1)
    servo.min() #                                       latch closes
    blue_led.off() #                                    water stops pouring 
    red_led.on()
    water_vol = (math.pi*r*r*water_h) #                 calculates volume of water poured
    print("Water poured: ",round(water_vol,3), "mm^3") 
    return sensor_data
#...........................................................................................
def button(user_button,counter):
    while True:
        if user_button.is_pressed == True:
            print("\n","-"*20,"\n") #                           separates our output values 
            counter+=1
            print("Button was pressed: ", counter, "times") #   prints how many times button was pressed
            time.sleep(1)
            water_h = (45*counter) #                            55 is the default value for the height of the cup(s) being poured
            print("The water's height is: ",water_h)
            if counter > 3: #                                   the user can only pour 3 cups of water 
                print("You want to pour too much")
                return counter,water_h
                break #                                         code stops when the user tries to pour more than 3 cups
            
            return counter,water_h       
    
#...........................................................................................

    
def rolling_average(sensor,sensor_data):
    n = 4
    i = 0
    moving_averages = []
    while i < len(sensor_data) - n + 1:
        this_n = sensor_data[i : i + n]
        n_average = sum(this_n) / n
        moving_averages.append(n_average)
        i += 1
        time.sleep(1)
           
        return moving_averages

    if i > len(sensor_data) - n + 1: 
        return None

#...........................................................................................
#...........................................................................................
def main():
    sensor = Distance_Sensor()

    user_button = Button(5)
    
    counter=0

    blue_led = LED(19)
    red_led = LED(20)

    red_led.on() #              lets user know water is not pouring 

    servo = Servo(12)
    servo.min() #               latch is closed, no water can be poured 

    #cup_height = 175 mm
    #slot_height = 140 mm
 
    ori_dist = 260 #mm          distance from bottom of the stand to the sensor
    r =  37.5 #mm               the radius of the cup

    print(input("Press Enter to activate button"))

    while True:
        
        counter,water_h=button(user_button,counter)
        if counter>3:
            print("Finished")
            break
    
        sensor_data=water_dispenser(ori_dist,sensor,water_h,counter,servo,blue_led,red_led,r)
    
        ra=rolling_average(sensor,sensor_data)
        print ("the rolling average is: ",ra)
             
#...........................................................................................
#...........................................................................................
            
            
        
    
