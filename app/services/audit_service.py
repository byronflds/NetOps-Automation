from app.extensions import db
from app.models.audit_log import AuditLog

def log_action(action,details):
    entry = AuditLog(
        action=action,
        details=details
    )
db.session.add(entry)
db.session.commit()