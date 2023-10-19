# 1. Klasy

1. Wykorzystując atrybut **```__slots__```** zaimplementuj w pliku **```punkt.py```** klasę Punkt z właściwościami **```x```** oraz **```y```**. Dla obu własności zdefiniuj **```setter```** oraz **```deleter```**. Zdefiniuj także metody specjalne **```__repr__```** i **```__str__```** w sposób jaki zostały zastosowane dla klasy **```Temperature```**. Przetestuj klasę **```Punkt```** w funkcji **```main```** zdefiniowanej w pliku **```main_punkt.py```**.

2. Wykorzystując atrybut **```__slots__```** zaimplementuj klasę **```NazwanyPunkt```** dziedziczącą po klasie **```Punkt```**. Przetestuj klasę **```NazwanyPunkt```** w funkcji main zdefiniowanej w pliku **```main_nazwanypunkt.py```**.

# 2 Serializacja - moduł **```pickle```**

1. Napisz program, w którym korzystając z klas **```Punkt```** oraz **```NazwanyPunkt```** z poprzednich dwóch zadań utwórz listę **```punkty```** z czterema obiektami tych klas (po dwa obiekty z każdej klasy). Stosując moduł **```pickle```** zapisz listę **```punkty```** w pliku **```punkty.pkl```**.
