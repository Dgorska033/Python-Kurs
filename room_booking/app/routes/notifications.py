from flask import Blueprint, jsonify

from app import db
from app.models import Notification


notifications_bp = Blueprint(
    'notifications',
    __name__
)


# ==========================================
# GET /api/notifications
# ==========================================

@notifications_bp.route(
    '/api/notifications',
    methods=['GET']
)
def get_notifications():
    """
    Zwraca listę nieprzeczytanych
    powiadomień.
    """

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


# ==========================================
# POST /api/notifications/<id>/read
# ==========================================

@notifications_bp.route(
    '/api/notifications/<int:notification_id>/read',
    methods=['POST']
)
def mark_notification_as_read(notification_id):
    """
    Oznacza powiadomienie jako przeczytane.
    """

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