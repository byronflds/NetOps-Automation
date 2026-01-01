from app import db

class Port(db.model):
    __tablename__ = "ports"

    id = db.Column(db.Integer, primary_key=True)
    switch_name = db.Column(db.String(100), nullable=False)
    port_name = db.Column(db.String(50), nullable=False)
    status = db.Column(db.String(20), nullable=False)
    is_uplink = db.Column(db.Boolean, default=False)

    def __repr__(self):
        return f"<Port {self.switch_name}:{self.port_name} ({self.status})>"