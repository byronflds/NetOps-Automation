import time

def create_port_job(port_name: str):
    # Simulate a long-running task
    time.sleep(5)
    print(f"Port {port_name} created successfully.")
    return {"status": "success", "port": port_name}