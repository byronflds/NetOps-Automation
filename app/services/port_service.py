from app import db
from app.models import Port

def create_port(switch_name, port_name, status, is_uplink=False):
    port = Port(
        switch_name = switch_name,
        port_name = port_name,
        status=status,
        is_uplink=is_uplink
    )

    db.session.add(port)
    db.session.commit()

    return port

def get_all_ports():
    return Port.query.all()