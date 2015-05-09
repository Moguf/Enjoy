#! /usr/bin/env python

import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np



fig=plt.figure()
plt.tick_params(labelbottom="off")
plt.tick_params(labelleft="off")

ax=fig.add_subplot(111)#,axisbg='darkslategray')
ax.set_aspect('equal')
ax.set_xlim([-2.3,2.3])
ax.set_ylim([-2.3,2.3])
ax.spines['right'].set_visible(False)
ax.spines['top'].set_visible(False)
ax.spines['bottom'].set_visible(False)
ax.spines['left'].set_visible(False)
ax.set_yticks([])
ax.set_yticks([])


anime=[]

cc=np.cos(-np.pi/2)
ss=np.sin(-np.pi/2)
for i,iline in enumerate(open("data.out").readlines()):
    if i%100==0:
        ilist=[float(i) for i in iline.strip().split()]
        one_frame=ax.plot([ilist[0],ilist[1],ilist[2]],[ilist[3],ilist[4],ilist[5]],'-o',alpha=0.5,ms=30,lw=10)
        anime.append(one_frame)
        
Writer = animation.writers['ffmpeg']
writer = Writer(fps=15, metadata=dict(artist='Me'), bitrate=1800)
ani=animation.ArtistAnimation(fig,anime,interval=30,repeat_delay=1)

ani.save('im.mp4', writer=writer)


plt.show()
