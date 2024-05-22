import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import os

GRAVITY = 9.8

class TrajectorySimulation:
    def __init__(self, initial_vx, initial_vy, duration, time_step=1.0):
        """
        Initializes the simulation with initial velocities, duration, and time step.

        :param initial_vx: Initial velocity in the x direction
        :param initial_vy: Initial velocity in the y direction
        :param duration: Duration of the simulation
        :param time_step: Time step for the simulation (default is 1.0)
        """
        self.time = np.arange(0, duration + time_step, time_step)
        self.vx = initial_vx - GRAVITY * self.time
        self.vy = initial_vy
        self.x = initial_vx * self.time - 0.5 * GRAVITY * self.time ** 2
        self.y = initial_vy * self.time
        results = {
            'Time': self.time,
            'X Position': self.x,
            'Y Position': self.y,
            'X Velocity': self.vx,
            'Y Velocity': self.vy
        }
        self.results_df = pd.DataFrame(results)

    def display_results(self):
        print(self.results_df)

    def save_results(self, filename='simulation_results.csv'):
        self.results_df.to_csv(filename, index=False)

    def plot_trajectory(self, save_path=None):
        plt.style.use('default')
        fig, ax = plt.subplots(figsize=(12, 7), dpi=100)

        ax.plot(self.results_df["Y Position"], self.results_df["X Position"], color='tab:red', label='Trajectory')

        ax.set_title('Trajectory Simulation', fontsize=24, family='Times New Roman')
        ax.set_xlabel('Y Position', fontsize=24, family='Times New Roman')
        ax.set_ylabel('X Position', fontsize=24, family='Times New Roman')

        ax.tick_params(axis='both', which='major', labelsize=14)
        plt.legend()
        plt.grid()
        plt.show()

        if save_path:
            fig.savefig(f'{save_path}.png', dpi=300, format='png')

if __name__ == '__main__':
    simulation = TrajectorySimulation(initial_vx=100, initial_vy=15, duration=15, time_step=1.0)

    simulation.display_results()
    simulation.save_results(filename='trajectory_results.csv')
    simulation.plot_trajectory(save_path='trajectory_plot')
