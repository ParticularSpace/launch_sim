import math
import matplotlib.pyplot as plt


class RealTimeVisualizer:

    def __init__(self, update_every=10):

        # Only redraw every N physics steps.
        # Physics still runs at the full time_step.
        self.update_every = update_every
        self.step_count = 0

        plt.ion()

        self.figure, self.axes = plt.subplots(
            2,
            2,
            figsize=(12, 8)
        )

        # TRAJECTORY
        self.trajectory_axis = self.axes[0][0]

        # Complete path traveled so far
        self.trajectory_line, = self.trajectory_axis.plot(
            [],
            [],
            label="Flight Path"
        )

        # Moving rocket point
        self.rocket_point, = self.trajectory_axis.plot(
            [],
            [],
            marker="o",
            markersize=8,
            linestyle="None",
            label="Rocket"
        )

        self.trajectory_axis.set_title(
            "Rocket Flight Path"
        )

        self.trajectory_axis.set_xlabel(
            "Horizontal Distance (m)"
        )

        self.trajectory_axis.set_ylabel(
            "Altitude (m)"
        )

        self.trajectory_axis.grid()

        self.trajectory_axis.legend()

        # ALTITUDE
        self.altitude_axis = self.axes[0][1]

        self.altitude_line, = self.altitude_axis.plot(
            [],
            []
        )

        self.altitude_axis.set_title(
            "Altitude vs Time"
        )

        self.altitude_axis.set_xlabel(
            "Time (s)"
        )

        self.altitude_axis.set_ylabel(
            "Altitude (m)"
        )

        self.altitude_axis.grid()

        # VELOCITY
        self.velocity_axis = self.axes[1][0]

        self.velocity_line, = self.velocity_axis.plot(
            [],
            []
        )

        self.velocity_axis.set_title(
            "Velocity vs Time"
        )

        self.velocity_axis.set_xlabel(
            "Time (s)"
        )

        self.velocity_axis.set_ylabel(
            "Speed (m/s)"
        )

        self.velocity_axis.grid()

        # ACCELERATION
        self.acceleration_axis = self.axes[1][1]

        self.acceleration_line, = self.acceleration_axis.plot(
            [],
            []
        )

        self.acceleration_axis.set_title(
            "Acceleration vs Time"
        )

        self.acceleration_axis.set_xlabel(
            "Time (s)"
        )

        self.acceleration_axis.set_ylabel(
            "Acceleration (m/s²)"
        )

        self.acceleration_axis.grid()


        plt.tight_layout()


    def update(self, simulation):

        self.step_count += 1

        # Don't redraw matplotlib on every physics calculation.
        if self.step_count % self.update_every != 0:
            return

        rocket = simulation.rocket

        # CALCULATE SPEED HISTORY
        speed_points = []

        for vx, vy in zip(
            simulation.velocity_x_points,
            simulation.velocity_y_points
        ):

            speed = math.sqrt(
                vx ** 2 +
                vy ** 2
            )

            speed_points.append(speed)

        # CALCULATE ACCELERATION HISTORY
        acceleration_points = []

        for ax, ay in zip(
            simulation.acceleration_x_points,
            simulation.acceleration_y_points
        ):

            acceleration = math.sqrt(
                ax ** 2 +
                ay ** 2
            )

            acceleration_points.append(
                acceleration
            )

        # UPDATE TRAJECTORY PATH
        self.trajectory_line.set_data(
            simulation.x_points,
            simulation.y_points
        )

        # UPDATE MOVING ROCKET POINT
        self.rocket_point.set_data(
            [rocket.x],
            [rocket.y]
        )

        # Update graph bounds as rocket moves
        self.trajectory_axis.relim()
        self.trajectory_axis.autoscale_view()

        # UPDATE ALTITUDE
        self.altitude_line.set_data(
            simulation.time_points,
            simulation.y_points
        )

        self.altitude_axis.relim()
        self.altitude_axis.autoscale_view()

        # UPDATE VELOCITY
        self.velocity_line.set_data(
            simulation.time_points,
            speed_points
        )

        self.velocity_axis.relim()
        self.velocity_axis.autoscale_view()

        # UPDATE ACCELERATION
        self.acceleration_line.set_data(
            simulation.time_points,
            acceleration_points
        )

        self.acceleration_axis.relim()
        self.acceleration_axis.autoscale_view()

        # CURRENT FLIGHT DATA
        current_speed = math.sqrt(
            rocket.velocity_x ** 2 +
            rocket.velocity_y ** 2
        )

        current_acceleration = math.sqrt(
            rocket.acceleration_x ** 2 +
            rocket.acceleration_y ** 2
        )

        self.figure.suptitle(
            f"Time: {simulation.time:.2f} s   |   "
            f"Altitude: {rocket.y:.1f} m   |   "
            f"Speed: {current_speed:.1f} m/s   |   "
            f"Acceleration: {current_acceleration:.1f} m/s²"
        )

        # Draw updated frame
        self.figure.canvas.draw_idle()
        self.figure.canvas.flush_events()

        plt.pause(0.001)


    def show(self):

        plt.ioff()
        plt.show()