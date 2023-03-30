# Exerciții RECOMANDATE - grad de dificultate: Ușor

# 1. Revizualizeaza intalnirea 3 si ia notite in caz ca ti-a scapat ceva
# 2. Vizualizeaza video despre Structuri de date din 'Primii pasi in Programare' (Daca nu ai facut-o deja)
# 3. Vizualizeaza video 4 despre Flow Control din 'Primii pasi in Programare'.
# Astfel, la intalnirea LIVE deja va fi a 2-a oara cand vei auzi conceptele si
# sigur ti se vor intipari in minte mai bine.
# Link video: https://www.itfactory.ro/8174437-intro-in-programare/

# EXERCITII OBLIGATORII

# 1.
# a. Declara o lista, note_muzicale, in care sa pui do re mi etc pana la do.

# lista = ['do', 're', 'mi', 'fa', 'sol', 'la', 'si', 'do']

# b. Afiseaz-o.

# print(lista)

# c. Inversează ordinea folosind slicing si suprascrie aceasta lista, apoi printeaza varianta actuala (inversata).
# lista1 = (lista[::-1])
# print(lista1)
# d. Aplica o metoda pe lista care banuiesti ca face același lucru, adica sa ii inverseze ordinea.
# (Nu trebuie sa o suprascrii în acest caz, deoarece metoda face asta automat)
# si apoi printeaza varianta actuala a listei. Practic ai ajuns înapoi la varianta inițială.

# lista1.reverse()
# print(lista1)
# Concluzii: slicing e temporar, dacă vrei sa pastrezi noua varianta va trebuie sa suprascrii lista
# sau sa o salvezi intr-o listă nouă.
# Metoda gasita de tine face suprascrierea automat și permanentizeaza aceste modificări.
# Ambele variante își găsesc utilitatea în funcție de ce ne dorim in acel moment.

# e. Afiseaza pe ecran de cate ori apare nota ‘do’ in lista.

# print(lista.count('do'))

# 2. Avand 2 liste, [3, 1, 0, 2] si [6, 5, 4], gaseste 2 variante prin care sa le unesti intr-o singura lista.

# lista1 = [3, 1, 0, 2]
# lista2 = [6, 5, 4]
# lista3 = lista1 + lista2
# print(lista3)
# lista1.extend(lista2)
# print(lista1)

# 3.
# a. Sorteaza si afiseaza lista generata la exercitiul anterior.

# lista3.sort()
# print(lista3)

# b. Sterge numarul 0 din lista folosind o functie/metoda ajutatoare si apoi afiseaza din nou lista.

# lista3.remove(0)
# print(lista3)

# 4. Folosind un if, verifica lista generata la exercitiul 3 si afiseaza pe fiecare ramura urmatoarele:
# Lista este goala (IF)
# Lista nu este goala (ELSE)

# if not lista3:
#     print('lista este goala')
# else:
#     print('lista nu este goala')

# 5. Foloseste o functie care sa goleasca lista de la exercitiul 3/ sa o transforme in lista goala.

# lista3.clear()
# print(lista3)

# 6. Rescrie if-ul de la exercitiul 5 si verifica inca o data rezultatul. Acum ar trebui sa se afiseze ca lista e goala.

# if not lista3:
#     print('lista este goala')
# else:
#     print('lista nu este goala')

# 7. Avand dictionarul dict1 = {'Ana' : 8, 'Gigel' : 10, 'Dorel' : 5},
# foloseste o functie ca sa afisezi Elevii (cheile).

# dict1 = {
#     'Ana' : 8,
#     'Gigel' : 10,
#     'Dorel' : 5
# }
# print(dict1)

# 8. Printeaza cei 3 elevi din dictionarul de la exercitiul 7 si respectiv notele lor.
# Ex: ‘Ana a luat nota {x}’.
# Doar nota o vei lua folosindu-te de cheie

# print(f"Ana a luat nota {dict1['Ana']}")
# print(f"Gigel a luat nota {dict1['Gigel']}")
# print(f"Dorel a luat nota {dict1['Dorel']}")


# 9. Imagineaza-ti ca Dorel a facut contestatie si a primit nota 6.
# Modifica nota lui Dorel in 6
# Printeaza nota lui dupa modificare

# dict1['Gigel'] = 6
# print(dict1['Gigel'])

# 10. Imagineaza-ti ca Gigel se transfera din clasa.
# a. Cauta o functie care sa il stearga

# del dict1['Gigel']
# print(dict1)

# b. Vine un coleg nou.
# Adaugati-l in lista pe Ionica, cu nota 9.

# dict1['Ionica'] = 9

# c. Printati dictionarul cu noii elevi

# print(dict1)