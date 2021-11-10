# -*- coding: utf-8 -*-
"""
Created on Sun Oct 31 22:19:42 2021

@author: diego
"""
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np
from tqdm import tqdm
from scipy.optimize import fsolve
import matplotlib.cm as cm


fig = plt.figure()
plt.style.use('dark_background')
ax = fig.add_subplot(111, projection='3d')
ax.set_axis_off()

pn=500 # Number of particles
maxr,minr= 500,-10 #Max position, Min position
frames= 1000 # Number of frames
G=6.673*10**-11 #Gravitational constant
m=10**16 #Mass of particle in origin
amp=1000 #Field of view
#minv,maxv= -0.01,0.01

r0=np.array([np.random.uniform(minr,maxr,pn),np.random.uniform(minr,maxr,pn),np.random.uniform(minr,maxr,pn)]) #Initial pos
r_u=r0/np.sqrt(r0[0]**2+r0[1]**2+r0[2]**2) #Inital position unit vectors
amag_0 = -G*m/(r0[0]**2+r0[1]**2+r0[2]**2)  #Initial acceleration magnitude
a0=amag_0*r_u # Initial acceleration poiting to the origin

vx_i=-10 # Magnitude of x component of initial velocity 

v0x=[]
v0y=[]
v0z=[]
for a,b,c,d,e,f in zip(r0[0],r0[1],r0[2],a0[0],a0[1],a0[2]):   ## Computing initial velocity to be perpendicullar to acceleration
    
    func= lambda x: d*vx_i+e*np.sqrt(G*m/np.sqrt(a**2+b**2+c**2)-vx_i-(x**2))+x*f    
    initial_guess = 0.00051
    tau_solution = fsolve(func, initial_guess)
    v0x.append(1)
    v0z.append(tau_solution[0])
    v0y.append( np.sqrt(G*m/np.sqrt(a**2+b**2+c**2)-1-tau_solution[0]**2))
v0=np.array([np.array([v0x])[0],np.array([v0y])[0],np.array([v0z])[0]])



rz=[]
ry=[]
rx=[]
vx=[]
vy=[]
vz=[]      ## Computing positions using constant acceleration for short amounts of time.
for i,t in zip(np.linspace(1,1.000001,frames),tqdm(range(frames+1))):  
    amag = -G*m/(r0[0]**2+r0[1]**2+r0[2]**2)
    a=amag*r_u 
    rx.append(a[0]*i**2/2+v0[0]*i+r0[0])    
    ry.append(a[1]*i**2/2+v0[1]*i+r0[1])
    rz.append(a[2]*i**2/2+v0[2]*i+r0[2])
    vx.append(v0[0]+a[0]*i)
    vy.append(v0[1]+a[1]*i)
    vz.append(v0[2]+a[2]*i)
    v0=np.array([vx[-1],vy[-1],vz[-1]])
    r0=np.array([rx[-1],ry[-1],rz[-1]])
    r_u=r0/np.sqrt(r0[0]**2+r0[1]**2+r0[2]**2)

rang=30
# Checking in particle got too close to origin
index=[]
for i,d in zip(range(frames),tqdm(range(frames+1))):
    for a,b,c,e in zip(rx[i],ry[i],rz[i],range(pn+1)):
        if a>-rang and a<rang  and b>-rang and b<rang and c>-rang and c<rang:
            index.append(tuple([i,e]))
        else:
          continue
for a in index:  # Making particle disappear if too close to origin
    for i,j,k in zip(rx[a[0]+1:],ry[a[0]+1:],rz[a[0]+1:]):
            i[a[1]]=3000
            j[a[1]]=3000
            k[a[1]]=3000
        
num_frame= [x[0] for x in index] # Counting particles too close to middle
count=0
c=[]
for n in np.arange(0,frames,1):
    for i in num_frame:
        if n==i:
            count=count+1
    c.append(count)
     
col=np.random.uniform(-10,10,pn)
    
def motion(n):  ## Plotting positions each frame
    ax.clear()    
    ax.set_axis_off()
    ax.scatter(xs=0,ys=0,zs=0,c="yellow",s=1800)   
    ax.scatter(xs=rx[n],ys=ry[n],alpha=0.6, zs=rz[n],c=col,label=" Devoured stars %.i" %c[n],cmap=cm.gray)
   # ax.legend(loc= "upper right")
    ax.set_xlim(-amp, amp)
    ax.set_ylim(-amp, amp)
    ax.set_zlim(-amp, amp)
    # ax.view_init(elev=0, azim=90)
   
ani = animation.FuncAnimation(fig, motion, range(1000),interval=0.0000001,cache_frame_data=(False)) # Animate
