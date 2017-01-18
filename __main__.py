# Jarred's Project

# Three body problem simulation
# Jarred Green
# Part of my final project for Programming Skills course

from visual import *
# import numpy as np
scene.width = 600
scene.height = 600
scene.title = 'Three Body Mechanics'
scene.autoscale = True
scene.fullscreen = False

# Initialize the three masses
m1 = sphere(
    pos=vector(10.0, 0, 0),
    vel=vector(0, 1.0, 0),
    mass=10,
    color=color.yellow,
    make_trail=True,
    interval=2,
    retain=10000
)

m2 = sphere(
    pos=vector(-10, 0, 3),
    vel=vector(-0.3, -1.0, 0.5),
    mass=10,
    color=color.red,
    make_trail=True,
    interval=2,
    retain=100000
)

m3 = sphere(
    pos=vector(0, 0, 0),
    vel=vector(0, 0.1, 0.1),
    mass=10,
    color=color.green,
    make_trail=True,
    interval=2,
    retain=10000
)

# move the frame to the center of mass
# also, adjust the sizes of the spheres for constant density

vcenter = ((m1.mass * m1.vel + m2.mass * m2.vel + m3.mass * m3.vel) /
           (m1.mass + m2.mass + m3.mass))
for i in [m1, m2, m3]:
    i.vel -= vcenter
    i.radius = 0.5 * i.mass ** (1.0 / 3.0)


def dydt(y):
    # calculate the derivative of the vector y
    deriv = zeros((6, 3), dtype=vector)
    radius_12 = y[0] - y[2]
    radius_23 = y[2] - y[4]
    radius_31 = y[4] - y[0]
    rad_12_c = radius_12 / mag(radius_12) ** 3.0
    rad_23_c = radius_23 / mag(radius_23) ** 3.0
    rad_31_c = radius_31 / mag(radius_31) ** 3.0

    # take derivatives
    deriv[1] = (-m2.mass * rad_12_c) + (m3.mass * rad_31_c)
    deriv[3] = (-m3.mass * rad_23_c) + (m1.mass * rad_12_c)
    deriv[5] = (-m1.mass * rad_31_c) + (m2.mass * rad_23_c)

    # copy the three velocities from y:
    deriv[0:5:2] = y[1:6:2]

    return deriv


# dt is the timestep in computations / sec
dt = 0.01

while True:
    # the rate of the calculations
    rate(100)

    # solved using the 4th order Runge Kutta method
    y = [m1.pos, m1.vel, m2.pos, m2.vel, m3.pos, m3.vel]
    k1 = dt * dydt(y)
    k2 = dt * dydt(y + k1 / 2.0)
    k3 = dt * dydt(y + k2 / 2.0)
    k4 = dt * dydt(y + k3)
    dy = k1 / 6.0 + k2 / 3.0 + k3 / 3.0 + k4 / 6.0

    # now update the animation
    m1.pos += dy[0]
    m1.vel += dy[1]
    m2.pos += dy[2]
    m2.vel += dy[3]
    m3.pos += dy[4]
    m3.vel += dy[5]
