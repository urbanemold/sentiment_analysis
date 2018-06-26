import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib import style


style.use('fivethirtyeight')

fig = plt.figure()
ax1 = fig.add_subplot(1,1,1)

def animate(i):
    graph_data = open('twitter_output.txt','r').read()
    lines = graph_data.split('\n')
    xarrray = []
    yarray = []

    x=0
    y=0

    for l in lines:
        x+=1
        if "pos" in l:
            y+=1.2
        elif "neg" in l:
            y-=0.3
        xarray.append(x)
        yarray.append(y)
ax1.clear()
ax1.plot(xarray, yarray)

animation=animation.FuncAnimation(fig,animate,interval=1000)
plt.show()
    
