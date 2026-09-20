import os
from dotenv import load_dotenv

# Wczytuje zmienne z pliku .env
load_dotenv()


class Config:
    # Pobiera connection string z pliku .env
    SQLALCHEMY_DATABASE_URI = os.getenv("DATABASE_URL")

    # Wyłącza zbędne śledzenie zmian
    SQLALCHEMY_TRACK_MODIFICATIONS = False