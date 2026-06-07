CI TENTA 

Detta projekt är enkel miniräknare som är skriven i python. Appen innehåller grunläggande fuktioer för matematiska beräkningar, som addtion och subtraction.


Syftet med projektet är att visa använding av git, github , branches, PR och en CI-pipeline med github Actions.

Köra applikationen lokalt:
Klona repositoryt:
git clone https://github.com/nourhassan94/ci-tenta.git
Gå till projektmappen:
cd ci-tenta
Kör programmet:
python calculator.py


För att köra testerna lokalt:
pytest

CI-pipeline:
Projektet använder GitHub Actions för Continuous Integration (CI).

Pipelinen startas automatiskt när:
Kod pushas till branchen main
En Pull Request skapas mot main

CI-pipelinen utför följande steg:
Checkar ut koden från repositoryt.
Installerar Python 3.12.
Installerar projektets beroenden.
Kör automatiserade tester med pytest.

Om testerna godkänns markeras körningen som lyckad. Om något test misslyckas stoppas pipelinen och körningen markeras som misslyckad.
