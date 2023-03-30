# TEMA 2: Metoda input(), metode string, operatori, conditionale

# A. RECOMANDAT (nivel USOR)

# 1. Revizualizeaza intalnirea 2 si ia notite in caz ca ti-a scapat ceva.
# 2. Vizualizeaza video despre Operatori si Flow Control din 'Primii pasi in Programare' (Daca nu ai facut-o deja)
# 3. Vizualizeaza video 3 despre Structuri de date din 'Primii pasi in Programare'.
# Astfel, la intalnirea LIVE deja va fi a 2-a oara cand vei auzi conceptele si
# sigur ti se vor intipari in minte mai bine.
# Link catre video: https://www.itfactory.ro/8174437-intro-in-programare

# B. OBLIGATORIU (nivel USOR -> MEDIU)

# 1. Citeste de la tastatura numele, citeste apoi de la tastatura prenumele. Afiseaza cate caractere are numele complet
# (nume + prenume), afisand propozitia 'Numele complet are x caractere.', unde x este numarul total de caractere.

# nume = input('Care este numele tau ?')
# prenume = input( 'Care este prenumele tau ?')
# print(f'Numele complet are {len(nume) + len(prenume)} caractere')

# 2. Citeste de la tastatura lungimea, citeste apoi de la tastatura latimea. Afiseaza aria dreptunghiului cu lungimea si
# latimea citite de la tastatura, afisand propozitia 'Aria dreptunghiului este x.', unde x este valoarea ariei.

# lungimea = float(input('care este lungimea ?'))
# latimea = float(input('care este latimea ?'))
# print(f'Aria dreptunghiului este {lungimea * latimea}')

# 3. Avand stringul: 'Coral is either the stupidest animal or the smartest rock.', afisati de cate ori apare cuvantul
# 'the' in acesta.

# afirmatie = 'Coral is either the stupidest animal or the smartest rock.'
# print(afirmatie.count(' the '))

# 4. Folosing acelasi string de la punctul 2, inlocuieste cuvantul 'the' cu 'THE' peste tot in propozitie si printeaza
# rezultatul.

# afirmatie = 'Coral is either the stupidest animal or the smartest rock.'
# print(afirmatie.replace(' the ',' THE '))

# 5. Folosind acelasi string de la punctul 2, folositi un assert ca sa verificati daca acest string contine doar
# numere.

# afirmatie = 'Coral is either the stupidest animal or the smartest rock.'
# assert == afirmatie.isnumeric()

# 6. Exploreaza urmatoarele metode ajutatoare ale string-ului si scrie cel putin un exemplu de folosire pentru fiecare:
# a. endswith()

# afirmatie = 'Coral'
# print(afirmatie.endswith('al'))

# b. index()
# afirmatie = 'Coral is either the stupidest animal or the smartest rock.'
# print(afirmatie.index('animal'))

# c. lower()

# afirmatie = 'Coral is either the stupidest animal or the smartest rock.'
# print(afirmatie.lower())

# d. replace()

# afirmatie = 'Coral is either the stupidest animal or the smartest rock.'
# print(afirmatie.replace('stupidest', 'smartest'))

# e. strip()

# afirmatie = ' Coral is either the stupidest animal or the smartest rock. '
# print(afirmatie.strip())

# f. split()

# afirmatie = 'Coral is either the stupidest animal or the smartest rock.'
# print(afirmatie.split())

# ATENTIE! Pentru exercitiile care urmeaza se va folosi notiunea de if in rezolvare.
# Indirect veti exersa si operatorii in cadrul conditiilor ramurilor din if.

# Variabila X specificata in exercitiile de mai jos poate fi initializata direct in cod
# sau citita de la tastatura, dupa preferinte si va fi o variabila int.

# 6. Explica cu cuvintele tale in cadrul unui comentariu cum functioneaza un if else.

# linia de cod de dupa IF se executa daca conditia mentionata anterior este true/este respectata.
# Daca nu, codul se opreste sau in cazul in care exista un ELSE veirifca daca acela este TRUE/se respecta
# si daca da, se executa, daca nu, se opreste.

# 7. Verifica si afiseaza daca x este numar natural sau nu.
# (un numar se considera natural daca este numar intreg mai mare ca 0)

# x = 5
# if x > 0:
#     print('Este numar natural')
# else:
#     print('Nu este numar natural')


# 8. Verifica si afiseaza daca x este numar pozitiv, negativ sau neutru (adica 0).

# x = 5
# if x > 0:
#     print('Este numar pozitiv')
# elif x < 0:
#     print('Este numar negativ')
# else:
#     print('Este numar neutru')


# 9. Verifica si afiseaza daca x este intre -2 si 13 (incluzand capetele de interval).

# x = 5
# if x >= -2 and x <= 13:
#     print('Este cuprins intre -2 si 13')

# 10.
# a. Declara o noua variabila numita y, de tip int.

# y = 3

# b. Verifica si afiseaza daca diferenta dintre x si y este mai mica de 5

# if (x - y) < 5:
#     print('diferenta dintre x si y este mai mica de 5')

# 11. Verifica daca x NU este intre 5 si 27, incluzand capetele de interval. (a se folosi ‘not’)
# x = 6
# if not (x >=5 and x <= 27):
#     print('nu se afla in intervalul 5 - 27')
# else:
#     print('se afla in intervalul 5 - 27')

# 12.
# a. Declara o noua variabila numita y, de tip int.

# y = 8

# b. Verifica si afiseaza daca x si y sunt egale. Daca nu, afiseaza care din ele este mai mare.

# if x == y:
#     print('x si y sunt egale')
# elif x > y:
#     print(x)
# elif y > x:
#     print(y)

# 13. Presupunand ca x, y, z (toate de tip int) - reprezinta laturile unui triunghi, afiseaza daca triunghiul
# este isoscel (doua laturi sunt egale), echilateral (toate laturile sunt egale) sau oarecare (nicio latura nu e egala).

# x = 5
# y = 6
# z = 5
# if x == y and x != z or y == z and y != x or x == z and x != y:
#     print('triunghiul este isoscel')
# if x == y and y == z:
#     print('triunghiul este echilateral')
# if x != y and y != z and x != z:
#     print('triunghiul este oarecare')

# 14. Citeste o litera de la tastatura apoi verifica si afiseaza daca este vocala sau nu.
# Atentie! Trebuie sa evaluati si cazurile uppercase si cazurile lowercase.

# vocale = ('a' 'A' 'e' 'E' 'i' 'I' 'o' 'O' 'u' 'U')
# litera = input('Introduceti o litera')
# if litera in vocale:
#     print('Ati ales o vocala')
# else:
#     print('Ati ales o consoana')
# print(type(vocale))

# 15. Transforma si printeaza notele din sistem românesc in sistem american dupa cum urmeaza:
# Peste 9 => A
# Peste 8 => B
# Peste 7 => C
# Peste 6 => D
# Peste 4 => E
# 4 sau sub => F

# nota = int(input('introdu nota'))
# if nota > 9:
#     print('A')
# elif nota > 8:
#     print('B')
# elif nota > 7:
#     print('C')
# elif nota > 6:
#     print('D')
# elif nota > 4:
#     print('E')
# else:
#     print('F')

