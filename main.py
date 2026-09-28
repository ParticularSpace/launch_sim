from rocket import Rocket
from simulation import Simulation
from visualization import RealTimeVisualizer


def main():

    # ROCKET PARAMETERS
    mass = 500.0
    thrust = 15_000.0
    burn_time = 12.0
    launch_angle = 85.0

    drag_coefficient = 0.4
    area = 0.5

    # Numerical simulation time step
    time_step = 0.01

    # CREATE ROCKET
    rocket = Rocket(
        mass=mass,
        thrust=thrust,
        burn_time=burn_time,
        launch_angle=launch_angle,
        drag_coefficient=drag_coefficient,
        area=area
    )

    # CREATE SIMULATION
    simulation = Simulation(
        rocket=rocket,
        time_step=time_step
    )

    # CREATE LIVE VISUALIZER
    visualizer = RealTimeVisualizer(
        update_every=10
    )

    # RUN SIMULATION
    simulation.run(
        visualizer=visualizer
    )

    # Keep final graph open after simulation ends
    visualizer.show()

if __name__ == "__main__":
    main()