# a. USOR (RECOMANDAT)
# 1. Revizualizeaza intalnirea 5 si ia notite in caz ca ti-a scapat ceva
# 2. Vizualizeaza video despre Functii din 'Primii pasi in Programare'
# (Daca nu ai facut-o deja)
# 3. Vizualizeaza video 7 despre OOP din 'Primii pasi in Programare'
# Astfel, la intalnirea LIVE deja va fi a 2-a oara cand vei auzi conceptele
# si sigur ti se vor intipari in minte mai bine.
# https://www.itfactory.ro/8174437-intro-in-programare/

# b. OBLIGATORIU: USOR SPRE MEDIU

# IMPORTANT! -> Pentru TOATE EXERCITIILE, apelati functia de cel putin 2 ori cu valori
# diferite pentru a testa. Daca functia are return, printati raspunsul!

# 1. Scrie o functie care sa calculeze si sa returneze suma a 2 numere
# def sum_numbers(a, b):
#     result = a + b
#     print(f'Sum: {result}')
#
# sum_numbers(10, 20)
# sum_numbers(5, 10)
# sum_numbers(5.5, 6)
# sum_numbers('ana', 'maria')

# 2. Scrie o functie care sa returneze True daca un numar este par, False daca este impar
# def par_numbers (i):
#     if i % 2 == 0:
#         print(True)
#     else:
#         print(False)
#
# par_numbers(2)
# par_numbers(3)
# par_numbers(133)
# par_numbers(0)
# par_numbers(3.5)

# 3. Scrie o functie care sa returneze numarul total de caractere din numele tau complet
# (nume, prenume, nume_mijlociu)

# nume = str(input('introdu numele'))
# prenume = str(input('introdu prenumele'))
# nume_mijlociu = str(input('introdu numele mijlociu'))
#
# def suma_nume(a, b, c):
#     result = len(a) + len(b) + len(c)
#     print(f'Suma numelui tau este {result}')
#
# suma_nume(nume, prenume, nume_mijlociu)


# 4. Scrie o functie care returneaza aria dreptunghiului

# def arie_dreptunghi(a, b):
#     result = a * b
#     print(f'Aria dreptunghiului este: {result}')
#
# arie_dreptunghi(5, 10)
# arie_dreptunghi(3.3, 8)
# arie_dreptunghi(5.5, 10.2)

# 5. Scrie o functie care returneaza aria cercului
# def arie_cerc(i):
#     arie = 3.14 * i * i
#     return arie
#
# numar = arie_cerc(9)
# print(numar)

# 6. Scrie o functie care returneaza True daca un caracter x se gaseste intr-un string dat, False daca nu.

# def find_element(x,string):
#     if x in string:
#         print('True')
#     else:
#         print('False')
#
# find_element('a','Ana')
# find_element('x', 'Ana')



# 7. Scrie o functie fara return care primeste ca parametru un string si printeaza pe ecran:
# - Nr. caractere lower case este x
# - Nr. caractere upper case este y

# def caractere(string):
#     print(sum(map(str.islower, string)))
#     print(sum(map(str.isupper, string)))
#
# caractere('Ana')
# caractere('python')
# caractere('PROGRAMARE')

# 8. Scrie o functie care primeste o lista de numere si returneaza o lista doar cu numerele pozitive

# def numere_pozitive(lista):
#     numere_pozitive = []
#     for i in lista:
#         if i > 0:
#             numere_pozitive.append(i)
#         else:
#             print('Nu am gasit numere pozitive')
#     print(numere_pozitive)
# numere_pozitive([1, 2, 3, -5])
# numere_pozitive([-2, 3, -8])
# numere_pozitive([-3, -9])


# 9. Scrie o functie care nu returneaza nimic. Primeste 2 numere si printeaza:
# - primul numar x este mai mare decat al doilea y
# - al doilea numar y este mai mare decat primul numar x
# - Numerele sunt egale.

# def compar_numere(x, y):
#     if x > y:
#         print('Primul numar este mai mare decat al doilea')
#     elif x < y:
#         print('Al doilea numar este mai mare decat primul')
#     else:
#         print('Numerele sunt egale')
#
# compar_numere(5,2)
# compar_numere(3,7)
# compar_numere(3,3)

# 10. Scrie o functie care primeste un numar si un set de numere.
# Printeaza 'am adaugat numarul nou in set' + returneaza True
# sau printeaza 'Nu am adaugat numarul nou in set. Acesta exista deja' + returneaza False

# def adaug_numar(i, set):
#     if i in set:
#         print('Nu am adaugat numarul, acesta exista')
#         return False
#     else:
#         print('Am adaugat numarul nou in set')
#         return True
#
# adaug_numar(5, {1, 2, 3})
# adaug_numar(5, {1, 2, 5})