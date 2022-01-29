# -*- coding: utf-8 -*-
"""
Created on Sat Jan 29 16:58:30 2022

@author: diego
"""

# -*- coding: utf-8 -*-
"""
Created on Sat Jan 29 16:48:02 2022

@author: diego
"""

import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np
from tqdm import tqdm
from scipy.optimize import fsolve
import matplotlib.cm as cm
import sys

fig = plt.figure()
plt.style.use('dark_background')
ax = fig.add_subplot(111, projection='3d')

pn=400 # Number of particles
frames= 3000 # Number of frames
G=6.673*10**-11 #Gravitational constant
m=10**15 #Mass of particle in origin
amp=1500 #Field of view
#minv,maxv= -0.01,0.01

r0_sun = np.array([-2500,0,0])
sx=np.full((1,pn),-2500)
sy=np.full((1,pn),0)
sz=np.full((1,pn),0)
rs=np.concatenate((sx,sy,sz),axis=0)

r0 =np.array([np.random.uniform(-2800,-2200,pn),np.random.uniform(-300,300,pn),np.random.uniform(-300,300,pn)])
r_2=r0-rs
amag_0 = -G*m/(r_2[0]**2+r_2[1]**2+r_2[2]**2)
r_2_unit=r_2/np.sqrt(r_2[0]**2+r_2[1]**2+r_2[2]**2)
a0 = amag_0*r_2_unit
vx_1= np.random.uniform(-1,1,pn)

v0x=[]
v0y=[]
v0z=[]
for a,b,c,d,e,f,g in zip(r_2[0],r_2[1],r_2[2],a0[0],a0[1],a0[2],vx_1):   ## Computing initial velocity to be perpendicullar to acceleration
    
    func= lambda x: d*g+e*np.sqrt(G*m/np.sqrt(a**2+b**2+c**2)-g-(x**2))+x*f    
    initial_guess = 0.000551
    tau_solution = fsolve(func, initial_guess)
    v0x.append(g)
    v0z.append(tau_solution[0])
    v0y.append( np.sqrt(G*m/np.sqrt(a**2+b**2+c**2)-1-tau_solution[0]**2))
v0=np.array([np.array([v0x])[0],np.array([v0y])[0],np.array([v0z])[0]])   

# First attempt let's choose a small constant velocity for the star and suppose 
# that the satelites will remain in orbit.
# If this doesn't work I could add the initial velocity
# of the star to the satellites such that they are at rest 
# with respect to one another in the direction of the velocity of the star.
# (Obviously they are not are rest with one another because the satellites are orbiting).
v0_sun = np.array([np.random.uniform(-1,1,1)[0],np.random.uniform(-1,1,1)[0],np.random.uniform(-1,1,1)[0]])

## Second Star -------------
r0_Draconis = np.array([2500,0,0])
sxD=np.full((1,pn),2500)
syD=np.full((1,pn),0)
szD=np.full((1,pn),0)
rsD=np.concatenate((sxD,syD,szD),axis=0)   # Right star initial position.

r_2o=r0-rsD  #Distance from stellites of star in the left, to star in the right
amag_0o= -G*m/(r_2o[0]**2+r_2o[1]**2+r_2o[2]**2)
r_2_unito=r_2o/np.sqrt(r_2o[0]**2+r_2o[1]**2+r_2o[2]**2)



v0_Draconis = np.array([np.random.uniform(-1,1,1)[0],np.random.uniform(-1,1,1)[0],np.random.uniform(-1,1,1)[0]]) #initial velocity of right star

#Asteroids orbiting second star.
r0D =np.array([np.random.uniform(+2800,2200,pn),np.random.uniform(-300,300,pn),np.random.uniform(-300,300,pn)])
r_2D=r0D-rsD
amag_0D = -G*m/(r_2D[0]**2+r_2D[1]**2+r_2D[2]**2)
r_2D_unit=r_2D/np.sqrt(r_2D[0]**2+r_2D[1]**2+r_2D[2]**2)
a0D = amag_0D*r_2D_unit
vx_1D= np.random.uniform(-1,1,pn)

v0xD=[]
v0yD=[]
v0zD=[]
for a,b,c,d,e,f,g in zip(r_2D[0],r_2D[1],r_2D[2],a0D[0],a0D[1],a0D[2],vx_1D):   ## Computing initial velocity to be perpendicullar to acceleration
    
    func= lambda x: d*g+e*np.sqrt(G*m/np.sqrt(a**2+b**2+c**2)-g-(x**2))+x*f    
    initial_guess = 0.00051
    tau_solution = fsolve(func, initial_guess)
    v0xD.append(g)
    v0zD.append(tau_solution[0])
    v0yD.append( np.sqrt(G*m/np.sqrt(a**2+b**2+c**2)-1-tau_solution[0]**2))
v0D=np.array([np.array([v0xD])[0],np.array([v0yD])[0],np.array([v0zD])[0]])   


###
#Gravitational attraction between the two stars:
r_sd= rs-rsD
asdmag0=-G*m/(r_sd[0]**2+r_sd[1]**2+r_sd[2]**2)
r_sd_unit=r_sd/np.sqrt(r_sd[0]**2+r_sd[1]**2+r_sd[2]**2)
##

r_2Do= r0D-rs  # Distance from satellites in the right to star in the left.
amag_0Do = -G*m/(r_2Do[0]**2+r_2Do[1]**2+r_2Do[2]**2)
r_2unitDo=r_2Do/np.sqrt(r_2Do[0]**2+r_2Do[1]**2+r_2Do[2]**2)



rz=[]
ry=[]
rx=[]
vx=[]
vy=[]
vz=[]    
r_sunx=[]
r_suny=[]
r_sunz=[]
v_sunx=[]
v_suny=[]
v_sunz=[]
r_sunxD=[]
r_sunyD=[]
r_sunzD=[]
v_Dx=[]
v_Dy=[]
v_Dz=[]
rx_2=[]
ry_2=[]
rz_2=[]
vx_2=[]
vy_2=[]
vz_2=[]

    ## Computing positions using constant acceleration for short amounts of time.
for i,t in zip(np.linspace(0,100.000001,frames),tqdm(range(frames+1))):  
    amag1 = -G*m/(r_2[0]**2+r_2[1]**2+r_2[2]**2)
    amag2= -G*m/(r_2o[0]**2+r_2o[1]**2+r_2o[2]**2)
    a=amag1*r_2_unit + amag2*r_2_unito
   # a =amag2*r_2_unito
    rx.append(a[0]*i**2/2+v0[0]*i+r0[0])    
    ry.append(a[1]*i**2/2+v0[1]*i+r0[1])
    rz.append(a[2]*i**2/2+v0[2]*i+r0[2])
    vx.append(v0[0]+a[0]*i)
    vy.append(v0[1]+a[1]*i)
    vz.append(v0[2]+a[2]*i)
    v0=np.array([vx[-1],vy[-1],vz[-1]])
    r0=np.array([rx[-1],ry[-1],rz[-1]])
    amagsd= -G*m/(r_sd[0]**2+r_sd[1]**2+r_sd[2]**2)
    asd=amagsd*r_sd_unit 
    r_sunx.append(asd[0]*i**2/2+v0_sun[0]*i+rs[0])
    r_suny.append(asd[1]*i**2/2+v0_sun[1]*i+rs[1])
    r_sunz.append(asd[2]*i**2/2+v0_sun[2]*i+rs[2])
    v_sunx.append(v0_sun[0]+asd[0]*i)
    v_suny.append(v0_sun[1]+asd[1]*i)
    v_sunz.append(v0_sun[2]+asd[2]*i)
    v0_sun=np.array([v_sunx[-1],v_suny[-1],v_sunz[-1]])
    rs=np.array([r_sunx[-1],r_suny[-1],r_sunz[-1]])
    r_2=r0-rs
    r_2_unit=r_2/np.sqrt(r_2[0]**2+r_2[1]**2+r_2[2]**2)    
    r_sunxD.append(-asd[0]*i**2/2+v0_Draconis[0]*i+rsD[0])
    r_sunyD.append(-asd[1]*i**2/2+v0_Draconis[1]*i+rsD[1])
    r_sunzD.append(-asd[2]*i**2/2+v0_Draconis[2]*i+rsD[2])
    v_Dx.append(v0_Draconis[0]-asd[0]*i)
    v_Dy.append(v0_Draconis[1]-asd[1]*i)
    v_Dz.append(v0_Draconis[2]-asd[2]*i)
    rsD=np.array([r_sunxD[-1],r_sunyD[-1],r_sunzD[-1]])
    v0_Draconis=np.array([v_Dx[-1],v_Dy[-1],v_Dz[-1]])
    r_2o=r0-rsD
    r_2_unito=r_2o/np.sqrt(r_2o[0]**2+r_2o[1]**2+r_2o[2]**2)    
    ## Position of second start orbits
    amagD1= -G*m/(r_2D[0]**2+r_2D[1]**2+r_2D[2]**2)
    amagD2 = -G*m/(r_2Do[0]**2+r_2Do[1]**2+r_2Do[2]**2)
    aD=amagD1*r_2D_unit + amagD2*r_2unitDo
    rx_2.append(aD[0]*i**2/2+v0D[0]*i+r0D[0])    
    ry_2.append(aD[1]*i**2/2+v0D[1]*i+r0D[1])
    rz_2.append(aD[2]*i**2/2+v0D[2]*i+r0D[2])
    vx_2.append(v0D[0]+aD[0]*i)
    vy_2.append(v0D[1]+aD[1]*i)
    vz_2.append(v0D[2]+aD[2]*i)
    v0D=np.array([vx_2[-1],vy_2[-1],vz_2[-1]])
    r0D=np.array([rx_2[-1],ry_2[-1],rz_2[-1]])
    r_2D=r0D-rsD
    r_2D_unit=r_2D/np.sqrt(r_2D[0]**2+r_2D[1]**2+r_2D[2]**2)
    r_2Do=r0D-rs
    r_2unitDo= r_2Do/np.sqrt(r_2Do[0]**2+r_2Do[1]**2+r_2Do[2]**2)
        
col=np.random.uniform(-100,100,pn)

    
def motion(n):  ## Plotting positions each frame
    ax.clear()    
    ax.set_axis_off()
    ax.scatter(xs=r_sunx[n],ys=r_suny[n],zs=r_sunz[n],c="orange",s=500)   
    #ax.scatter(-1000,0,0,s=1500)
    #ax.scatter(1000,0,0,s=1500)
    ax.scatter(xs=rx[n],ys=ry[n],alpha=1, zs=rz[n],c=col,cmap=cm.viridis)
    #plt.legend()
    ax.scatter(xs=r_sunxD[n],ys=r_sunyD[n],zs=r_sunzD[n],c="purple",s=500)
   # ax.legend(loc= "upper right")
    ax.scatter(xs=rx_2[n],ys=ry_2[n],zs=rz_2[n],cmap=cm.magma,c=col)
    ax.set_xlim(-amp, amp)
    ax.set_ylim(-amp, amp)
    ax.set_zlim(-amp, amp)
    #ax.view_init(elev=0, azim=90)
   
ani = animation.FuncAnimation(fig, motion, range(frames),interval=0.0000001,cache_frame_data=(False)) # Animate    
