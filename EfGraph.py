import matplotlib.pyplot as plt
import matplotlib.animation as animation
import time

fig = plt.figure()
ax2 = fig.add_subplot(1,1,1)
ax2.set_title('Efficiency vs Time')
ax2.set_xlabel('Time')
ax2.set_ylabel('Propulsive Force')

def animate(i):
    pullData = open("EfGraphData.txt","r").read()
    dataArray = pullData.split('\n')
    xar = []
    yar = []
    for eachLine in dataArray:
        if len(eachLine)>1:
            x,y = eachLine.split(',')
            xar.append(int(x))
            yar.append(int(y))
    ax2.clear()
    ax2.plot(xar,yar)
ani = animation.FuncAnimation(fig, animate, interval=1000)
plt.show()
