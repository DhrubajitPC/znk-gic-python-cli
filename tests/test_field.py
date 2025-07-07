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

    def test_field_is_car_at_position(self):
        """Test if the field detects a car at a position"""
        position = Position(5, 5)
        found, cars = self.field.is_car_at_position(position)
        assert not found
        assert cars == []

        # Add a car at the position
        car = Car(name="TestCar", position=position, direction=Direction.NORTH, commands="")
        self.field.add_car(car)
        found, cars = self.field.is_car_at_position(position)
        assert found
        assert car in cars

    def test_field_invalid_dimensions(self):
        """Test field initialization with invalid dimensions"""
        from pytest import raises
        with raises(ValueError):
            Field(0, 10)
        with raises(ValueError):
            Field(10, 0)
        with raises(ValueError):
            Field(-1, 5)

    def test_is_valid_position(self):
        """Test is_valid_position method"""
        assert self.field.is_valid_position(Position(0, 0))
        assert self.field.is_valid_position(Position(9, 9))
        assert not self.field.is_valid_position(Position(-1, 0))
        assert not self.field.is_valid_position(Position(0, -1))
        assert not self.field.is_valid_position(Position(10, 10))

    def test_get_cars_list(self):
        """Test get_cars_list method"""
        assert self.field.get_cars_list() == []
        car = Car(name="TestCar", position=Position(1, 1), direction=Direction.NORTH, commands="")
        self.field.add_car(car)
        assert car in self.field.get_cars_list()
