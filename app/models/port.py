from app.extensions import db

class Port(db.Model):
    __tablename__ = "ports"

    id = db.Column(db.Integer, primary_key=True)
    switch_name = db.Column(db.String(100), nullable=False)
    port_name = db.Column(db.String(50), nullable=False)
    status = db.Column(db.String(20), nullable=False)
    is_uplink = db.Column(db.Boolean, default=False)
    vlan_id = db.Column(db.Integer, nullable=True)
    billing_account = db.Column(db.String(50), nullable=True)

    def __repr__(self):
        return f"<Port {self.switch_name}:{self.port_name} ({self.status}), Billing: {self.billing_account}>"