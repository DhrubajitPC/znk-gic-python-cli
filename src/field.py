from typing import List

from src.car import Car, Position


class Field:
    def __init__(self, width: int, height: int):
        if width <= 0 or height <=  0:
            raise ValueError("Width and height must be positive integers.")
        self.width = width
        self.height = height
        self.cars: List[Car] = []

    def is_valid_position(self, position: Position) -> bool:
        return 0 <= position.x < self.width and 0 <= position.y < self.height

    def add_car(self, car: Car):
        if not self.is_valid_position(car.get_position()):
            raise ValueError("Car position is out of bounds.")
        for existing_car in self.cars:
            if existing_car.get_position() == car.get_position():
                raise ValueError("A car already exists at this position.")
            if existing_car.name == car.name:
                raise ValueError("A car with this name already exists.")
        self.cars.append(car)

    def is_car_at_position(self, position: Position) -> (bool, Car):
        for car in self.cars:
            if car.position.x == position.x and car.position.y == position.y:
                return True, car
        return False, None

    def get_cars_list(self) -> List[Car]:
        return self.cars