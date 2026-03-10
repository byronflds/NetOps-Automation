from flask import Blueprint
from flask_login import login_required
from rq.job import Job
from app.jobs import redis_conn

jobs = Blueprint("jobs", __name__, url_prefix="/jobs")


@jobs.route("/<job_id>")
@login_required
def job_status(job_id):

    job = Job.fetch(job_id, connection=redis_conn)

    return {
        "job_id": job.id,
        "status": job.get_status(),
        "result": job.result
    }