# Komiwojażer dla kurierów  
*Algorytm aproksymacyjny Christofides'a*   
Projekt Zespołowy, MCB 2022
<br />  
## 1 Opis problemu  
W dzisiejszych czasach większość z nas robi różnego rodzaju zakupy przez Internet z dostawą do domu. W Polsce istnieje wiele sklepów online, które do wysyłki
zamówień internetowych, nie korzystają z zewnętrznych usług kurierskich, ale z
magazynów zlokalizowanych na terenie całej Polski codziennie wysyłają swoich
kurierów do klientów z danego obszaru. Trasa kuriera codziennie się zmienia w
zależności od tego, do jakich klientów ma dowieźć zamówienia danego dnia. Motywem powstania niniejszego projektu jest chęć usprawnienia procesu ustalania
trasy dla każdego kuriera danej firmy, który musi dojechać do każdego klienta,
po czym wrócić na punkt startowy. Kluczowe jest, aby kurier użył optymalnej
trasy, najtańszego cyklu Hamiltona. Sprowadza się to do problemu komiwojażera. Aplikacja, nad którą będziemy pracowali, będzie dedykowana wszelkiego
rodzaju firmom, które w swojej działalność mają wpisaną spedycję.  
<br/>
## 2 Algorytm  
Znalezienie najtańszego cyklu Hamiltona w grafie jest problemem NP-trudnym,
czyli nie ma szybkiego (wielomianowego) algorytmu, który by rozwiązywał to
zagadnienie optymalnie. Do rozwiązania problemu będziemy korzystać z algorytmu aproksymacyjnego Christofides’a. Algorytm ten działa jeśli w grafie jest
spełniona nierówność trójkąta na wagach krawędzi. My będziemy rozważać grafy, których wagi krawędzi reprezentują realne odległości na mapie, więc taka
nierówność zawsze będzie spełniona. Dokładny opis algorytmu można znaleźć
tutaj. Chcemy aby nasz aplikacja przyjmowała adresy do których kurier musi
dojechać i zwracała trasę znalezioną przez nasz algorytm.  
<br/>
**Literatura**  
[1] Prof. L. Cowen, Scribe: S. Tauber, Lecture notes on *The Travelling Salesman
Problem (TSP)*, Comp260: Advanced Algorithms, Tufts University, Spring
2002  
[2] Prof. L. Cowen, Scribe: S. Tauber, Lecture notes on *The Travelling Salesman
Problem (TSP)*, Comp260: Advanced Algorithms, Tufts University, Spring
2018, http://www.cs.tufts.edu/comp/260/public_html/lecture3a.pdf  
[3] A. S. Biswas, Recorded Lecture *R9. Approximation Algorithms: Traveling Salesman Problem*, 6.046J Design and Analysis of Algorithms, MIT, Spring 2015, https://www.youtube.com/watch?v=zM5MW5NKZJg&t=1168s  
[4] N. Christofides, Worst-Case Analysis of a New Heuristic
for the Travelling Salesman Problem, *SN Operations Research Forum 3(1)*, 2022, 1--4, https://apps.dtic.mil/dtic/tr/fulltext/u2/a025602.pdf  
[5] P. E. Black, Christofides algorithm, in *Dictionary of Algorithms and Data Structures* [online], P. E. Black, ed. 24 November 2020. (accessed 5.11.2022) Available from: https://www.nist.gov/dads/HTML/christofides.html
