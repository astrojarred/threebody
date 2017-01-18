## three dimensional simulation of the three-body problem
## using the Python Visual module for the animation
## see http://www.vpython.org/
from visual import *

scene.autoscale=true;
##scene.range=15

## set up the masses
m1 = sphere(pos=vector( 10,0,0),vel=vector( 0.0, 1.0,0.0),
              mass=10.0, color=color.red,
              make_trail=True, interval=2, retain=1000)
m2 = sphere(pos=vector(-10,0,3),vel=vector(-0.3,-1.0,0.5),
              mass=10.0, color=color.yellow,
              make_trail=True, interval=2, retain=1000)
m3 = sphere(pos=vector(  0,0,0),vel=vector(   0, 0.1,0.1),
              mass=10.0, color=color.white,
              make_trail=True, interval=2, retain=1000)

## move to the centre of mass frame and adjust sizes for constant density
vcentre=(m1.mass*m1.vel+m2.mass*m2.vel+m3.mass*m3.vel)/(m1.mass+m2.mass+m3.mass)
for a in [m1, m2, m3]:
  a.vel -= vcentre
  a.radius = 0.5*a.mass**(1.0/3.0)

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

dt = 0.1 ## the time step.  Keep this as small as possible.

while True:
  rate(100)
  ## solve using forth-order Runge Kutta.  See CHOPF p62.
  y = [m1.pos,m1.vel,m2.pos,m2.vel,m3.pos,m3.vel]
  k1 = dt*dydt(y);  k2 = dt*dydt(y+k1/2.0)
  k3 = dt*dydt(y+k2/2.0);  k4 = dt*dydt(y+k3)
  dy = k1/6.0 + k2/3.0 +k3/3.0 + k4/6.0
## update the animation
  m1.pos += dy[0]; m1.vel += dy[1]
  m2.pos += dy[2]; m2.vel += dy[3]
  m3.pos += dy[4]; m3.vel += dy[5]