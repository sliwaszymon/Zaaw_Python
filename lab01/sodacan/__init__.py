from math import pi


class SodaCan:
    height: int | float
    radius: int | float

    def __init__(self, height: int | float, radius: int | float):
        self.height = height
        self.radius = radius
        self.base_surface = pi * radius ** 2
        self.side_surface = 2 * pi * radius * height
        self.volume = self.base_surface * height

    def get_surface_area(self) -> float:
        return 2 * self.base_surface + self.side_surface

    def get_volume(self) -> float:
        return self.volume
