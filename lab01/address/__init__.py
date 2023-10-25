class Address:
    building_no: int
    street: str
    flat_no: int | None
    city: str
    postal_code: str

    def __init__(self, building_no: int, street: str, city: str, postal_code: str, flat_no: int = None):
        self.building_no = building_no
        self.street = street
        self.city = city
        self.postal_code = postal_code
        self.flat_no = flat_no

    # funkcje z reguły "nie gadają" no ale takie zadanie
    def show(self):
        if self.flat_no:
            print(f'{self.street} {self.building_no}/{self.flat_no} \n{self.postal_code} {self.city}')
        else:
            print(f'{self.street} {self.building_no} \n{self.postal_code} {self.city}')

    def comes_before(self, other) -> bool:
        add1 = self.postal_code.split('-')
        add2 = other.postal_code.split('-')
        if add1[0] < add2[0]:
            return True
        if add1[0] == add2[0] and add1[1] < add2[1]:
            return True
        return False
