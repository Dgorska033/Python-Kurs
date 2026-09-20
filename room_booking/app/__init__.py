from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import text


# Jeden wspólny obiekt SQLAlchemy
db = SQLAlchemy()


def create_app():
    app = Flask(__name__)

    # Wczytanie konfiguracji aplikacji
    app.config.from_object("config.Config")

    # Inicjalizacja SQLAlchemy
    db.init_app(app)


    # ----------------------------------------
    # Endpoint sprawdzający połączenie z bazą
    # ----------------------------------------

    @app.route("/test-db")
    def test_db():
        try:
            db.session.execute(
                text("SELECT 1")
            )

            return "Połączenie OK!"

        except Exception as e:
            return (
                f"Błąd połączenia: {e}",
                500
            )


    # ----------------------------------------
    # Rejestracja Blueprint debug
    # Zadanie 2
    # ----------------------------------------

    from app.routes.debug import debug_bp

    app.register_blueprint(
        debug_bp
    )


    # ----------------------------------------
    # Rejestracja Blueprint dashboard
    # Zadanie 3
    # ----------------------------------------

    from app.routes.dashboard import dashboard_bp

    app.register_blueprint(
        dashboard_bp
    )


    # ----------------------------------------
    # Rejestracja Blueprint notifications
    # Zadanie 4
    # ----------------------------------------

    from app.routes.notifications import notifications_bp

    app.register_blueprint(
        notifications_bp
    )


     # ----------------------------------------
    # Rejestracja Blueprint recurring bookings
    # Zadanie 5
    # ----------------------------------------

    from app.routes.recurring_bookings import recurring_bookings_bp

    app.register_blueprint(
        recurring_bookings_bp
    )


    # ----------------------------------------
    # Rejestracja Blueprint reports
    # Zadanie 6
    # ----------------------------------------

    from app.routes.reports import reports_bp

    app.register_blueprint(
        reports_bp
    )


    # Zwracamy gotową aplikację Flask
    return app