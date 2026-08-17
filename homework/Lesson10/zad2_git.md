# Zadanie 2 — Tworzenie i zarządzanie repozytorium na GitHub

## 1. Utworzenie i sklonowanie repozytorium

Na GitHubie utworzyłam nowe repozytorium:

`Python-mini-project`

Następnie sklonowałam je na komputer:
git clone https://github.com/Dgorska033/Python-mini-project.git


# Git wyświetlił komunikat:
warning: You appear to have cloned an empty repository.


Repozytorium było puste, ponieważ nie zawierało jeszcze żadnych plików ani commitów.

Następnie przeszłam do katalogu repozytorium:
cd Python-mini-project


---

## 2. Utworzenie pliku `projekt.md`

W PowerShell utworzyłam plik:
New-Item projekt.md


Następnie otworzyłam go w VS Code:
code projekt.md


W pliku opisałam pomysł na aplikację **RoadTrip Randomizer**.

Aplikacja ma wykorzystywać lokalizację użytkownika i losować ciekawe miejsce na wycieczkę samochodową w wybranym przez użytkownika promieniu.

Po zapisaniu pliku sprawdziłam stan repozytorium:
git status


Git pokazał `projekt.md` jako `Untracked file`, ponieważ nowy plik nie był jeszcze śledzony.

Dodałam go do obszaru staging:
git add projekt.md


Następnie utworzyłam pierwszy commit:
git commit -m "docs: dodano opis projektu"

---

## 3. Utworzenie gałęzi `feature-readme`

Utworzyłam nową gałąź roboczą:
git switch -c feature-readme`

Gałąź `feature-readme` została utworzona na podstawie aktualnego stanu `main`.

Następnie zmodyfikowałam plik `projekt.md`, dodając opis grupy docelowej aplikacji.

Stan zmian sprawdziłam za pomocą:
git status


Git pokazał:
modified: projekt.md

Oznaczało to, że śledzony już plik został zmodyfikowany.

---

## 4. Zapisanie zmian zgodnie z Conventional Commits

Dodałam zmodyfikowany plik do staging area:
git add projekt.md


Następnie utworzyłam commit:
git commit -m "docs: dodano opis grupy docelowej"


Zastosowałam konwencję **Conventional Commits**.

```text
docs:


oznacza zmianę dotyczącą dokumentacji projektu.

---

## 5. Wysłanie gałęzi na GitHub

Wysłałam lokalną gałąź `feature-readme` do zdalnego repozytorium:

```bash
git push -u origin feature-readme
```

Opcja `-u` ustawiła powiązanie lokalnej gałęzi `feature-readme` ze zdalną `origin/feature-readme`.

---

## 6. Utworzenie Pull Request

Na GitHubie utworzyłam Pull Request:

```text
base: main
compare: feature-readme
```

Oznacza to, że zmiany z `feature-readme` miały zostać włączone do głównej gałęzi `main`.

Pull Request otrzymał tytuł:

```text
docs: dodano opis grupy docelowej
```

oraz opis informujący o dodaniu sekcji opisującej grupę docelową aplikacji RoadTrip Randomizer.

GitHub potwierdził brak konfliktów między gałęziami:

```text
No conflicts with base branch
```

---

## 7. Scalenie Pull Request

Po sprawdzeniu zmian scaliłam Pull Request z gałęzią `main`.

Do scalenia użyłam opcji:

```text
Merge pull request
```

a następnie:

```text
Confirm merge
```

W efekcie zmiany z `feature-readme` zostały włączone do `main`.

---

## 8. Aktualizacja lokalnej gałęzi `main`

Po wykonaniu merge na GitHubie wróciłam lokalnie na główną gałąź:

```bash
git switch main
```

Następnie pobrałam aktualny stan repozytorium:

```bash
git pull
```

Git pobrał zmiany wykonane wcześniej na GitHubie.

---

## 9. Usunięcie lokalnej gałęzi `feature-readme`

Po scaleniu zmian gałąź robocza nie była już potrzebna.

Usunęłam ją lokalnie:

```bash
git branch -d feature-readme
```

Opcja `-d` usuwa gałąź i chroni przed przypadkowym usunięciem niescalonych zmian.

Następnie sprawdziłam dostępne lokalne gałęzie:

```bash
git branch
```

Pozostała gałąź:

```text
* main
```

---

## 10. Usunięcie zdalnej gałęzi

Próbując usunąć zdalną gałąź:

```bash
git push origin --delete feature-readme
```

otrzymałam komunikat:

```text
refusing to delete the current branch
```

Przyczyną było ustawienie `feature-readme` jako domyślnej gałęzi repozytorium na GitHubie.

W ustawieniach repozytorium zmieniłam więc:

```text
Default branch: feature-readme
```

na:

```text
Default branch: main
```

Po zmianie ustawień `feature-readme` nie występowała już jako zdalna gałąź.

---

## 11. Wyczyszczenie nieaktualnych informacji o zdalnych gałęziach

Lokalny Git nadal posiadał informację o usuniętej zdalnej gałęzi.

Wykonałam:

```bash
git fetch --prune
```

Opcja `--prune` usuwa lokalne referencje do zdalnych gałęzi, które już nie istnieją.

Na końcu sprawdziłam gałęzie:

```bash
git branch -a
```

`feature-readme` nie występowała już ani jako gałąź lokalna, ani jako zdalna.