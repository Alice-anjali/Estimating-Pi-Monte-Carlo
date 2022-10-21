import matplotlib.pyplot as plt
import numpy as np
import math

#1. Circle at origin with radius 1
def draw_circle():
    fig, ax = plt.subplots()
    x = 0
    y = 0
    radius = 1 #radius of circle
    circle = plt.Circle( (x, y ),radius ,fill = False, color='b' )

    ax.set_aspect(1)
    ax.add_artist(circle)
    plt.title( 'Circle' )
    plt.xlim([-1.3, 1.3])
    plt.ylim([-1.3, 1.3])


#Scaling the random point of 0,1 range to -1,1 range using Simple Linear Conversion

def get_new_value(k):
    oldMin = 0
    oldMax = 1
    newMin = -1
    newMax = 1
    oldValue = k #received random value

    oldRange = oldMax - oldMin
    newRange = newMax - newMin
    newValue = (((oldValue - oldMin) * newRange) / oldRange) + newMin #calculated new value

    return newValue


#2 plot random points

def plot_points(points):
    
    #list to store x and y values of the points
    x_list = []
    y_list = []
    for i  in range(points):
        #generating random x and y values
        x = np.random.rand()
        y = np.random.rand()
        new_x = round(get_new_value(x), 1)
        new_y = round(get_new_value(y), 1)
                
        x_list.append(new_x)
        y_list.append(new_y)
        
    draw_circle() #plotting circle
    plt.plot(x_list, y_list, 'o', color='r' ) #plotting points
    plt.show()
    
    return x_list, y_list



#3 Calculating value of pi

def calculate_pi():
    
    #4 Calculating value of pi for 100, 200, 500, 1000, 5000
    
    points_list = [100, 200, 500, 1000, 5000]
    pi_orig = math.pi
    print("--------------------------------------")
    print("Original value of pi = ",round(pi_orig, 10))
    print("--------------------------------------")
    print(" ")
        
    for i in points_list:
        print('\033[1m', "Plotting ", i, " points:")
        x_list, y_list = plot_points(i)
        
        inside_pt = 0 #number of points inside circle
        total_pt = 0 #total number of points plotted
    
        for j in range(i):
            #distance between the point from origin
            distance_o = x_list[j]**2 + y_list[j]**2
    
            #if distance is less than radius of circle, then point is inside the circle
            if distance_o <= 1:
                inside_pt += 1
            
            total_pt += 1
                
        pi_value = (inside_pt / total_pt) * 4 #calculating the value of pi
        pi_value = round(pi_value, 10)
        difference = round(pi_orig - pi_value, 10) #comparison of the two values of pi
        
        print("Calculated value of pi = ", pi_value)
        print("Difference between original pi and calculated pi = ", difference)
        print(" ")
        print("-------------------------------------------------------------")
        print(" ")
        
        
calculate_pi()
    
