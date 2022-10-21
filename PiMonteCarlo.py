import matplotlib.pyplot as plt
import numpy as np

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
