import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt
from matplotlib.patches import Circle
from celluloid import Camera
import time

tic = time.perf_counter()
print("swinging...", end ='\r')

g=9.8		#gravitational acceleration
l1=1		#length of pendulum 1
l2=1		#length of pendulum 2
m1=1		#mass of pendulum 1
m2=1		#mass of pendulum 2

theta1_0=0.9999*np.pi 				#initial theta values
theta2_0=-0.9999*np.pi
alpha1_0=0							#initial change in theta values
alpha2_0=0					

T=20									#time in seconds to run model
AnimationFps=20						#fps of output animation

res=60*T							#number of timesteps
plotfreq=round(60/AnimationFps)		#frequency to write timesteps to output animation

#function to differentiate U = [theta1, alpha1=theta1_dot, theta2, alpha2=theta2_dot] based on equations of motion
def dU_dt(U,t):						
	alpha1dot = (m2*g*np.cos(U[0]-U[2])*np.sin(U[2])-m2*l2*U[3]**2*np.sin(U[0]-U[2])-1/2*m2*l1*U[1]**2*np.sin(2*(U[0]-U[2]))-(m1+m2)*g*np.sin(U[0]))/(l1*(m1+m2-m2*np.cos(U[0]-U[2])**2))
	alpha2dot = ((m1+m2)*(g*np.sin(U[2])-l1*U[1]**2*np.sin(U[0]-U[2])-g*np.cos(U[0]-U[2])*np.sin(U[0]))-1/2*m2*l2*U[3]**2*np.sin(2*(U[0]-U[2])))/(l2*(m2*np.cos(U[0]-U[2])-m1-m2))	
	return [U[1],alpha1dot,U[3],alpha2dot]

U0=[theta1_0,alpha1_0,theta2_0,alpha2_0]		#Initial conditions for U
t=np.linspace(0,T,res)							#time array

#Evolves the system
U=odeint(dU_dt,U0,t)
theta1 = U[:,0]									#Arrays of theta values over time
theta2 = U[:,2]

x1 = l1 * np.sin(theta1)						#Mass positions in cartesian coordinates
y1 = -l1 * np.cos(theta1)
x2 = x1 + l2 * np.sin(theta2)
y2 = y1 - l2 * np.cos(theta2)

toc = time.perf_counter()
print(f"swinging...{toc - tic:0.4f} secs")

tic = time.perf_counter()
print("plotting...", end ='\r')

fig, ax = plt.subplots()		#figure to plot pendulumns
camera = Camera(fig)			#camera to snap plot for animation
fig.subplots_adjust(left=0, bottom=0, right=1, top=1, wspace=None, hspace=None)		#remove whitespace around plot

xlim_l=min(np.minimum(x1,x2))		#limits of mass positions
xlim_h=max(np.maximum(x1,x2))
ylim_l=min(np.minimum(y1,y2))
ylim_h=max(0,max(np.maximum(y1,y2)))
xbuff=0.1*(xlim_h-xlim_l)			#buffer to leave 10% margin
ybuff=0.1*(ylim_h-ylim_l)

plt.axis([xlim_l-xbuff, xlim_h+xbuff, ylim_l-ybuff, ylim_h+ybuff])
ax.set_aspect('equal', adjustable='box')		#equal aspect to avoid stretching squishing
plt.axis('off')									#hide axes


for i in range(0,res):		#loop over timesteps
	if i%plotfreq==0:		#if the timestep is to be written to animation
		#plot trail from previous half second
		ax.plot(x2[max(0,i-round(0.5*res/T)):i+1], y2[max(0,i-round(0.5*res/T)):i+1], '-', lw=2, c='red',solid_capstyle='round'); 
		#plot both pendulum arms with masses at end
		ax.plot([0, x1[i], x2[i]], [0, y1[i], y2[i]], 'o-', lw=2, c='k',markevery=[1,2],solid_capstyle='round');
		camera.snap() #snap plot for animation

toc = time.perf_counter()
print(f"plotting...{toc - tic:0.4f} secs")

tic = time.perf_counter()
print("animating...", end ='\r')
animation = camera.animate(interval=1000*T*plotfreq/res) #animate
animation.save('DoublePendulum.mp4', fps=len(t)/(T*plotfreq), extra_args=['-vcodec', 'libx264']) 	#save mp4 animation
#animation.save('DoublePendulum.gif', fps=len(t)/(T*plotfreq), writer = 'imagemagick')				#save gif animation (more expensive)
toc = time.perf_counter()
print(f"animating...{toc - tic:0.4f} secs")
