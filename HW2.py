import math

class RoboticSystem:
    def __init__(self, start_x, start_y, start_angle):
        """
        Initializes the robotic system with starting position and angle.

        :param start_x: Initial X position
        :param start_y: Initial Y position
        :param start_angle: Initial angle relative to the X axis, positive in counterclockwise direction
        """
        self.x = start_x
        self.y = start_y
        self.angle = start_angle

        self.engine_on = False
        self.power_on = False
        self.elapsed_time = 0

        print(f'Initial position: ({self.x}, {self.y}), angle: {self.angle} degrees, time: {self.elapsed_time}')

    def toggle_engine(self, on=False):
        """
        Toggles the diesel engine status.

        :param on: True to turn on, False to turn off
        """
        self.engine_on = on
        status = "ON" if on else "OFF"
        print(f'Diesel engine is {status}')

    def toggle_power(self, on=False, check=False):
        """
        Toggles the power switch status and optionally checks current status.

        :param on: True to turn on, False to turn off
        :param check: If True, prints the current status of engine and power switch
        """
        self.power_on = on
        status = "ON" if on else "OFF"
        print(f'Power switch is {status}')

        if check:
            self.toggle_engine(self.engine_on)
            self.toggle_power(self.power_on)

    def move_robot(self, move_speed, move_duration, rotate_speed, rotate_duration, halt_duration):
        """
        Simulates the robot's movement and rotation.

        :param move_speed: Speed at which the robot moves forward
        :param move_duration: Duration of forward movement
        :param rotate_speed: Speed at which the robot rotates counterclockwise
        :param rotate_duration: Duration of rotation
        :param halt_duration: Duration of halt after movement
        """
        if not self.engine_on:
            print('Diesel engine is OFF')
        elif not self.power_on:
            print('Power switch is OFF')
        else:
            print('Diesel engine and power switch are ON')
            self.angle += rotate_speed * rotate_duration
            delta_x = move_speed * move_duration * math.cos(math.radians(self.angle))
            delta_y = move_speed * move_duration * math.sin(math.radians(self.angle))
            self.x += delta_x
            self.y += delta_y
            self.elapsed_time += move_duration + rotate_duration + halt_duration

        print(f'Current position: ({self.x}, {self.y}), angle: {self.angle} degrees, time: {self.elapsed_time}')

if __name__ == '__main__':
    robot = RoboticSystem(0, 0, 0)
    robot.move_robot(0, 0, 5, 9, 0)
    robot.toggle_power(False, check=True)
    robot.toggle_engine(True)
    robot.toggle_power(True)
    robot.move_robot(0, 0, 5, 9, 0)
    robot.move_robot(2, 1, 0, 0, 1)
