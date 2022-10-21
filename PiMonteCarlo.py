import matplotlib.pyplot as plt

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


draw_circle()
plt.show()
