from app.extensions import db
from app.models import Port
from app.services.audit_service import log_action

def move_billing(source_id, dest_id):
    source = Port.query.get(source_id)
    dest = Port.query.get(dest_id)

    if not source or not dest:
        raise ValueError("One or both ports do not exist")
    
    if source.is_uplink or dest.is_uplink:
        raise ValueError("Uplink ports cannot be modified")
    
    if not source.billing_account:
        raise ValueError("Source port has no billing assigned")
    
    if dest.billing_acount:
        raise ValueError("Destination port already has billing")
    
    try:
        dest.billing_account = source.billing_account
        source.billing_account = None

        db.session.commit()

        log_action(
            action="MOVE_BILLING",
            details=f"Billing moved from port {source.id} to port {dest.id}"
        )
    except Exception:
        db.session.rollback()
        raise