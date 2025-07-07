from src.car import Position, Direction, Car
from src.field import Field
from typing import List, TypedDict
from dataclasses import dataclass

class FinalPosition(TypedDict):
    car_name: str
    position: Position

@dataclass
class SimulationResult:
    final_positions: List[FinalPosition]
    collisions: List[Position]


class Simulation:
    def __init__(self, field: Field):
        self.field = field

    def run(self) -> SimulationResult:
        if not self.field.cars:
            return SimulationResult([],[])
        number_of_steps = max(len(car.commands) for car in self.field.cars)
        collisions: List[Position] = []
        for step in range(number_of_steps):
            for car in self.field.cars:
                if car.is_collided:
                    continue
                if step < len(car.commands):
                    command = car.commands[step]
                    if command == 'F':
                        next_position, present_car = self._get_car_next_position(car)
                        # ignore out of bounds action
                        if not self.field.is_valid_position(next_position):
                            continue
                        if self.field.is_car_at_position(next_position):
                            car.is_collided = True
                            present_car.is_collided = True
                            collisions.append(next_position)
                    car.move(command)
        final_positions = [FinalPosition(car_name=car.name, position=car.position) for car in self.field.cars]
        return SimulationResult(final_positions, collisions)


    @staticmethod
    def _get_car_next_position(car: Car) -> Position:
        next_position = Position(car.position.x, car.position.y)
        if car.direction == Direction.NORTH:
            next_position.y += 1
        elif car.direction == Direction.SOUTH:
            next_position.y -= 1
        elif car.direction == Direction.EAST:
            next_position.x += 1
        elif car.direction == Direction.WEST:
            next_position.x -= 1
        return next_position