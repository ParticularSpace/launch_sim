from physics import (
    calculate_thrust_components,
    calculate_gravity_force,
    calculate_air_density,
    calculate_drag_components,
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

        # SIMULATION HISTORY
        self.time_points = []

        self.x_points = []
        self.y_points = []

        self.velocity_x_points = []
        self.velocity_y_points = []

        self.acceleration_x_points = []
        self.acceleration_y_points = []


    # FORCE CALCULATIONS

    def calculate_forces(self):

        # THRUST
        if self.time <= self.rocket.burn_time:

            thrust_x, thrust_y = calculate_thrust_components(
                self.rocket.thrust,
                self.rocket.launch_angle
            )
        else:

            thrust_x = 0.0
            thrust_y = 0.0


        # GRAVITY
        gravity_force = calculate_gravity_force(
            self.rocket.mass
        )

        # ATMOSPHERE
        air_density = calculate_air_density(
            self.rocket.y
        )

        # DRAG
        drag_x, drag_y = calculate_drag_components(
            self.rocket.velocity_x,
            self.rocket.velocity_y,
            air_density,
            self.rocket.drag_coefficient,
            self.rocket.area
        )

        # NET FORCE
        net_force_x = (
            thrust_x +
            drag_x
        )

        net_force_y = (
            thrust_y +
            drag_y -
            gravity_force
        )

        return net_force_x, net_force_y


    # NUMERICAL UPDATE
    def update_rocket(self):

        net_force_x, net_force_y = self.calculate_forces()

        # ----------------------------------------------------
        # ACCELERATION
        # F = ma -> a = F/m
        # ----------------------------------------------------

        self.rocket.acceleration_x = calculate_acceleration(
            net_force_x,
            self.rocket.mass
        )

        self.rocket.acceleration_y = calculate_acceleration(
            net_force_y,
            self.rocket.mass
        )


        # VELOCITY
        self.rocket.velocity_x = update_velocity(
            self.rocket.velocity_x,
            self.rocket.acceleration_x,
            self.time_step
        )

        self.rocket.velocity_y = update_velocity(
            self.rocket.velocity_y,
            self.rocket.acceleration_y,
            self.time_step
        )


        # POSITION
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

    # DATA RECORDING
    def record_data(self):

        self.time_points.append(
            self.time
        )


        self.x_points.append(
            self.rocket.x
        )

        self.y_points.append(
            self.rocket.y
        )


        self.velocity_x_points.append(
            self.rocket.velocity_x
        )

        self.velocity_y_points.append(
            self.rocket.velocity_y
        )


        self.acceleration_x_points.append(
            self.rocket.acceleration_x
        )

        self.acceleration_y_points.append(
            self.rocket.acceleration_y
        )


    # RUN SIMULATION
    def run(self, visualizer=None):

        while True:

            # Update physics
            self.update_rocket()

            # Record current state
            self.record_data()


            # REAL-TIME VISUALIZATION
            if visualizer is not None:

                visualizer.update(
                    self
                )


            # Advance time
            self.time += self.time_step

            # ROCKET RETURNS TO EARTH
            if (
                self.rocket.y < 0
                and self.time > self.rocket.burn_time
            ):

                print("Rocket returned to Earth.")

                break


            # ROCKET REACHES SPACE
            if self.rocket.y >= SPACE_ALTITUDE:

                print("Rocket reached space!")

                break