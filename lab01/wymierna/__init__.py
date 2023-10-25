class Wymierna:
    _p: int
    _q: int

    def __init__(self, licznik: int = 0, mianownik: int = 1) -> None:
        nwd = self.nwd(abs(licznik), abs(mianownik))
        if mianownik < 0:
            self._p = -int(licznik / nwd)
            self._q = int(abs(mianownik) / nwd)
        else:
            self._p = int(licznik / nwd)
            self._q = int(mianownik / nwd)

    def get_licznik(self) -> int:
        return self._p

    def get_mianownik(self) -> int:
        return self._q

    def __repr__(self) -> str:
        return f'{self._p}/{self._q}'

    def __float__(self) -> float:
        return self._p / self._q

    def __add__(self, other: int | object) -> object:
        if isinstance(other, int):
            return Wymierna(self._p + (self._p * other), self._q)
        if isinstance(other, Wymierna):
            return Wymierna(self._p * other.get_mianownik() + other.get_licznik() * self._q,
                            self._q * other.get_mianownik())
        else:
            raise Exception('Substraction object is not instance of int or Wymierna')

    def __sub__(self, other: int | object) -> object:
        if isinstance(other, int):
            return Wymierna(self._p - (self._p * other), self._q)
        if isinstance(other, Wymierna):
            return Wymierna(self._p * other.get_mianownik() - other.get_licznik() * self._q,
                            self._q * other.get_mianownik())
        else:
            raise Exception('Substraction object is not instance of int or Wymierna')

    @staticmethod
    def nwd(a: int, b: int) -> int:
        while min(a, b) != 0:
            if a >= b:
                a = a % b
            else:
                b = b % a
        return max(a, b)
