#include <stdio.h>
#include <math.h>


int main(void){
    double theta[2];
    int k1[2];
    int k2[2];
    int k3[2];
    int k4[2];
    int kk[2];
    int i,j;
    double h=0.01;


    for(i=0;i<2;i++){
        k1[i]=0;
        k2[i]=0;
        k3[i]=0;
        k4[i]=0;
        kk[i]=0;
        theta[i]=0;
    }
    
    for(i=0;i<100;i++){
        k1[0]=h*-cos(theta[1]);
        k1[1]=h*theta[0];
        
        k2[0]=h*-cos(theta[1]+k1[0]/2.0);
        k2[1]=h*(theta[0]+k1[1])/2.0;
            
        k3[0]=h*-cos(theta[1]+k2[0]/2.0);
        k3[1]=h*(theta[0]+k2[1])/2.0;

        k4[0]=h*-cos(theta[1]+k3[0]);
        k4[1]=h*(theta[0]+k3[1]);
            
        kk[0]=h*(k1[0]+2*k2[0]+2*k3[0]+k4[0])/6.0;
        kk[1]=h*(k1[1]+2*k2[1]+2*k3[1]+k4[1])/6.0;
            
        theta[0]=theta[0]+kk[0];
        theta[1]=theta[1]+kk[1];
        printf("%7.3lf%7.3lf\n",cos(theta[1]),sin(theta[1]));
        h+=h;
    }
    

    return 0;

}
    
