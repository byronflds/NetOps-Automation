from flask import Blueprint, render_template, request, redirect, url_for, current_app
from app.models import Port
from app.services.billing_service import move_billing
from flask_login import login_required, current_user
from app.utils.decorators import admin_required

billing = Blueprint("billing", __name__, url_prefix="/billing")

@billing.route("/", methods=["GET","POST"])
@login_required
@admin_required
def adjust():
    if request.method == "POST":
        source_id = request.form.get("source_port")
        dest_id = request.form.get("dest_port")

        try:
            move_billing(int(source_id), int(dest_id))
            current_app.logger.info("Billing move completed")
            return redirect(url_for("billing.adjust"))
        except ValueError as e:
            current_app.logger.warning(f"Billing move failed: {e}")
            ports = Port.query.all()
            return render_template("billing.html", ports=ports, error=str(e))
    
    ports = Port.query.all()
    return render_template("billing.html", ports=ports)