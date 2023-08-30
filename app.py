from flask import Flask, render_template, jsonify, request
from database import load_jobs_from_db, load_job_from_db, add_application_to_db, load_applications_from_db

app = Flask(__name__)

@app.route("/")
def hello():
    jobs = load_jobs_from_db()
    return render_template("home.html", jobs=jobs)

@app.route("/job/<id>")
def job_description(id):
    job = load_job_from_db(id)

    if not job:
        return "Not Found", 404
    return render_template("jobpage.html", job=job)

@app.route("/job/<id>/apply", methods=["post"])
def apply_job(id):
    data = request.form
    job = load_job_from_db(id)

    add_application_to_db(id, data)
    return render_template("application_submitted.html", 
                           application=data, job=job)

@app.route("/api/jobs")
def all_jobs_apis():
    jobs = load_jobs_from_db()
    return jsonify(jobs)

@app.route("/api/job/<id>")
def job_api(id):
    job = load_job_from_db(id)
    return jsonify(job)

@app.route("/admin/applications/")
def view_applications():
    applications =  load_applications_from_db()
    return render_template("view_applications.html", applications=applications)


if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)