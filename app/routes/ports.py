from flask import Blueprint, render_template, request, redirect, url_for, current_app
from app.services.port_service import create_port, get_all_ports

ports = Blueprint("ports", __name__, url_prefix="/ports")

@ports.route("/", methods=["GET","POST"])
@login_required
def manage_ports():
    if current_user.role != "admin":
        abort(403)
    if request.method == "POST":
        switch_name = request.form.get("switch_name")
        port_name = request.form.get("port_name")
        status = request.form.get("status")

        if not switch_name or not port_name or not status:
            current_app.logger.warning("Port creation failed: missing fields")
            return redirect(url_for("ports.manage_ports"))
        try:
            port = create_port(switch_name, port_name, status)
            current_app.logger.info(f"Port created: {port}")
        except ValueError as e:
            current_app.logger.warning(f"Port creation failed: {e}")
            return render_template("ports.html", error=str(e), ports=get_all_ports())

        return redirect(url_for("ports.manage_ports"))
    
    ports_list = get_all_ports()
    return render_template("ports.html", ports=ports_list)
        


