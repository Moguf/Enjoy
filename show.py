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

ax=fig.add_subplot(111)
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
step=50
init_anime=[]
init_list=[]
for i,iline in enumerate(open(sys.argv[1]).readlines()):
    if i%step==0:
        ilist=[float(k) for k in iline.strip().split()]
        if i==0:
            init_list=[[ilist[0],ilist[1],ilist[2]],[ilist[3],ilist[4],ilist[5]]]
            
        one_frame=ax.plot([ilist[0],ilist[1],ilist[2]],[ilist[3],ilist[4],ilist[5]],'-ob',alpha=0.5,ms=30,lw=10)
        
        
        linelist[0].append(ilist[2])
        linelist[1].append(ilist[5])
        
        two_frame=ax.plot(linelist[0],linelist[1],'-r',ms=3,alpha=0.3)
        
        if len(linelist[0]) >300:
            del linelist[0][0]
            del linelist[1][0]

        init_anime.append(ax.plot(init_list[0],init_list[1],'-oy',alpha=0.2,ms=30,lw=10))
        anime.append(one_frame)
        anime2.append(two_frame)


Writer = animation.writers['ffmpeg']
writer = Writer(fps=15, metadata=dict(artist='Me'), bitrate=1800)
ani=animation.ArtistAnimation(fig,anime,interval=30,repeat_delay=1)
ani2=animation.ArtistAnimation(fig,anime2,interval=30,repeat_delay=1)
ani3=animation.ArtistAnimation(fig,init_anime,interval=30,repeat_delay=1)

ani3.save(filename+'.mp4', writer=writer,extra_anim=[ani2,ani])
