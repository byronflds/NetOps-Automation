from functools import wraps
from flask_login import current_user

def admin_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if not current_user.is_authenticated:
            abort(401)
        
        if current_user.role != "admin":
            current_app.logger.warning(
    f"Unauthorized admin access attempt by user {current_user.username}"
)
            abort(403)
        
        return f(*args, **kwargs)
    return decorated_function
