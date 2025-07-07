from src.car import Car,Position, Direction

class TestCar:
    def setup_method(self):
        self.position = Position(0, 0)
        self.direction = Direction.NORTH
        self.car = Car(name="TestCar", position=self.position, direction=self.direction, commands="FFLFR")

    def test_car_initialization(self):
        """Test car initialization"""
        assert self.car.name == "TestCar"
        assert self.car.position == self.position
        assert self.car.direction == self.direction
        assert self.car.commands == ['F', 'F', 'L', 'F', 'R']
        assert not self.car.is_collided

    def test_turn_left(self):
        """Test car turns left correctly"""
        self.car.turn_left()
        assert self.car.direction == Direction.WEST

        self.car.turn_left()
        assert self.car.direction == Direction.SOUTH

        self.car.turn_left()
        assert self.car.direction == Direction.EAST

        self.car.turn_left()
        assert self.car.direction == Direction.NORTH

    def test_turn_right(self):
        """Test car turns right correctly"""
        self.car.turn_right()
        assert self.car.direction == Direction.EAST

        self.car.turn_right()
        assert self.car.direction == Direction.SOUTH

        self.car.turn_right()
        assert self.car.direction == Direction.WEST

        self.car.turn_right()
        assert self.car.direction == Direction.NORTH

    def test_car_forward_movement(self):
        """Test car moves forward in the current direction"""
        self.car.move_forward()
        p = Position(0, 1)
        assert self.car.position.x == p.x
        assert self.car.position.y == p.y

        self.car.direction = Direction.EAST
        self.car.move_forward()
        p = Position(1, 1)
        assert self.car.position.x == p.x
        assert self.car.position.y == p.y

        self.car.direction = Direction.SOUTH
        self.car.move_forward()
        p = Position(1, 0)
        assert self.car.position.x == p.x
        assert self.car.position.y == p.y

        self.car.direction = Direction.WEST
        self.car.move_forward()
        p = Position(0, 0)
        assert self.car.position.x == p.x
        assert self.car.position.y == p.y

    def test_car_set_collision(self):
        """Test car collision state"""
        self.car.set_collision_true()
        assert self.car.is_collided