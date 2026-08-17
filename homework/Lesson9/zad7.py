# Zadanie 7 
# Tworzenie struktury folderów: Użyj modułu pathlib , aby napisać skrypt, który tworzy
# strukturę folderów: Projekt/src , Projekt/data , Projekt/docs 

from pathlib import Path

PROJEKT_FOLDER: Path = Path(__file__).parent / "Projekt"
PODKATALOGI: list[Path] = [
    PROJEKT_FOLDER / "src",
    PROJEKT_FOLDER / "data", 
    PROJEKT_FOLDER / "docs" 
]

def stworz_strukture_folderow() -> None: 
    """Tworzymy strukturę podfolderów za pomocą pathlib."""
    for folder in PODKATALOGI:
        # parents = True - tworzy główny folder "Projekt" jeśli nie istenieje 
        # exist_ok=True - jeśli folder już istenieje to nie będzie rzucać błędem 
        folder.mkdir(parents=True, exist_ok=True) 

try: 
    stworz_strukture_folderow() 
    print("Struktura folderów została pomyślnie utworzona")
except PermissionError:
    print("Błąd: Brak uprawnień") 
except Exception as e: 
    print(f"Wystąpił nieoczekiwany błąd {e}")
