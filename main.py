from rocket import Rocket
from simulation import Simulation

from visualization import (
    plot_trajectory,
    plot_altitude,
    plot_velocity
)


def main():

    # ROCKET DETAILS
    mass = 500.0             # kg
    thrust = 150000.0         # newtons extreme to space
    launch_angle = 85.0      # degrees
    burn_time = 12.0         # seconds
    time_step = 0.01         # seconds

    # CREATE ROCKET
    rocket = Rocket(
        mass=mass,
        thrust=thrust,
        burn_time=burn_time,
        launch_angle=launch_angle
    )


    # CREATE SIMULATION
    simulation = Simulation(
        rocket=rocket,
        time_step=0.01
    )

    # RUN
    simulation.run()

    # VISUALIZE RESULTS
    plot_trajectory(
        simulation.x_points,
        simulation.y_points
    )

    plot_altitude(
        simulation.time_points,
        simulation.y_points
    )

    plot_velocity(
        simulation.time_points,
        simulation.velocity_y_points
    )


if __name__ == "__main__":
    main()