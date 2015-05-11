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
        self.g=9.8
        
    def func1(self,i,theta,vtheta):
        S=np.sin(theta[0]-theta[1])
        C=np.cos(theta[0]-theta[1])
        if i==0:
            return (S*vtheta[1]**2+C*S*vtheta[0]**2+2*self.g*np.sin(theta[0])-self.g*C*np.sin(theta[1]))/(C**2-2)
        elif i==1:
            return (C*S*vtheta[1]**2+2*S*vtheta[0]**2+2*self.g*C*np.sin(theta[0])-2*self.g*np.sin(theta[1]))/(2-C**2)
        
        
    def func2(self,i,theta,vtheta):
        return vtheta[i]
    
        
    def do(self,theta1,theta2,filename):
        ofile=open(filename,'w')
        otxt=""
        
        theta=np.array([theta1,theta2])#theta1,theta2
        vtheta=np.array([0.0,0.0])#vtheta1,vtheta2
        
        k1=np.array([0.0 for i in range(4)])
        k2=np.array([0.0 for i in range(4)])
        k3=np.array([0.0 for i in range(4)])
        k4=np.array([0.0 for i in range(4)])
        kk=np.array([0.0 for i in range(4)])

        self.frame=[]
        x=[]
        h=0.0001
        
        for i in xrange(2000000):
            k1[0]=h*self.func1(0,theta,vtheta)
            k1[1]=h*self.func2(0,theta,vtheta)
            k1[2]=h*self.func1(1,theta,vtheta)
            k1[3]=h*self.func2(1,theta,vtheta)

            _ptmp=theta+np.array([k1[0],k1[2]])*0.5
            _vtmp=vtheta+np.array([k1[1],k1[3]])*0.5
            k2[0]=h*self.func1(0,_ptmp,_vtmp)
            k2[1]=h*self.func2(0,_ptmp,_vtmp)
            k2[2]=h*self.func1(1,_ptmp,_vtmp)
            k2[3]=h*self.func2(1,_ptmp,_vtmp)

            _ptmp=theta+np.array([k2[0],k2[2]])*0.5
            _vtmp=vtheta+np.array([k2[1],k2[3]])*0.5
            k3[0]=h*self.func1(0,_ptmp,_vtmp)
            k3[1]=h*self.func2(0,_ptmp,_vtmp)
            k3[2]=h*self.func1(1,_ptmp,_vtmp)
            k3[3]=h*self.func2(1,_ptmp,_vtmp)
            
            _ptmp=theta+np.array([k3[0],k3[2]])
            _vtmp=vtheta+np.array([k3[1],k3[3]])
            k4[0]=h*self.func1(0,_ptmp,_vtmp)
            k4[1]=h*self.func2(0,_ptmp,_vtmp)
            k4[2]=h*self.func1(1,_ptmp,_vtmp)
            k4[3]=h*self.func2(1,_ptmp,_vtmp)


            kk=(k1+2.0*k2+2.0*k3+k4)/6.0

            
            theta=theta+np.array([kk[1],kk[3]])     #postion
            vtheta=vtheta+np.array([kk[0],kk[2]])     #velo
            #x.append(vtheta)
            if i%10==0:
                otxt+="%lf %lf %lf %lf %lf %lf \n"% (0,np.cos(theta[0]-np.pi/2),np.cos(theta[0]-np.pi/2)+np.cos(theta[1]-np.pi/2),0,np.sin(theta[0]-np.pi/2),np.sin(theta[0]-np.pi/2)+np.sin(theta[1]-np.pi/2))
                
        ofile.write(otxt)
        ofile.close()
        
        #ax.plot(x)
        #plt.show()
        
if __name__=='__main__':
    test=DoublePenduium()
    #for i in xrange(4,7):
        #for j in xrange(7):
    i=3
    j=6
    filename="dp"+str(i)+str(j)+".out"
    print filename,i*np.pi/6,j*np.pi/6
    test.do(i*np.pi/6,j*np.pi/6,filename)
