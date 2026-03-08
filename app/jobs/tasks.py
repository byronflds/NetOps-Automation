import time
from app.services.port_service import create_port

def create_port_job(switch_name: str, port_name: str, status: str):
    # Simulate a long-running task
    time.sleep(5)
    port = create_port(switch_name, port_name, status)
    return {
        "id": port.id,
        "switch_name": port.switch_name,
        "port_name": port.port_name,
        "status": port.status
    }