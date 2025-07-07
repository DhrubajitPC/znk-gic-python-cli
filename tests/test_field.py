from src.car import Position, Car, Direction
from src.field import Field


class TestField:
    """Test the Field class"""

    def setup_method(self):
        """Setup method to initialize the field"""
        self.field = Field(10, 10)

    def test_field_initialization(self):
        """Test field initialization"""
        assert self.field.width == 10
        assert self.field.height == 10
        assert self.field.cars == []

    def test_add_car_valid(self):
        """Test adding a car with valid parameters"""
        position = Position(5, 5)
        car = Car(name="TestCar", position=position, direction=Direction.NORTH, commands="")
        self.field.add_car(car)

        assert len(self.field.cars) == 1
        assert self.field.cars[0] == car

    def test_add_car_invalid_position(self):
        """Test adding a car with an invalid position"""
        position = Position(15, 15)
        car = Car(name="TestCar", position=position, direction=Direction.NORTH, commands="")
        try:
            self.field.add_car(car)
        except ValueError as e:
            assert str(e) == "Car position is out of bounds."

    def test_add_car_duplicate_position(self):
        """Test adding a car at a position where another car already exists"""
        position = Position(5, 5)
        car1 = Car(name="TestCar1", position=position, direction=Direction.NORTH, commands="")
        self.field.add_car(car1)

        car2 = Car(name="TestCar2", position=position, direction=Direction.SOUTH, commands="")
        try:
            self.field.add_car(car2)
        except ValueError as e:
            assert str(e) == "A car already exists at this position."

    def test_add_car_duplicate_name(self):
        """Test adding a car with a name that already exists"""
        position = Position(5, 5)
        car1 = Car(name="TestCar", position=position, direction=Direction.NORTH, commands="")
        self.field.add_car(car1)

        car2 = Car(name="TestCar", position=Position(6, 6), direction=Direction.SOUTH, commands="")
        try:
            self.field.add_car(car2)
        except ValueError as e:
            assert str(e) == "A car with this name already exists."

    def test_field_is_crash_at_position(self):
        """Test if the field detects a crash at a position"""
        position = Position(5, 5)
        assert not self.field.is_crash_at_position(position)

        # Add a car at the position
        car = Car(name="TestCar", position=position, direction=Direction.NORTH, commands="")
        car.set_collision()
        self.field.add_car(car)

        assert self.field.is_crash_at_position(position)

