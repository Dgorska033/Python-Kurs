"""
Konfiguracja aplikacji Flask.
NIGDY nie commituj haseł do repozytorium!
"""

import os
from dotenv import load_dotenv


# Ładujemy zmienne zapisane w pliku .env
load_dotenv()


class Config:
    """Bazowa konfiguracja."""

    # SECRET_KEY pobieramy ze zmiennej środowiskowej.
    # Druga wartość jest wartością domyślną dla developmentu.
    SECRET_KEY = os.getenv(
        'SECRET_KEY',
        'dev-secret-key-change-me'
    )

    # Wyłączamy śledzenie modyfikacji SQLAlchemy.
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class DevelopmentConfig(Config):
    """Konfiguracja developerska."""

    DEBUG = True

    # Adres połączenia z bazą PostgreSQL.
    # Najpierw próbujemy pobrać DATABASE_URL z pliku .env.
    SQLALCHEMY_DATABASE_URI = os.getenv(
        'DATABASE_URL',
        'postgresql://postgres:mama.123@localhost:5432/flask_masterclass'
    )

    # Pokazuje zapytania SQL w konsoli.
    SQLALCHEMY_ECHO = True


class ProductionConfig(Config):
    """Konfiguracja produkcyjna."""

    DEBUG = False

    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL')

    SQLALCHEMY_ECHO = False


# Słownik pozwala łatwo wybrać konfigurację.
config = {
    'development': DevelopmentConfig,
    'production': ProductionConfig,
    'default': DevelopmentConfig
}