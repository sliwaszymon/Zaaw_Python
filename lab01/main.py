from punkt.punkt_alfa import Point
from address import Address
from sodacan import SodaCan
from car import Car
from student import Student
from wymierna import Wymierna


def zad1_1() -> None:
    print('### ZAD 1.1 ###')
    punkt1 = Point(1, 2)
    punkt2 = Point(7, 9)
    print(Point.distance(punkt1, punkt2))


def zad1_2() -> None:
    print('### ZAD 1.2 ###')
    address1 = Address(16, 'Tołkiny', 'Korsze', '11-430', 2)
    address2 = Address(12, 'Wojska Polskiego', 'Kętrzyn', '11-400')
    address1.show()
    address2.show()
    print('Czy address2 jest wcześniej niż address1? ', address2.comes_before(address1))


def zad1_3() -> None:
    print('### ZAD 1.3 ###')
    sodacan = SodaCan(8, 2)
    print('Surface: ', sodacan.get_surface_area())
    print('Volume: ', sodacan.get_volume())


def zad1_4() -> None:
    print('### ZAD 1.4 ###')
    my_car = Car(20, 40)
    my_car.add_fuel(30)
    my_car.drive(100)


def zad1_5() -> None:
    print('### ZAD 1.5 ###')
    my_student = Student('Szymon', 'Śliwa')
    print(my_student.get_name())
    my_student.add_quizz(20)
    my_student.add_quizz(14)
    print('Total score', my_student.get_total_score())
    print('Average score', my_student.get_average_score())


def zad2_1() -> None:
    print('### ZAD 2.1 ###')
    wym1 = Wymierna(45, -63)
    print(wym1)
    print(float(wym1))
    wym2 = Wymierna(1, 2)
    print(wym1 + wym2)
    print(wym1 - wym2)


if __name__ == '__main__':
    # zad1_1()
    # zad1_2()
    # zad1_3()
    # zad1_4()
    # zad1_5()
    zad2_1()
