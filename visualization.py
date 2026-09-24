import matplotlib.pyplot as plt


def plot_trajectory(x_points, y_points):
    """
    Plot horizontal distance vs altitude.
    """

    plt.figure()

    plt.plot(
        x_points,
        y_points
    )

    plt.xlabel("Horizontal Distance (m)")
    plt.ylabel("Altitude (m)")

    plt.title("Rocket Launch Trajectory")

    plt.grid()

    plt.show()


def plot_altitude(time_points, y_points):
    """
    Plot altitude over time.
    """

    plt.figure()

    plt.plot(
        time_points,
        y_points
    )

    plt.xlabel("Time (s)")
    plt.ylabel("Altitude (m)")

    plt.title("Altitude vs Time")

    plt.grid()

    plt.show()


def plot_velocity(time_points, velocity_y_points):
    """
    Plot vertical velocity over time.
    """

    plt.figure()

    plt.plot(
        time_points,
        velocity_y_points
    )

    plt.xlabel("Time (s)")
    plt.ylabel("Vertical Velocity (m/s)")

    plt.title("Vertical Velocity vs Time")

    plt.grid()

    plt.show()