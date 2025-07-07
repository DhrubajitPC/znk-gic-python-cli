from enum import Enum


class Position:
    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y

    def __repr__(self):
        return f"Position(x={self.x}, y={self.y})"

class Direction(Enum):
    NORTH = "N"
    SOUTH = "S"
    EAST = "E"
    WEST = "W"

class Car:
    def __init__(self, name: str, position: Position, direction: Direction, commands: str):
        if not name:
            raise ValueError("Name cannot be empty.")
        self.name = name
        self.position = position
        self.direction = direction
        self.commands = list(commands)
        self.is_collided = False

    def turn_left(self):
        if self.direction == Direction.NORTH:
            self.direction = Direction.WEST
        elif self.direction == Direction.WEST:
            self.direction = Direction.SOUTH
        elif self.direction == Direction.SOUTH:
            self.direction = Direction.EAST
        elif self.direction == Direction.EAST:
            self.direction = Direction.NORTH

    def turn_right(self):
        if self.direction == Direction.NORTH:
            self.direction = Direction.EAST
        elif self.direction == Direction.EAST:
            self.direction = Direction.SOUTH
        elif self.direction == Direction.SOUTH:
            self.direction = Direction.WEST
        elif self.direction == Direction.WEST:
            self.direction = Direction.NORTH

    def move_forward(self):
        if self.direction == Direction.NORTH:
            self.position.y += 1
        elif self.direction == Direction.SOUTH:
            self.position.y -= 1
        elif self.direction == Direction.EAST:
            self.position.x += 1
        elif self.direction == Direction.WEST:
            self.position.x -= 1

    def move(self, command: str):
        valid_commands = ['F', 'L', 'R']
        if command not in valid_commands:
            raise ValueError(f"Invalid command '{command}' for car '{self.name}'.")
        if command == 'F':
            self.move_forward()
        elif command == 'L':
            self.turn_left()
        elif command == 'R':
            self.turn_right()

    def get_position(self) -> Position:
        return self.position


    def set_collision_true(self):
        self.is_collided = True

    def __str__(self) -> str:
        """String representation of the car with commands"""
        commands_str = "".join(self.commands)
        return f"{self.name}, ({self.position.x},{self.position.y}) {self.direction.value}, {commands_str}"