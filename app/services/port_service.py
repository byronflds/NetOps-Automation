from app.extensions import db
from app.models import Port
from app.services.audit_service import log_action

def create_port(switch_name, port_name, status, is_uplink=False, vlan_id=None):

    if vlan_id is not None:
        raise ValueError("VLAN assignment is not supported in this service.")
    
    existing = Port.query.filter_by(switch_name=switch_name, port_name=port_name).first()
    if existing:
        raise ValueError("Port already exists.")
    
    port = Port(
        switch_name = switch_name,
        port_name = port_name,
        status=status,
        is_uplink=is_uplink,
        vlan_id=vlan_id
    )

    db.session.add(port)
    db.session.commit()

    log_action(
        action="CREATE_PORT",
        details=f"{switch_name}:{port_name} status={status}"
    )

    return port

def get_all_ports():
    return Port.query.all()