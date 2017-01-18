## three dimensional simulation of the three-body problem
## using the Python Visual module for the animation
## see http://www.vpython.org/
from visual import *

global threebody
scene = display(title='University of Glasgow A1 Dynamical Astronomy orbit demos (press 1-7). RH mouse rotates, LH+RH zooms.', width=1280, height=800)
scene.autoscale=false;

## set up the masses. m1 is missing in 2-body systems
m1 = sphere(color=color.cyan,   make_trail=True, interval=2, retain=1000)
m2 = sphere(color=color.yellow,make_trail=True, interval=2, retain=1000)
m3 = sphere(color=color.white, make_trail=True, interval=2, retain=1000)

## move to the centre of mass frame and adjust sizes for constant density
def resetscene(m1,m2,m3):
    vcentre=(m1.mass*m1.vel+m2.mass*m2.vel+m3.mass*m3.vel)/(m1.mass+m2.mass+m3.mass)
    for a in [m1, m2, m3]:
        a.vel -= vcentre
        a.radius = 0.5*a.mass**(1.0/3.0)
        a.trail_object.pos=[]

def dydt(y):
## determine the derivative of the state vector y
    deriv = zeros((6,3), dtype=vector)
    r12=y[0]-y[2]; r23=y[2]-y[4]; r31=y[4]-y[0]
    r12c=r12/mag(r12)**3; r23c=r23/mag(r23)**3; r31c=r31/mag(r31)**3
    deriv[1] = -m2.mass*r12c + m3.mass*r31c
    deriv[3] = -m3.mass*r23c + m1.mass*r12c
    deriv[5] = -m1.mass*r31c + m2.mass*r23c
    deriv[0:5:2] = y[1:6:2] ## just copy the three velocities from y
    return deriv


def keyInput(evt):
    global threebody,dt
    s = evt.key
    if (s == '0'): ##circular
        m1.pos=vector( 100,0,0); m1.vel=vector(0,0,0);   m1.mass=0
        m2.pos=vector( -10,0,0);   m2.vel=vector( 0, 0,0); m2.mass=10
        m3.pos=vector( 10,0,0);  m3.vel=vector(0,0,0);  m3.mass=5
        scene.range=15
        resetscene(m1,m2,m3)
        threebody = False;
    if (s == '1'): ##circular
        m1.pos=vector( 100,0,0); m1.vel=vector(0,0,0);   m1.mass=0
        m2.pos=vector( 0,0,0);   m2.vel=vector( 0, 0,0); m2.mass=10
        m3.pos=vector( 10,0,0);  m3.vel=vector(0,-1,0);  m3.mass=0.1
        scene.range=20
        resetscene(m1,m2,m3)
        threebody = False;
    if (s == '2'):
        m1.pos=vector( 100,0,0); m1.vel=vector(0,0,0);   m1.mass=0
        m2.pos=vector( 5,0,0);   m2.vel=vector(0,0,0);   m2.mass=10.0
        m3.pos=vector(-10,0,0);  m3.vel=vector(0,0.5,0); m3.mass=0.1
        scene.range=15
        resetscene(m1,m2,m3)
        threebody= False
    if (s == '3'):
        m1.pos=vector( 100,0,0); m1.vel=vector(0,0,0);   m1.mass=0
        m2.pos=vector( 5,0,0);   m2.vel=vector(0,1.0/3.0,0);   m2.mass=10.0
        m3.pos=vector(-10,0,0);  m3.vel=vector(0,-2.0/3.0,0); m3.mass=5.0
        scene.range=20
        resetscene(m1,m2,m3)
        threebody= False
    if (s == '4'):
        m1.pos=vector( 100,0,0); m1.vel=vector(0,0,0);    m1.mass=0
        m2.pos=vector(-10,0,0);  m2.vel=vector(0,0.2,0);  m2.mass=5.0
        m3.pos=vector( 10,0,0);  m3.vel=vector(0,-0.2,0); m3.mass=5.0
        scene.range=15
        resetscene(m1,m2,m3)
        threebody= False
    if (s == '5'):
        m1.pos=vector( 100,0,0); m1.vel=vector(0,0,0);    m1.mass=0
        m2.pos=vector(-10,0,0);  m2.vel=vector(0,0.2,0);  m2.mass=10.0
        m3.pos=vector( 10,0,0);  m3.vel=vector(0,-0.2,0); m3.mass=5.0
        scene.range=15
        resetscene(m1,m2,m3)
        threebody= False
    if (s == '6'):
        threebody = True;
        m1.pos=vector( 10.5,0,0); m1.vel=vector(0.0, sqrt(10.0/10.5),0.0); m1.mass=0.01; m1.retain=500
        m2.pos=vector(0,0,0); m2.vel=vector(0,0,0);m2.mass=10.0
        m3.pos=vector(-10,0,0);  m3.vel=vector( 0, -1,0);  m3.mass=0.01;m3.retain=500
        scene.range=20
        #dt=0.1
        resetscene(m1,m2,m3)
        m1.radius = m1.radius*3;m3.radius = m3.radius*3
    if (s == '7'):
        threebody = True;
        m1.pos=vector( 10,0,0); m1.vel=vector(0.0, 1.0,0.0); m1.mass=10.0;  m1.retain=800
        m2.pos=vector(-10,0,3); m2.vel=vector(-0.3,-1.0,0.5);m2.mass=10.0; m2.retain=800
        m3.pos=vector( 0,0,0);  m3.vel=vector( 0, 0.1,0.1);  m3.mass=10.0; m3.retain=800
        scene.range=30
        resetscene(m1,m2,m3)

scene.bind('keydown', keyInput)

## initiate with the simplest system
m1.pos=vector( 100,0,0); m1.vel=vector(0,0,0);   m1.mass=0
m2.pos=vector( 0,0,0);   m2.vel=vector( 0, 0,0); m2.mass=10
m3.pos=vector( 10,0,0);  m3.vel=vector(0,-1,0);  m3.mass=0.1
scene.range=20
resetscene(m1,m2,m3)
threebody = False;

dt = 0.1 ## the time step.  Keep this as small as possible.

while True:
  rate(150)
  ## solve using forth-order Runge Kutta.  See CHOPF p62.
  y = [m1.pos,m1.vel,m2.pos,m2.vel,m3.pos,m3.vel]
  k1 = dt*dydt(y);  k2 = dt*dydt(y+k1/2.0)
  k3 = dt*dydt(y+k2/2.0);  k4 = dt*dydt(y+k3)
  dy = k1/6.0 + k2/3.0 +k3/3.0 + k4/6.0
## update the animation
  if threebody:
    m1.pos += dy[0]; m1.vel += dy[1]
  if mag(m2.pos-m3.pos)>1:
     m2.pos += dy[2]; m2.vel += dy[3]
     m3.pos += dy[4]; m3.vel += dy[5]
