from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from config import config


app = Flask(__name__)

# Wczytujemy konfigurację developerską
app.config.from_object(config['development'])

# Łączymy SQLAlchemy z aplikacją
db = SQLAlchemy(app)


# Prosty model służący do testowania połączenia
class TestConnection(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    message = db.Column(db.String(100))


# Strona główna
@app.route('/')
def index():
    return "Flask + PostgreSQL działa! 🎉"


# Test połączenia z PostgreSQL
@app.route('/test-db')
def test_db():
    """Testuje połączenie z bazą."""

    try:
        # Najprostsze możliwe zapytanie SQL
        db.session.execute(db.text('SELECT 1'))

        return "✅ Połączenie z PostgreSQL OK!"

    except Exception as e:
        return f"❌ Błąd połączenia: {str(e)}"


if __name__ == '__main__':

    # Tworzymy tabelę TestConnection,
    # jeśli jeszcze nie istnieje.
    with app.app_context():
        db.create_all()
        print("Tabele utworzone!")

    app.run(debug=True)