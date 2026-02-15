from app.services.port_service import create_port
from app.models import Port
from app import db

def test_create_port(app):
    port = create_port(
        switch_name="core-sw-01",
        port_name="Gi1/0/1",
        status="down",
        is_uplink=False
    )

    saved = Port.query.first()

    assert saved is not None
    assert saved.port_name == "Gi1/0/1"
