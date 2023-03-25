# TEMA 1

# A. RECOMANDAT (nivel USOR)

# 1. Revizualizeaza inregistrarea sesiunii 1 si ia notite
# 2. Vizualizeaza cursul "PRIMII PASI IN PROGRAMARE" (daca nu ai facut-o deja), sectiunea "Variable si Tipuri de date"
# 3. Vizualizeaza cursul "PRIMII PASI IN PROGRAMARE", sectiunea "Operatori si Flow Control".
# LINK curs "PRIMII PASI IN PROGRAMARE": https://www.itfactory.ro/8174437-intro-in-programare/


# B. OBLIGATORIU (nivel USOR -> MEDIU)

# 1. In cadrul unui comentariu, explicati cu cuvintele voastre ce este o variabila.
# O variabila este o zona din memorie care contine date

# 2. Declarati si initializati cate o variabila din fiecare din urmatoarele tipuri: string, int, float, bool.
# Valorile le alegeti voi dupa preferinte.
prenume = 'Florentina'
numar = 10
numar1 = 10.5
este_par = True

# 3. Utilizati functia type(), pentru a verifica daca variabilele declarate la punctul 2 au tipul de date asteptat.
print(type(prenume))
print(type(numar))
print(type(numar1))
print(type(este_par))

# 4. Rotunjiti variabila definita ca tip float, folosindu-va de functia round() si salvati aceasta modificare in aceeasi
# variabila (suprascriere). Verificati apoi tipul acesteia.
round(numar1)
numar1 = round(numar1)
print(type(numar1))

# 5. Folositi functia print() pentru a printa in consola 4 propozitii, folosind cele 4 variabile.
# (Rezolvati nepotrivirile de tip prin ce modalitate doriti)
print('Buna ziua, numele meu este' + ' ' + prenume)
print('Studentii de la clasa sunt in numar de' + ' ' + str(numar))
#sau
print(f'Studentii de la clasa sunt in numar de {numar}.')
print(f'Tricoul costa {numar1} lei.')
print('Numarul 2 este par ? raspuns:' + str(este_par))

# 6.
# a. Defineste o variabila float cu valoarea 1.5 .
variabila = 1.5
print(variabila)

# b. Verifica daca variabila este egala cu 1.5 .
assert variabila == 1.5
print('Este adevarat')

# c. Verifica daca variabila este egala cu true. Ce observi?
assert variabila == true
print("Este True")
# observ ca variabila nu este egal true si am eroare, deci nu se printeaza "Este True"

# d. Cum poti face ca assert-ul de la punctul c sa treaca?
variabila = true
assert variabila == true
print('Este true.')

variabila = bool(variabila)
assert variabila == true