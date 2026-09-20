# Zadanie 4 – System powiadomień

## Cel zadania

Celem zadania było dodanie do aplikacji systemu powiadomień związanego z rezerwacjami sal.

System obsługuje dwa rodzaje automatycznych powiadomień:

- powiadomienie dla administratora po utworzeniu nowej rezerwacji,
- przypomnienie dla użytkownika około 1 godzinę przed rozpoczęciem rezerwacji.

Dodatkowo zostały utworzone endpointy API umożliwiające pobieranie nieprzeczytanych powiadomień oraz oznaczanie ich jako przeczytane.

---

## 1. Model Notification

W pliku:

```text
app/models.py
```

utworzyłam model `Notification`:

```python
class Notification(db.Model):
    """Powiadomienie przypisane do użytkownika."""

    __tablename__ = 'notifications'

    id = db.Column(
        db.Integer,
        primary_key=True
    )

    user_id = db.Column(
        db.Integer,
        db.ForeignKey('users.id'),
        nullable=False
    )

    message = db.Column(
        db.String(500),
        nullable=False
    )

    is_read = db.Column(
        db.Boolean,
        default=False,
        nullable=False
    )

    created_at = db.Column(
        db.DateTime,
        default=datetime.utcnow,
        nullable=False
    )

    user = db.relationship(
        'User',
        backref='notifications'
    )

    def to_dict(self):
        return {
            'id': self.id,
            'user_id': self.user_id,
            'message': self.message,
            'is_read': self.is_read,
            'created_at': self.created_at.isoformat()
        }
```

Model przechowuje:

- `id` – identyfikator powiadomienia,
- `user_id` – użytkownika, do którego należy powiadomienie,
- `message` – treść wiadomości,
- `is_read` – informację, czy powiadomienie zostało przeczytane,
- `created_at` – datę utworzenia powiadomienia.

Metoda `to_dict()` umożliwia zamianę powiadomienia na słownik, który może zostać zwrócony przez API jako JSON.

---

## 2. Automatyczne powiadomienie dla administratora

Po utworzeniu nowej rezerwacji system automatycznie tworzy powiadomienie dla administratora.

Do tego wykorzystałam event SQLAlchemy:

```python
@event.listens_for(
    Booking,
    'after_insert'
)
```

Listener uruchamia się automatycznie po zapisaniu nowego obiektu `Booking` w bazie danych.

```python
@event.listens_for(Booking, 'after_insert')
def create_admin_notification(mapper, connection, target):

    users_table = User.__table__

    result = connection.execute(
        users_table.select().where(
            users_table.c.is_admin.is_(True)
        )
    )

    admins = result.fetchall()

    message = (
        f'Nowa rezerwacja: "{target.title}" '
        f'(ID rezerwacji: {target.id})'
    )

    for admin in admins:
        connection.execute(
            Notification.__table__.insert().values(
                user_id=admin.id,
                message=message,
                is_read=False,
                created_at=datetime.utcnow()
            )
        )
```

Po utworzeniu rezerwacji system:

1. wykrywa zapis nowego `Booking`,
2. wyszukuje użytkowników z `is_admin=True`,
3. tworzy wiadomość dotyczącą nowej rezerwacji,
4. zapisuje powiadomienie dla administratora.

Przykładowe powiadomienie:

```text
Nowa rezerwacja: "Test przypomnienia 1h" (ID rezerwacji: 21)
```

Schemat działania:

```text
Nowa rezerwacja
      ↓
Booking
      ↓
after_insert
      ↓
wyszukanie administratora
      ↓
Notification
```

---

## 3. Przypomnienie 1 godzinę przed rezerwacją

Drugim rodzajem powiadomienia jest automatyczne przypomnienie dla użytkownika przed rozpoczęciem jego rezerwacji.

W tym celu utworzyłam plik:

```text
app/reminders.py
```

Znajduje się w nim funkcja:

```python
def create_upcoming_booking_notifications(app):
```

Funkcja sprawdza rezerwacje rozpoczynające się za około godzinę:

```python
now = datetime.now()

start_range = now + timedelta(minutes=55)
end_range = now + timedelta(minutes=65)

bookings = Booking.query.filter(
    Booking.start_time >= start_range,
    Booking.start_time <= end_range,
    Booking.status != 'cancelled'
).all()
```

Zakres 55–65 minut pozwala znaleźć rezerwacje rozpoczynające się za około godzinę.

Dla znalezionej rezerwacji tworzona jest wiadomość:

```python
message = (
    f'Przypomnienie: rezerwacja '
    f'"{booking.title}" rozpoczyna się '
    f'o {booking.start_time.strftime("%H:%M")} '
    f'(ID rezerwacji: {booking.id})'
)
```

Przed zapisaniem system sprawdza, czy takie powiadomienie już istnieje:

```python
existing_notification = (
    Notification.query
    .filter_by(
        user_id=booking.user_id,
        message=message
    )
    .first()
)
```

Dzięki temu to samo przypomnienie nie jest tworzone wielokrotnie.

Jeżeli przypomnienia jeszcze nie ma, tworzony jest nowy obiekt:

```python
notification = Notification(
    user_id=booking.user_id,
    message=message
)

db.session.add(notification)
```

Na końcu zmiany są zapisywane:

```python
db.session.commit()
```

---

## 4. Automatyczne sprawdzanie rezerwacji – APScheduler

Aby system mógł sam sprawdzać czas rozpoczęcia rezerwacji, wykorzystałam bibliotekę `APScheduler`.

Scheduler został skonfigurowany w `run.py`:

```python
scheduler = BackgroundScheduler()

scheduler.add_job(
    func=lambda: create_upcoming_booking_notifications(app),
    trigger='interval',
    minutes=1
)

scheduler.start()
```

Scheduler uruchamia funkcję sprawdzającą rezerwacje co 1 minutę.

Działanie:

```text
APScheduler
     ↓
co 1 minutę
     ↓
sprawdzenie rezerwacji
     ↓
rezerwacja za około 1h?
     ↓
TAK
     ↓
Notification dla użytkownika
```

Dzięki temu przypomnienie może zostać utworzone automatycznie bez wykonywania dodatkowego żądania przez użytkownika.

---

## 5. API powiadomień

Dla systemu powiadomień utworzyłam plik:

```text
app/routes/notifications.py
```

oraz Blueprint:

```python
notifications_bp = Blueprint(
    'notifications',
    __name__
)
```

Blueprint został następnie zarejestrowany w `app/__init__.py`:

```python
from app.routes.notifications import notifications_bp

app.register_blueprint(
    notifications_bp
)
```

---

## 6. GET /api/notifications

Endpoint:

```text
GET /api/notifications
```

zwraca listę nieprzeczytanych powiadomień.

```python
@notifications_bp.route(
    '/api/notifications',
    methods=['GET']
)
def get_notifications():

    notifications = (
        Notification.query
        .filter_by(is_read=False)
        .order_by(Notification.created_at.desc())
        .all()
    )

    return jsonify([
        notification.to_dict()
        for notification in notifications
    ])
```

Warunek:

```python
.filter_by(is_read=False)
```

powoduje pobranie tylko nieprzeczytanych powiadomień.

Natomiast:

```python
.order_by(Notification.created_at.desc())
```

sortuje je od najnowszego do najstarszego.

Jeżeli nie ma nieprzeczytanych powiadomień, API zwraca:

```json
[]
```

---

## 7. POST /api/notifications/<id>/read

Endpoint:

```text
POST /api/notifications/<id>/read
```

umożliwia oznaczenie wybranego powiadomienia jako przeczytane.

```python
@notifications_bp.route(
    '/api/notifications/<int:notification_id>/read',
    methods=['POST']
)
def mark_notification_as_read(notification_id):

    notification = db.session.get(
        Notification,
        notification_id
    )

    if notification is None:
        return jsonify({
            'error': 'Nie znaleziono powiadomienia'
        }), 404

    notification.is_read = True

    db.session.commit()

    return jsonify({
        'message': (
            'Powiadomienie oznaczone '
            'jako przeczytane'
        ),
        'notification': notification.to_dict()
    })
```

Po znalezieniu powiadomienia jego wartość:

```python
is_read
```

jest zmieniana na:

```python
True
```

i zapisywana w bazie danych.

Jeżeli powiadomienie o podanym ID nie istnieje, API zwraca status `404`.

---

## 8. Test działania

Do sprawdzenia całego mechanizmu utworzyłam testową rezerwację:

```text
ID rezerwacji: 21
Nazwa: Test przypomnienia 1h
Godzina rozpoczęcia: 16:19
```

Po utworzeniu rezerwacji event `after_insert` automatycznie utworzył powiadomienie dla administratora:

```text
Nowa rezerwacja: "Test przypomnienia 1h" (ID rezerwacji: 21)
```

Powiadomienie zostało przypisane do administratora:

```text
user_id: 4
```

Następnie scheduler wykrył, że rezerwacja rozpoczyna się za około godzinę i automatycznie utworzył przypomnienie:

```text
Przypomnienie: rezerwacja "Test przypomnienia 1h"
rozpoczyna się o 16:19 (ID rezerwacji: 21)
```

Przypomnienie zostało przypisane do użytkownika posiadającego rezerwację:

```text
user_id: 1
```

Oba powiadomienia zostały zapisane w bazie i były widoczne przez:

```text
GET /api/notifications
```

Endpoint zwrócił:

```text
HTTP 200
```

---

# Wynik

System powiadomień został zaimplementowany i działa prawidłowo.

Zrealizowane zostały:

- model `Notification`,
- powiązanie powiadomienia z użytkownikiem,
- automatyczne powiadomienie administratora po utworzeniu rezerwacji,
- event SQLAlchemy `after_insert`,
- automatyczne przypomnienie użytkownika około 1 godzinę przed rezerwacją,
- cykliczne sprawdzanie rezerwacji za pomocą `APScheduler`,
- zabezpieczenie przed wielokrotnym utworzeniem tego samego przypomnienia,
- `GET /api/notifications`,
- pobieranie nieprzeczytanych powiadomień,
- `POST /api/notifications/<id>/read`,
- oznaczanie powiadomień jako przeczytane.

Końcowy mechanizm działania:

```text
                  REZERWACJA
                      ↓
              ┌───────┴───────┐
              ↓               ↓
         after_insert      APScheduler
              ↓               ↓
     powiadomienie       około 1h przed
        dla admina             ↓
                       przypomnienie dla
                          użytkownika
              ↓               ↓
              └───────┬───────┘
                      ↓
                 Notification
                      ↓
            GET /api/notifications
                      ↓
       POST /api/notifications/<id>/read
```

Test potwierdził poprawne utworzenie zarówno powiadomienia dla administratora, jak i przypomnienia dla użytkownika przed rozpoczęciem rezerwacji.
