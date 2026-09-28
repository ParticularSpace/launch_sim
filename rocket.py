class Rocket:

    def __init__(
        self,
        mass,
        thrust,
        burn_time,
        launch_angle,
        drag_coefficient,
        area
    ):

        # Physical properties
        self.mass = mass
        self.thrust = thrust
        self.burn_time = burn_time

        self.launch_angle = launch_angle

        self.drag_coefficient = drag_coefficient
        self.area = area


        # Position
        self.x = 0.0
        self.y = 0.0


        # Velocity
        self.velocity_x = 0.0
        self.velocity_y = 0.0


        # Acceleration
        self.acceleration_x = 0.0
        self.acceleration_y = 0.0