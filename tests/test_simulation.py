from src.car import Car, Position, Direction
from src.field import Field
from src.simulation import Simulation

class TestSimulation:
    def setup_method(self):
        self.field = Field(5, 5)

    def test_run_no_cars(self):
        sim = Simulation(self.field)
        sim.run()  # Should not raise or do anything
        assert self.field.cars == []

    def test_run_no_collisions(self):
        car1 = Car("A", Position(0, 0), Direction.NORTH, "F")
        car2 = Car("B", Position(1, 0), Direction.NORTH, "F")
        self.field.add_car(car1)
        self.field.add_car(car2)
        sim = Simulation(self.field)
        sim.run()
        assert not car1.is_collided
        assert not car2.is_collided
        assert car1.position.y == 1
        assert car2.position.y == 1

    def test_run_with_collision(self):
        car1 = Car("A", Position(0, 0), Direction.EAST, "F")
        car2 = Car("B", Position(1, 0), Direction.WEST, "F")
        self.field.add_car(car1)
        self.field.add_car(car2)
        sim = Simulation(self.field)
        sim.run()
        assert car1.is_collided
        assert car2.is_collided
        assert car1.collision_step == 1
        assert car2.collision_step == 1

    def test_run_out_of_bounds(self):
        car = Car("A", Position(0, 0), Direction.WEST, "F")
        self.field.add_car(car)
        sim = Simulation(self.field)
        sim.run()
        # Car should not move out of bounds
        assert car.position.x == 0
        assert car.position.y == 0
        assert not car.is_collided

    def test_run_car_with_no_commands(self):
        car = Car("A", Position(0, 0), Direction.NORTH, "")
        self.field.add_car(car)
        sim = Simulation(self.field)
        sim.run()
        assert car.position.x == 0
        assert car.position.y == 0
        assert not car.is_collided

    def test_run_multiple_steps(self):
        car = Car("A", Position(0, 0), Direction.NORTH, "FFRFF")
        self.field.add_car(car)
        sim = Simulation(self.field)
        sim.run()
        # After FFRFF: (0,0)->(0,1)->(0,2)->turn right->(1,2)->(2,2)
        assert car.position.x == 2
        assert car.position.y == 2
        assert not car.is_collided

    def test_run_collision_after_multiple_steps(self):
        car1 = Car("A", Position(0, 0), Direction.NORTH, "FF")
        car2 = Car("B", Position(0, 2), Direction.SOUTH, "FF")
        self.field.add_car(car1)
        self.field.add_car(car2)
        sim = Simulation(self.field)
        sim.run()
        # Both cars should collide at (0,1) on step 1
        assert car1.is_collided
        assert car2.is_collided
        assert car1.collision_step == 1
        assert car2.collision_step == 1
