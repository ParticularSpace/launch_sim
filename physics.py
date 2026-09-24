import math

GRAVITY = 9.81


def degrees_to_radians(angle):
    """
    Convert degrees to radians.
    """
    return math.radians(angle)


def calculate_thrust_components(thrust, angle):
    """
    Break thrust into x and y components.

    Fx = F cos(theta)
    Fy = F sin(theta)
    """

    angle_rad = degrees_to_radians(angle)

    force_x = thrust * math.cos(angle_rad)
    force_y = thrust * math.sin(angle_rad)

    return force_x, force_y


def calculate_gravity_force(mass):
    """
    Weight due to gravity.

    Fg = mg
    """
    return mass * GRAVITY


def calculate_acceleration(force, mass):
    """
    Newton's Second Law.

    F = ma
    a = F / m
    """
    return force / mass


def update_velocity(velocity, acceleration, dt):
    """
    Update velocity using:

    v_new = v_old + a * dt
    """
    return velocity + acceleration * dt


def update_position(position, velocity, dt):
    """
    Update position using:

    x_new = x_old + v * dt
    """
    return position + velocity * dt