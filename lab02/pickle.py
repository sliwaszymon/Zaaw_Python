import pickle


class Point(object):
    x: float
    y: float

    def __init__(self, x: float, y: float) -> None:
        self.x = x
        self.y = y

    def __str__(self) -> str:
        return f'<{self.x}, {self.y}>'

    def move(self, delta_x: float, delta_y: float) -> None:
        self.x += delta_x
        self.y += delta_y


class NamedPoint(Point):
    nazwa: str

    def __init__(self, x: float, y: float, nazwa: str) -> None:
        # Point.__init__(self, x, y)
        super().__init__(x, y)
        self.nazwa = nazwa

    def __str__(self) -> str:
        return f'{self.nazwa}: ({self.x}, {self.y})'

    def __del__(self) -> None:
        self.nazwa = ""


def main() -> None:
    points = [
        Point(2, 4),
        Point(7, 11),
        NamedPoint(3, 5, 'Nazwany punkt 1'),
        NamedPoint(3, 5, 'Nazwany punkt 2')
    ]

    with open('punkty.pkl', 'wb') as pickle_file:
        pickle.dump(points, pickle_file)


if __name__ == '__main__':
    main()
