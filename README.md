Musuroi David-Gabriel Seria CC Grupa 311

In functia determine_win.py determin modul de constructie al datelor, el fiind
furnizat in felul urmator : am extras la intamplare cateva aspecte care mi s-au
parut relevante pentru determinarea probabilitatii unui jucator de a castiga un
meci (numarul de trofee, win streak-ul, etc.) si am dezvoltat o formula 
aleatorie pentru a determina aceasta probabilitate, maximul posibil fiind 130%
din 100% (pentru a avea si date incorecte, din nou, pentru a le elimina).
Jucatorul a castigat daca un numar generat aleatoriu este mai mic decat
probabilitatea de a castiga, iar in caz contrar a pierdut. La final returnez un
dictionar cu toate cele 10 coloane.

In functia main am generat aleatoriu 10 coloane pentru 1000 de instante, pe
care le-am impartit in felul urmator : 700 pentru antrenare si 300 pentru
testare, ambele generate la intamplare, si le-am pus in 2 csv-uri diferite.
Dupa aceea, am eliminat valorile lipsa (probabilitatea de castig mai mare ca 
100 sau cazul in care Favourite_Win_Condition este N.A. --> not available, o
eroare introdusa de mine pentru a ma asigura ca exista mai multe date pe care
le pot elimina) si am exportat si aceste subseturi in format csv.

In continuare, am determinat statisticile descriptive folosind functia describe
si am realizat histograma, countplot-ul, boxplot-ul si violinplot-ul intr-o
alta functie plots.py pentru variabilele corespunzatoare cerintei date, pe
care nu am putut sa le afisez asa ca le-am salvat ca poze cu extensia .jpg.

Tot in main, fiind o problema de clasificare, am folosit Random Forest pentru
a antrena subsetul de antrenare si pentru a evalua subsetul de testare, cu
precizarea ca pentru variabilele categorice am folosit One Hot Encoding, astfel
determinand acuratetea modelului. La final am realizat matricea de confuzie pe
care am salvat-o tot ca poza cu extensia .jpg.

Referitor la grafice nu se pot spune multe lucruri despre ele, intrucat
cum toata implementarea a fost realizata folosind biblioteca random, fiecare
rulare a programului va rezulta in alte date, alta acuratete, alta matrice de
confuzie etc. asa ca programul trebuie analizat in parte pentru fiecare rulare.