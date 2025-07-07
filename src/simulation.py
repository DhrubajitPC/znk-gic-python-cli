from src.car import Position, Direction, Car
from src.field import Field


class Simulation:
    def __init__(self, field: Field):
        self.field = field

    def run(self):
        if not self.field.cars:
            return
        number_of_steps = max(len(car.commands) for car in self.field.cars)
        for step in range(number_of_steps):
            for car in self.field.cars:
                if car.is_collided:
                    continue
                if step < len(car.commands):
                    command = car.commands[step]
                    if command == 'F':
                        next_position = self._get_car_next_position(car)
                        is_car_present, present_cars = self.field.is_car_at_position(next_position)
                        # ignore out of bounds action
                        if not self.field.is_valid_position(next_position):
                            continue
                        if is_car_present:
                            car.set_collision_true(step)
                            [present_car.set_collision_true(step) for present_car in present_cars]
                    car.move(command)

    def _get_car_next_position(self, car: Car) -> Position:
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