# 1. Klasy

1. Dodaj do klasy **```Punkt```** statyczną metodę **```distance```**, która oblicza długość odcinka łączącego dwa punkty będące argumentami tej metody. W funkcji **```main```** utwórz obiekt klasy **```Punkt```** oraz obiekt klasy **```NazwanyPunkt```**, a następnie wypisz rezultat wywołania metody **```distance```** dla tych obiektów.

2. Zaimplementuj klasę **```Adres```**. Adres zawiera numer domu, ulicę, opcjonalnie numer mieszkania, miasto i kod pocztowy. Zdefiniuj inicjalizator tak, aby obiekt mógł zostać utworzony na jeden z dwóch sposobów: z numerem mieszkania lub bez niego. Dostarcz metodę **```show```**, która wypisuje adres z ulicą w jednym wierszu oraz kodem pocztowym i miastem w następnej linii. Dostarcz metodę **```comes_before(self, other)```**, która sprawdza, czy dany adres jest przed innym, gdy porównujemy go według kodu pocztowego.

3. Zaimplementuj klasę **```SodaCan```** z metodami **```get_surface_area()```** i **```get_volume()```**. W inicjalizatorze podaj wysokość i promień puszki.

4. Zaimplementuj klasę **```Car```** o następujących właściwościach. Samochód ma określoną wydajność paliwową (mierzoną w kilometrach/litr) i pewną maksymalną ilość paliwa w zbiorniku. Wydajność jest określona w konstruktorze, a początkowy poziom paliwa wynosi **```0```**. Dostarcz metodę drive, która symuluje jazdę samochodem przez pewien dystans, zmniejszając poziom paliwa w zbiorniku, metodę **```get_fuel_level```**, która zwraca aktualny poziom paliwa, oraz metodę **```add_fuel```**, która symuluje tankowanie, przy czym nie można przekroczyć maksymalnej pojemności baku. Przykładowe użycie:

```python
my_car = Car(20, 40) # Wydajność 20 km/litr, pojemność baku 40
my_car.add_fuel(30) # Zatankuj co najwyżej 30 litrów
my_car.drive(100) # Przejedź 100m
print(my_car.get_fuel_level()) # Wydrukuj ilość pozostałego paliwa
```

5. Zaimplementuj klasę **```Student```**. Na potrzeby tego ćwiczenia student ma imię i nazwisko oraz całkowity wynik quizów. Dostarcz odpowiedni inicjalizator oraz metody **```get_name()```**, **```add_quiz(score)```**, **```get_total_score()```**, oraz **```get_average_score()```**. Aby w ostatniej z tych metod obliczyć średni wynik ze wszystkich quizów, należy przechowywać w odpowiednim polu liczbę quizów, do których przystąpił student.

# 2. Wybrane zagadnienia programowania klas

1. Napisz klasę **```Wymierna```** reprezentującą liczby wymierne **```p/q```**. Liczby **```p```** i **```q```** powinny być pamiętane jako względnie pierwsze z dodatnim **```q```**. Zaimplementuj:

    - Inicjalizator z dwoma argumentami całkowitymi, **```licznik```** i **```mianownik```**, przy czym domyslną wartoscią licznika powinno być zero a mianownika jeden. Inicjalizator powinien działać poprawnie również jeżeli podane argumenty nie są względnie pierwsze lub mianownik jest ujemny.
    - Funkcje składowe **```get_licznik```** i **```get_mianownik```** zwracające odpowiednio licznik i mianownik liczby.
    - Funkcję składową **```__repr__```** zwracającą łańcuch znaków reprezentujący liczbę wymierną.
    - Funkcję składową **```__float__```** zwracającą wartość typu **```float```** odpowiadającą danej liczbie wymiernej.
    - Funkcje składowe **```__add__```** oraz **```__sub__```**.
    - Funkcje składowe **```__eq__```**, **```__ne__```**, **```__lt__```**, **```__le__```**, **```__gt__```**, **```__ge__```**.

    W funkcji **```main```** wczytaj licznik i mianownik dla dwóch liczb wymiernych, utwórz z wczytanych liczb dwie liczby wymierne, a następnie wypisz w kolejnych liniach wyniki uzyskane z zastosowania zdefiniowanych operatorów.

2. Rozszerz definicję klasy z poprzedniego zadania poprzez zdefiniowanie funkcji składowych **```__mul__```** oraz **```__div__```** - **zakładam, że tu chodzi o ```__truediv__```**.

3. Zaimplementuj funkcję **```__eq__```** w sposób wykorzystujący fakt, iż dwie liczby są równe, wtedy i tylko wtedy, gdy żadna z nich nie jest mniejsza od drugiej.

# 3. Ćwiczenia sprawdzające podstawową wiedzę z klas

1.  Napisz program importujący wbudowany moduł **```array```** i wyświetlający przestrzeń nazw tego modułu.

2. Napisz program, który utworzy klasę i wyświetli przestrzeń nazw wspomnianej klasy.

3. Napisz program, który utworzy instancję określonej klasy i wyświetli przestrzeń nazw tej instancji.

4. Moduł **```builtins```** zapewnia bezpośredni dostęp do wszystkich ’wbudowanych’ identyfikatorów Pythona. Napisz program, który zaimportuje funkcję **```abs()```** za pomocą wbudo wanego modułu, wyświetli dokumentację funkcji **```abs()```** i znajdzie wartość bezwzględną z **```−155```**.
5. Zdefiniuj klasę **```Student```** (atrybuty: **```nazwa_ucznia, klasa_ucznia, student_id```**). Używając atrybutów funkcji wyświetlaj nazwy wszystkich argumentów.

6. Napisz metodę **```student_data()```**, która wyświetli identyfikator ucznia (**```student_id```**). Jeśli użytkownik przekaże argument **```nazwa_ucznia```** lub **```klasa_ucznia```**, funkcja wyświetli nazwę ucznia i klasę.

7. Napisz prostą klasę o nazwie **```Student```** i wyświetl jej typ. Wyświetl także klucze atrybutów **```__dict__```** i wartość atrybutu **```__module__```** klasy Student.

8. Napisz program, w którym utworzysz dwie puste klasy, **```Student```** i **```Marks```**. Teraz utwórz kilka instancji i sprawdź, czy są to instancje wspomnianych klas, czy nie. Sprawdź również, czy wspomniane klasy są podklasami wbudowanej klasy **```Object```**, czy nie.

9. Napisz klasę nazwie **```Student```** z dwoma atrybutami **```student_name, marks```**. Zmodyfikuj wartości atrybutów wspomnianej klasy i wydrukuj oryginalne i zmodyfikowane wartości wspomnianych atrybutów.

10. Napisz klasę o nazwie **```Student```** z dwoma atrybutami **```student_id, student_name```**. Poza klasą dodaj nowy atrybut **```student_class```** i wyświetl cały atrybut wraz z wartościami wspomnianej klasy. Teraz usuń atrybut **```student_name```** i wyświetl cały atrybut z wartościami. Przykładowe wyjście:

```
Original attributes and their values of the Student class:
student_id V10
student_name Adam Nowak
After adding the student_class, attributes and their values with the said class:
student_id V10
student_name Adam Nowak
student_class V
After removing the student_name, attributes and their values from the said class:
student_id V10
student_class V
```

11. . Napisz klasę o nazwie **```Student```** i utwórz dwie instancje **```student_1, student_2```** i przypisz podane wartości do wspomnianych atrybutów instancji. Wydrukuj wszystkie atrybuty instancji **```student_1, student_2```** z ich wartościami w podanym formacie.

# 4. Niewiele trudniejsze ćwiczenia sprawdzające podstawową wiedzę

1. Napisz klasę, która ma dwie metody **```get_string```** i **```print_string```**. **```get_string```** akceptuje ciąg znaków od użytkownika, a **```print_string```** drukuje ciąg wielkimi literami.
2. Napisz klasę o nazwie **```Rectangle```** skonstruowaną przez długość i szerokość oraz metodę, która obliczy pole prostokąta.
3. Napisz klasę o nazwie **```Circle```** skonstruowaną przez promień i dwie metody, które obliczą pole i obwód koła.
4. Napisz program, który uzyska nazwę klasy instancji w Pythonie.

# 5. Klasy (2)

1. Zdefiniuj klasę o nazwie **```American```**, która ma statyczną metodę o nazwie **```print_nationality```**. (Użyj dekoratora staticmethod, aby zdefiniować metodę statyczną klasy.)
2. Zdefiniuj klasę o nazwie **```American```** i jej podklasę **```NewYorker```**.
3. Zdefiniuj klasę o nazwie **```Shape```** i jej podklasę **```Square```**. Klasa **```Square```** posiada inicjalizator, który jako argument przyjmuje długość. Obie klasy mają funkcję **```area```**, która może zwrócić kształtu, który domyślnie wynosi 0.
4. W pliku **```polynomial.py```** zaimplementuj własną (Nie korzystając z analogicznych klas z bibliotek Pythona!) klasę **```Polynomial```**, reprezentującą wielomian pojedynczej zmiennej x. Klasa powinna zawierać metody:

    - **```__init__(self, coefficients)```** – inicjalizator tworzący wielomian. Atrybut **```coefficients```** to lista współczynników wielomianu stojących kolejno przy coraz większych potęgach **```x```**, np. **```coefficients = [5, 4, 3, 0, 1]```** reprezentuje wielomian **```1 ∗ x^4 + 0 ∗ x^3 + 3 ∗ x^2 + 4 ∗ x + 5```**.
    - **```deg(self)```** – zwraca stopień wielomianu.
    - **```__str__(self)```** – zwraca napis reprezentujący self.
    - **```__neg__(self)```** – zwraca wielomian (instancję Polynomial) odpowiadający **```-self```**.
    - **```__add__(self, other_poly)```** – zwraca wielomian odpowiadający **```self + other_poly```**. Zastanów się czy w przypadku dodawania, odejmowania i mnożenia można sobie ułatwić zadanie pisząc metode pomocniczą. Zaimplementuj ją. (Przetestuj dla **```pol_1.coefficients = [3 1, 1]```** i **```pol_2.coefficients = [5, 2]```**).
    - **```__sub__(self, other_poly)```** – zwraca wielomian odpowiadający **```self * other_poly```**.
    - **```__mul__(self, other_poly)```** – zwraca wielomian odpowiadający **```self * other_poly```**.
    - **```__eq__(self, other_poly)```** – zwraca **```True```**, gdy wielomiany **```self```** i **```other_poly```** są równe i **```False```** w przeciwnym przypadku.
    - **```__call__(self, x)```** – zwraca wartość wielomianu w punkcie **```x```**.

    Następnie przetestuj każdą z tych metod w funkcji **```main()```** w pliku **```test_polynomial.py```**.

5. Napisz klasę Vector. Zaimplementuj metody: **```__init__, __repr__, __add__, __sub__, __mul__, __eq__, __len__, __getitem__, __str__```** oraz metody norm - zwraca normę (długość, wielkość) wektora, inner – zwraca iloczyn skalarny (iloczyn skalarny) siebie i innego wektora. Przetestuj te metody w osobnym pliku w funkcji main.

6. Wykorzystując atrybut **```__slots__```** zaimplementuj w pliku **```osoba.py```** klasę **```Osoba```** z właściwościami **```nazwisko```** oraz **```rok_urodzenia```**. Dla obu własności zdefiniuj setter oraz deleter. Zdefiniuj także metodę specjalną **```__str__```**. Dodaj do klasy **```Osoba```** metodę klasową o nazwie **```get_ile(cls)```**, która zwraca wartość zmiennej **```cls._ile```** oraz metode **```zwieksz_pobory(ile_procent)```**. Wykorzystując atrybut **```__slots__```** zaimplementuj w pliku **```osoba.py```** klasę **```Pracownik```** dziedziczącą po klasie **```Osoba```** z własnościami **```rok_zatrudnienia```** oraz **```pobory```**. Dla obu własności **```nazwisko```** oraz **```rok_urodzenia```** zdefiniuj setter oraz deleter. Zdefiniuj także metodę specjalną **```__str__```**.

W pliku test_osoba.py w funkcji main():

- Na rzecz klasy **```Osoba```** wywołaj metodę **```get_ile()```**.
- Utwórz jedną instancję klasy **```Osoba```** i przetestuj każdą z metod tej klasy w tym metodę **```get_ile()```**.
- Utwórz jedną instancję klasy **```Pracownik```** i przetestuj każdą z metod tej klasy w tym metodę **```get_ile()```**.
- Usuń utworzone instancje i na rzecz klasy **```Pracownik```** wywołaj metodę **```get_ile()```**.