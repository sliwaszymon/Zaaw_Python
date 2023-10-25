class Car:
    fuel_efficiency: int | float
    fuel_capacity: int | float
    _actual_fuel: int | float

    def __init__(self, fuel_efficiency: int | float, fuel_capacity: int | float) -> None:
        self.fuel_efficiency = fuel_efficiency
        self.fuel_capacity = fuel_capacity
        self._actual_fuel = 0

    def drive(self, distance: int | float) -> None:  # distance in meters
        distance_could_drive = self._actual_fuel * self.fuel_efficiency * 1000
        if distance_could_drive >= distance:
            self._actual_fuel -= (distance / 1000) / self.fuel_efficiency
            print('Car arrived the target.')
        else:
            self._actual_fuel = 0
            print(f'Car has no more fuel and stopped {distance - distance_could_drive:.2}km before the target.')

    def get_fuel_level(self) -> int | float:
        return self._actual_fuel

    def add_fuel(self, fuel: int | float) -> None:
        if fuel + self._actual_fuel >= self.fuel_capacity:
            self._actual_fuel = self.fuel_capacity
        else:
            self._actual_fuel += fuel

