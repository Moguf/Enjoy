#! /usr/bin/env python

import sys
import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np
import matplotlib.lines as lines


fig=plt.figure()
plt.tick_params(labelbottom="off")
plt.tick_params(labelleft="off")

ax=fig.add_subplot(111)#,axisbg='darkslategray')
ax.set_aspect('equal')
ax.set_xlim([-2.3,2.3])
ax.set_ylim([-2.3,2.3])
ax.set_xticks(())
ax.spines['right'].set_visible(False)
ax.spines['top'].set_visible(False)
ax.spines['bottom'].set_visible(False)
ax.spines['left'].set_visible(False)
ax.set_yticks([])
ax.set_yticks([])


anime=[]

cc=np.cos(-np.pi/2)
ss=np.sin(-np.pi/2)
filename=sys.argv[1].split(".")[0]
follow=10
anime2=[]
linelist=[[] for i in range(2)]
print linelist
step=1000
data=open(sys.argv[1]).readlines()
def animate(iframe):
    plt.clf()
    iline=data[iframe]
    if iframe%step==0:
        ilist=[float(i) for iframe in iline.strip().split()]
        ax.plot([ilist[0],ilist[1],ilist[2]],[ilist[3],ilist[4],ilist[5]],'-ob',alpha=0.5,ms=30,lw=10)
        
        linelist[0].append(ilist[2])
        linelist[1].append(ilist[5])
        ax.plot(linelist[0],linelist[1],'-r',ms=3,alpha=0.3)        

        
        if len(linelist[0]) >300:
            del linelist[0][0]
            del linelist[1][0]



Writer = animation.writers['ffmpeg']
writer = Writer(fps=15, metadata=dict(artist='Me'), bitrate=1800)
ani=animation.FuncAnimation(fig,animate,frames=30,repeat_delay=1)
plt.show()
#ani=animation.ArtistAnimation(fig,anime2,interval=30,repeat_delay=1)

ani.save(filename+'.mp4', writer=writer)

