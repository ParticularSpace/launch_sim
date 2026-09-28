import math

# CONSTANTS
GRAVITY = 9.81
SEA_LEVEL_AIR_DENSITY = 1.225  # kg/m^3
SCALE_HEIGHT = 8500  # meters


# ANGLE / VECTOR FUNCTIONS
def degrees_to_radians(angle):
    return math.radians(angle)


def calculate_thrust_components(thrust, angle):
    """
    Break thrust into horizontal and vertical components.

    Fx = F cos(theta)
    Fy = F sin(theta)
    """

    angle_rad = degrees_to_radians(angle)

    thrust_x = thrust * math.cos(angle_rad)
    thrust_y = thrust * math.sin(angle_rad)

    return thrust_x, thrust_y


# GRAVITY
def calculate_gravity_force(mass):
    """
    Fg = mg
    """

    return mass * GRAVITY


# ATMOSPHERE
def calculate_air_density(altitude):
    """
    Simplified exponential atmospheric model.

    rho = rho0 * e^(-h / H)

    rho0 = sea-level air density
    h    = altitude
    H    = atmospheric scale height
    """

    if altitude < 0:
        altitude = 0

    return SEA_LEVEL_AIR_DENSITY * math.exp(
        -altitude / SCALE_HEIGHT
    )


# DRAG
def calculate_drag_force(
    velocity,
    air_density,
    drag_coefficient,
    area
):
    """
    Aerodynamic drag:

    Fd = 1/2 * rho * v^2 * Cd * A
    """

    return (
        0.5
        * air_density
        * velocity ** 2
        * drag_coefficient
        * area
    )


def calculate_drag_components(
    velocity_x,
    velocity_y,
    air_density,
    drag_coefficient,
    area
):
    """
    Drag always acts opposite the velocity vector.
    """

    speed = math.sqrt(
        velocity_x ** 2 +
        velocity_y ** 2
    )

    if speed == 0:
        return 0.0, 0.0

    drag_force = calculate_drag_force(
        speed,
        air_density,
        drag_coefficient,
        area
    )

    drag_x = -drag_force * velocity_x / speed
    drag_y = -drag_force * velocity_y / speed

    return drag_x, drag_y


# KINEMATICS
def calculate_acceleration(force, mass):
    """
    Newton's Second Law:

    a = F / m
    """

    return force / mass


def update_velocity(velocity, acceleration, dt):
    """
    Numerical velocity update.

    v_new = v_old + a * dt
    """

    return velocity + acceleration * dt


def update_position(position, velocity, dt):
    """
    Numerical position update.

    x_new = x_old + v * dt
    """

    return position + velocity * dt