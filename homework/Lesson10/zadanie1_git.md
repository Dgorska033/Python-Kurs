# Zadanie 1 — Zespołowe tworzenie małego projektu

## 1. Utworzenie repozytorium

Utworzyłam repozytorium `Python-Kurs` na GitHubie.

Następnie połączyłam lokalne repozytorium z GitHubem:


git remote add origin https://github.com/Dgorska033/Python-Kurs.git

#Następnie zmieniłam nazwę głównej gałęzi z master na main:
git branch -M main

 # Wysłałam lokalne repozytorium na GitHub:
git push -u origin main
# Opcja -u ustawia połączenie między lokalną gałęzią main i zdalną origin/main

--- 

## 2. Konfiguracja .gitignore

# Utworzyłam plik: 
.gitignore

# Dodałam do niego:
venv/
__pycache__/
*.pyc
.vscode/

# Dzięki temu Git nie śledzi:

# środowiska wirtualnego venv,
# plików __pycache__,
# skompilowanych plików .pyc,
# ustawień VS Code.

# Ponieważ venv i .vscode były już wcześniej dodane do repozytorium, usunęłam je z indeksu Git bez usuwania ich z komputera:
git rm -r --cached venv
git rm -r --cached .vscode

# Następnie zapisałam zmiany:
git add .gitignore
git commit -m "Usuń .vscode z repozytorium"

---


## 3. Sprawdzenie historii commitów
# Do sprawdzenia historii repozytorium użyłam:
git log --oneline
# Polecenie pokazuje skrócony identyfikator commita oraz jego opis.

---

## 4. Dodanie pliku README

# Utworzyłam plik:
README.md
# Plik zawiera opis repozytorium i jego struktury.

# Następnie dodałam go do repozytorium:
git add README.md
git commit -m "Dodaj README"
git push

---

## 5. Utworzenie gałęzi develop

# Utworzyłam nową gałąź:
git switch -c develop
# -c tworzy nową gałąź i od razu na nią przełącza.

# Następnie wysłałam ją na GitHub:
git push -u origin develop

# Sprawdziłam dostępne gałęzie:
git branch
# Wynik pokazał:
* develop
  main
# Gwiazdka oznacza aktualnie używaną gałąź.

---

## 6. Ochrona gałęzi main

# Na GitHubie skonfigurowałam ruleset dla gałęzi main.

# Ustawiłam:

# ochronę przed usunięciem gałęzi,
# blokadę force push,
# wymaganie Pull Request przed scaleniem,
# wymaganie 2 akceptacji Pull Request.

# Nie ustawiłam wymaganych status checks, ponieważ repozytorium nie miało jeszcze skonfigurowanych testów automatycznych.

---

## 7. 7. Klonowanie repozytorium

# W celu przećwiczenia klonowania repozytorium wykonałam:
git clone https://github.com/Dgorska033/Python-Kurs.git

# Następnie weszłam do sklonowanego katalogu:
cd Python-Kurs

# Sprawdziłam stan repozytorium:
git status

# Git potwierdził, że lokalna gałąź main jest aktualna względem origin/main 
 
---

## 8. Utworzenie struktury projektu
# Utworzyłam katalogi:
mkdir src
mkdir tests
mkdir docs

# Następnie sprawdziłam zawartość katalogu:
dir

