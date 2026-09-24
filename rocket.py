class Rocket:

    def __init__(self, mass, thrust, burn_time, launch_angle):
        self.mass = mass
        self.thrust = thrust
        self.burn_time = burn_time
        self.launch_angle = launch_angle

        # Position
        self.x = 0.0
        self.y = 0.0

        # Velocity
        self.velocity_x = 0.0
        self.velocity_y = 0.0