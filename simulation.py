from physics import (
    calculate_thrust_components,
    calculate_gravity_force,
    calculate_acceleration,
    update_velocity,
    update_position,
)


SPACE_ALTITUDE = 100_000  # meters


class Simulation:

    def __init__(self, rocket, time_step=0.01):
        self.rocket = rocket
        self.time_step = time_step

        self.time = 0.0

        # Simulation history
        self.time_points = []

        self.x_points = []
        self.y_points = []

        self.velocity_x_points = []
        self.velocity_y_points = []


    def calculate_forces(self):
        """
        Calculate the net forces acting on the rocket.
        """

        # Engine produces thrust only during burn time
        if self.time <= self.rocket.burn_time:

            thrust_x, thrust_y = calculate_thrust_components(
                self.rocket.thrust,
                self.rocket.launch_angle
            )

        else:

            thrust_x = 0.0
            thrust_y = 0.0


        # Gravity always acts downward
        gravity_force = calculate_gravity_force(
            self.rocket.mass
        )


        # Net forces
        net_force_x = thrust_x

        net_force_y = thrust_y - gravity_force


        return net_force_x, net_force_y


    def update_rocket(self):
        """
        Advance the rocket forward by one time step.
        """

        # Calculate forces
        net_force_x, net_force_y = self.calculate_forces()

        # Calculate acceleration
        # F = ma
        # a = F / m
        acceleration_x = calculate_acceleration(
            net_force_x,
            self.rocket.mass
        )

        acceleration_y = calculate_acceleration(
            net_force_y,
            self.rocket.mass
        )

        # Update velocity
        # v_new = v_old + a * dt

        self.rocket.velocity_x = update_velocity(
            self.rocket.velocity_x,
            acceleration_x,
            self.time_step
        )

        self.rocket.velocity_y = update_velocity(
            self.rocket.velocity_y,
            acceleration_y,
            self.time_step
        )

        # Update position
        # x_new = x_old + v * dt

        self.rocket.x = update_position(
            self.rocket.x,
            self.rocket.velocity_x,
            self.time_step
        )

        self.rocket.y = update_position(
            self.rocket.y,
            self.rocket.velocity_y,
            self.time_step
        )


    def record_data(self):
        """
        Store the current rocket state so it
        can be graphed later.
        """

        self.time_points.append(self.time)

        self.x_points.append(self.rocket.x)
        self.y_points.append(self.rocket.y)

        self.velocity_x_points.append(
            self.rocket.velocity_x
        )

        self.velocity_y_points.append(
            self.rocket.velocity_y
        )


    def run(self):
        """
        Run the launch simulation until the rocket
        either returns to Earth or reaches space.
        """

        while True:

            # Advance rocket physics
            self.update_rocket()

            # Save current state
            self.record_data()

            # Advance simulation time
            self.time += self.time_step

            # Rocket returns to the ground
            if (
                self.rocket.y < 0
                and self.time > self.rocket.burn_time
            ):

                print("Rocket returned to Earth.")
                break

            # Rocket reaches 100 km altitude
            if self.rocket.y >= SPACE_ALTITUDE:

                print("Rocket reached space!")
                break