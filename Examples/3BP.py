#PLEASE VISIT: www.pythonforphysics.blogspot.com
#Created by: Oriol Frigola
#Year: 2013
#THE PROGRAM IS DISTRIBUTED IN THE HOPE THAT
#...IT WILL BE USEFUL, BUT WITHOUT ANY WARRANTY.

from visual import *
import math
scene.width = 700
scene.height = 600
scene.title = 'THREE BODY PROBLEM'
scene.autoscale= False
scene.fullscreen = False


#PARAMETERS

#Masses
m1 = 3 
m2 = 3
m3 =  3

e1 = 0.1 #Escale factor
e2 = 0.1 #Escale factor
e3 = 0.1 #Escale factor

#The radius as a funtion of mass (volume)
r1 = pow(m1, 1./3)*e1 
r2 = pow(m2, 1./3)*e2
r3 =  pow(m3, 1./3)*e3
G = 3
dt =0.01

#Initial positions
pos1 = vector(-3, 0, 0) #red ball
pos2 = vector(0, 0, 0) #green ball
pos3 =vector(-5, 0, 0) #blue ball

#velocitats inicials
v1= vector(0, 0, 1) #red
v2 = vector(0, 0, 0) #green
v3 = vector(0, 0, -1.5) #blue

#DRAWING
P1 = sphere(pos = pos1, radius = r1, color = color.red)
P2 = sphere(pos = pos2, radius = r2, color = color.green)
P3 = sphere(pos = pos3, radius = r3, color = color.blue)
P1.trail = curve(color = P1.color)
P2.trail = curve(color = P2.color)
P3.trail = curve(color = P3.color)


#MOVEMENT
#Defining an acceleration function:
def grav(p, p_m, m):
    r = p-p_m
    r_mag = mag(r)
    r_norm = norm(r)
    a = (-G*m/(r_mag**2)) * r_norm
    return a

#Computing
while True:
    rate(100)
    #P1
    a1 = grav(P1.pos, P2.pos, m2) + grav(P1.pos, P3.pos, m3)
    dv1 = a1*dt
    v1 = v1 + dv1
    dp1 = v1*dt
    #P2
    a2 = grav(P2.pos, P1.pos, m1) + grav(P2.pos, P3.pos, m3)
    dv2 = a2*dt
    v2 = v2 + dv2
    dp2 = v2*dt
    #P3
    a3 = grav(P3.pos, P2.pos, m2) + grav(P3.pos, P1.pos, m1)
    dv3 = a3*dt
    v3 = v3 + dv3
    dp3 = v3*dt
    #Updating positions
    P1.pos = P1.pos + dp1
    P1.trail.append(pos=P1.pos)
    P2.pos = P2.pos + dp2
    P2.trail.append(pos=P2.pos)
    P3.pos = P3.pos + dp3
    P3.trail.append(pos=P3.pos)
    #Colision condition
    '''if  mag(P1.pos-P2.pos)<(r1+r2) or mag(P1.pos-P3.pos)<(r1+r3) or (mag(P3.pos-P2.pos)<(r3+r2)):
        print "Collision !?"
        break '''

print "...finish"












