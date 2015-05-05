#! /usr/bin/env python3
import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np





class DoublePenduium:
    def __init__(self):
        self.theta0=90
        self.frame=[]
        
    def func1(self,i,theta,vtheta):
        return -np.cos(theta)

    def func2(self,t,theta,vtheta):
        return vtheta

        
    def do(self):
        fig=plt.figure()
        ax=fig.add_subplot(111)
        ax.set_aspect('equal')
        ax.set_xlim([-1,1])
        ax.set_ylim([-1,1])
        
        theta=[0,0]#-2*np.pi/6]  #velo,postion
        k1=[0 for i in range(2)]
        k2=[0 for i in range(2)]
        k3=[0 for i in range(2)]
        k4=[0 for i in range(2)]
        kk=[0 for i in range(2)]
        x=[]
        self.frame=[]
        self.frame2=[]
        h=0.1
        for i in xrange(200):
            k1[0]=h*self.func1(i,theta[1],theta[0])
            k1[1]=h*self.func2(i,theta[1],theta[0])
            
            k2[0]=h*self.func1(i,theta[1]+k1[1]*0.5,theta[0]+k1[0]*0.5)
            k2[1]=h*self.func2(i,theta[1]+k1[1]*0.5,theta[0]+k1[0]*0.5)
            
            k3[0]=h*self.func1(i,theta[1]+k2[1]*0.5,theta[0]+k2[0]*0.5)
            k3[1]=h*self.func2(i,theta[1]+k2[1]*0.5,theta[0]+k2[0]*0.5)

            k4[0]=h*self.func1(i,theta[1]+k3[1],theta[0]+k3[0])
            k4[1]=h*self.func2(i,theta[1]+k3[1],theta[0]+k3[0])
            
            kk[0]=(k1[0]+2.0*k2[0]+2.0*k3[0]+k4[0])/6.0
            kk[1]=(k1[1]+2.0*k2[1]+2.0*k3[1]+k4[1])/6.0
            
            theta[0]=theta[0]+kk[0]   #velo
            theta[1]=theta[1]+kk[1]   #postion

            x.append(theta[0])
            
            print theta[0]
            one_frame=ax.plot([0,np.cos(theta[1])],[0,np.sin(theta[1])],"-ob")
            #one_frame=ax.plot(np.cos(theta[1]),np.sin(theta[1]),"ob")
            #one_frame=plt.plot(theta[1],0,"ob")
            self.frame.append(one_frame)
            #self.frame2.append(one__frame)
            
        ani=animation.ArtistAnimation(fig,self.frame,interval=30,repeat_delay=1)
        #ani=animation.ArtistAnimation(fig,self.frame2,interval=30,repeat_delay=1)
        #ax.plot(x)
        plt.show()
        
if __name__=='__main__':
    test=DoublePenduium()
    test.do()
