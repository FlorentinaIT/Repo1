
# Tema 4 - Funcții
# Exerciții Recomandate - grad de dificultate: Ușor
# 1. Revizualizează întâlnirea 4 și ia notițe în caz că ți-a scăpat ceva.
# 2. Vizualizează din ‘Primii pași în Programare’ video.
#
# - Flow Control;
# - Funcții.
#
# Astfel, la întâlnirea LIVE deja va fi a 2-a oară când vei auzi conceptele și
# sigur ți se vor întipări în minte mai bine.
# Link: https://www.itfactory.ro/8174437-intro-in-programare/
# Iterațiile sunt mai dificile deoarece necesită puțină gândire algoritmică.
# Te rog să scrii pe canalul de comunicare scrisă unde întâmpini dificultăți și
# te ajut.
# Dacă stai blocat > 30 min, cere indiciu.
# Exerciții obligatorii - grad de dificultate: Usor spre Mediu .
# 1.Având lista:
# masini = ['Audi', 'Volvo', 'BMW', 'Mercedes', 'Aston Martin', 'Lăstun','Fiat', 'Trabant', 'Opel']
# Folosește un for că să iterezi prin toată lista și să afișezi;
# ● ‘Mașina mea preferată este x’.
# for masina in range(0, len(masini)) :
#     print(f'Masina mea preferata este {masina}')
# ● Fă același lucru cu un for each.
# for x in masini :
#     print(f'Masina mea preferata este {x}')
# ● Fă același lucru cu un while.
# while x in masini:
#     print(f'Masina mea preferata este {x}')
# 2. Aceeași listă:
# Folosește un for else
# În for - Modifică elementele din listă astfel încât să fie scrie cu majuscule,
# exceptând primul și ultimul.
# În else:
# - Printează lista.

# for x in masini:
#     print(masini[0], masini[1].upper(), masini[2].upper(),masini[3].upper(), masini[4].upper(), masini[5].upper(), masini[6].upper(),masini[7].upper(),masini[8])
# else:
#     print(masini)


# 3. Aceeași listă:
# Vine un cumpărător care dorește să cumpere un Mercedes.
# Itereaza prin ea prin modalitatea aleasă de tine.
# Dacă mașina e mercedes:
# Printează ‘am găsit mașina dorită de dvs’
# Ieși din ciclu folosind un cuvânt cheie care face acest lucru
# Altfel:
# Printează ‘Am găsit mașina X. Mai căutam‘

# masini = ['Audi', 'Volvo', 'BMW', 'Mercedes', 'Aston Martin', 'Lăstun','Fiat', 'Trabant', 'Opel']
# masina_dorita = 'Mercedes'
# if masina_dorita in masini:
#     print('Am gasit masina dorita de dvs.')
# else:
#     print('Nu am gasit masina dorita de dvs., mai cautam...')

#nu-mi sunt clare ultimele 3 randuri din cerinta acestui exercitiu... l-am adaptat dupa logica mea... posibil sa fi trebuit sa folosesc While ?

# 4. Aceași listă;
# Vine un cumpărător bogat dar indecis. Îi vom prezenta toate mașinile cu
# excepția Trabant și Lăstun.
# - Dacă mașina e Trabant sau Lăstun:
# Folosește un cuvânt cheie care să dea skip la ce urmează (nu trebuie
# else).
# - Printează S-ar putea să vă placă mașina x.

# masini = ['Audi', 'Volvo', 'BMW', 'Mercedes', 'Aston Martin', 'Lăstun','Fiat', 'Trabant', 'Opel']
# for x in masini:
#     if x == 'Trabant' or x == 'Lăstun':
#         continue
#     print(f'S-ar putea sa va placa masina {x}')

# 5. Modernizează parcul de mașini:
# ● Crează o listă goală, masini_vechi.
# masini_vechi = []
# ● Itereaza prin mașini.
# ● Când găsesti Lăstun sau Trabant:
# - Salvează aceste mașini în masini_vechi.
# - Suprascrie-le cu ‘Tesla’ (în lista inițială de mașini).
# masini = ['Audi', 'Volvo', 'BMW', 'Mercedes', 'Aston Martin', 'Lăstun','Fiat', 'Trabant', 'Opel']
# for x in masini:
#     if x == 'Trabant'or x == 'Lăstun':
#         masini_vechi.append(x)
# #nu stiu de ce apare dpar "lastun" ... initial au aparut amandoua :((
#         print(masini_vechi)
#         masini[5] = 'Tesla'
#         masini[7] = 'Tesla'
#         print(masini)

# ● Printează Modele vechi: x.
# ● Modele noi: x.
#
# 6. Având dict:
# pret_masini = {
# 'Dacia': 6800,
# 'Lăstun': 500,
# 'Opel': 1100,
# 'Audi': 19000,
# 'BMW': 23000
# }
# Vine un client cu un buget de 15000 euro.
# ● Prezintă doar mașinile care se încadrează în acest buget.
# masini_in_buget = {k:v for k,v in pret_masini.items() if v <= 15000}
# print(masini_in_buget)
# aceasta este o solutie gasita pe net... sunt convinsa ca solutia asteptata este una mai simpla...
# am inceput initial prin a declara o variabila buget = 15000, insa apoi m-am blocat...

# ● Itereaza prin dict.items() și accesează mașina și prețul.
# print(pret_masini.items())
# print(pret_masini['Dacia'])
# nu-mi este clar ce am de facut aici...

# ● Printează Pentru un buget de sub 15000 euro puteți alege mașină
# xLastun
# print('Pentru bugetul de sub 15000 EUR puteti alege masina Lastun')

# ● Iterează prin listă.
# nu inteleg la ce lista se face referire

# 7. Având lista:
# numere = numere = [5, 7, 3, 9, 3, 3, 1, 0, -4, 3]
# ● Iterează prin ea.
# ● Afișează de câte ori apare 3 (nu ai voie să folosești count).
# numere = [5, 7, 3, 9, 3, 3, 1, 0, -4, 3]
# x = 0
# for numar in numere:
#     if numar == 3:
#             x += 1
# print(f'Numarul 3 apare in numere de {x} ori')

# 8. Aceeași listă:
# ● Iterează prin ea
# ● Calculează și afișează suma numerelor (nu ai voie să folosești sum).
# numere = [5, 7, 3, 9, 3, 3, 1, 0, -4, 3]
# print(sum(numere))

#se pare ca nu gasesc solutia... banuiesc ca se face ca la ex precedent, insa nu stiu cum sa pun conditia...

# 9. Aceeași listă:
# ● Iterează prin ea.
# ● Afișază cel mai mare număr (nu ai voie să folosești max ).

# numere = [5, 7, 3, 9, 3, 3, 1, 0, -4, 3]
# print(numere.sort())
# print(numere[9])

# 10. Aceeași listă:
# ● Iterează prin ea.
# ● Dacă numărul e pozitiv, înlocuieste-l cu valoarea lui negativă.
# Ex: dacă e 3, să devină -3
# ● Afișază noua listă.

# numere = [5, 7, 3, 9, 3, 3, 1, 0, -4, 3]
#
# for x in numere:
#     print(-x)
# nu stiu sa afisez in lista...

