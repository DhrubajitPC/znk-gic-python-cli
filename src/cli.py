import sys
from typing import List

from src.car import Position, Direction, Car
from src.field import Field
from enum import Enum

from src.simulation import Simulation

init_options = ["Add a car to field", "Run simulation"]
end_options = ["Start over", "Exit"]

class States(Enum):
    START = "start"
    INPUT = "input"
    RUN = "run"
    END = "end"

class Cli:
    def __init__(self):
        self.field = None
        self.running = False
        self.state = States.START

    def run(self):
        while True:
            if self.state == States.START:
                print("Welcome to Auto Driving Car Simulation!\n")
                self._create_field()
                self._show_menu(init_options)
            elif self.state == States.INPUT:
                self._print_status()
                self._show_menu(init_options)
            elif self.state == States.RUN:
                self._simulate()
            elif self.state == States.END:
                self._print_simulation_result()

    def _print_status(self):
        print("Your current list of cars are: \n")
        cars = self.field.get_cars_list()
        for car in cars:
           print(f"- {car.name}, ({car.get_position().x}, {car.get_position().y}) {car.direction.value}, {"".join(car.commands)}\n")

    def _create_field(self):
        prompt = "Please enter the width and height of the simulation field in x y format:\n"
        dimensions = None
        while not dimensions:
            print(prompt)
            try:
                dimensions = input().strip().split()
                if len(dimensions) != 2:
                    raise ValueError("invalid input")

                width, height = int(dimensions[0]), int(dimensions[1])
                self.field = Field(width, height)
                print(f"You have created a field of {width} x {height}.\n")

            except ValueError as e:
                print(f"Invalid input. \n{e}")
                dimensions = None

    def _print_simulation_result(self):
        self._print_status()
        print("\nAfter simulation, the result is:\n")
        for car in self.field.cars:
            if car.is_collided:
                _, collided_cars = self.field.is_car_at_position(car.position)
                collided_cars = [c for c in collided_cars if c.name != car.name]
                collided_cars_str = ', '.join([c.name for c in collided_cars])
                print(f"- {car.name}, collides with {collided_cars_str} at ({car.position.x}, {car.position.y}) at step {car.collision_step}")
            else:
                print(f"- {car.name}, ({car.get_position().x}, {car.get_position().y}) {car.direction.value}\n")

        self._show_menu(end_options)


    def _show_menu(self, options: List[str]):
        print(f"Please choose from the following options:\n[1] {options[0]}\n[2] {options[1]}\n")
        try:
            choice = int(input().strip())
            if choice == 1 and self.state == States.END:
                self.state = States.START
                self.field = None
            elif choice == 1:
                self._add_car()
                self.state = States.INPUT
            elif choice == 2 and self.state == States.END:
                print("Thank you for running the simulation. Goodbye!")
                sys.exit(0)
            elif choice == 2:
                self.state = States.RUN
            else:
                print("Invalid choice. Please select 1 or 2.")
                self._show_menu(options)
        except ValueError as e:
            print(f"Invalid input: {e}. Please enter a number 1 or 2.")
            return
        except KeyboardInterrupt:
            print("\nGoodbye!")
            sys.exit(0)

    def _add_car(self):
        car_name=self._get_car_name()
        car_position, car_direction = self._get_car_position_direction(car_name)
        car_commands = self._get_car_commands(car_name)
        car = Car(car_name, car_position, car_direction, car_commands)
        self.field.add_car(car)

    def _get_car_name(self) -> str:
        car_name = None
        while not car_name:
            print("Please enter the name of the car:\n")
            car_name = input().strip()
            if not car_name:
                print("Car name cannot be empty.")
                continue
            if any(car.name == car_name for car in self.field.get_cars_list()):
                print(f"A car with the name '{car_name}' already exists. Please choose a different name.")
                car_name = ""
                continue
        return car_name

    def _get_car_position_direction(self, car_name: str) -> (Position, Direction):
        car_position = None
        car_direction = None
        while not car_position and not car_direction:
            print(f"Please enter initial position of car {car_name} in x y Direction format:\n")
            user_input = input().strip().split()
            if len(user_input) != 3:
                print("Please enter exactly three values: x, y, and direction (N, S, E, W).")
                continue
            try:
                x, y = int(user_input[0]), int(user_input[1])
                direction = user_input[2].upper()
                if direction not in ['N', 'S', 'E', 'W']:
                    raise ValueError("Direction must be one of N, S, E, W.")
                car_position = Position(x, y)
                car_direction = Direction(direction)
                if not self.field.is_valid_position(car_position):
                    raise ValueError("Car position is out of bounds.")
                is_existing_car, _ = self.field.is_car_at_position(car_position)
                if is_existing_car:
                    raise ValueError("A car already exists at this position.")
            except ValueError as e:
                print(f"Invalid input: {e}. Please try again.")
                car_position = None
                car_direction = None
        return car_position, car_direction

    def _get_car_commands(self, car_name: str) -> str:
        valid_commands = ['F', 'L', 'R']
        command = None
        while not command:
            print(f"Please enter the commands for car {car_name}:")
            command = input().strip().upper()
            for cmd in command:
                if cmd not in valid_commands:
                    print(f"Invalid command '{cmd}'. Valid commands are: {', '.join(valid_commands)}")
                    command = None
                    continue
        return command

    def _simulate(self):
        simulation = Simulation(self.field)
        simulation.run()
        self.state = States.END
