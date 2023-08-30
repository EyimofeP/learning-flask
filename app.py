from flask import Flask, render_template, jsonify, request
from database import *

app = Flask(__name__)

# home page 
@app.route("/")
def hello():
    jobs = load_jobs_from_db()
    return render_template("home.html", jobs=jobs)

# view a job description
@app.route("/job/<id>")
def job_description(id):
    job = load_job_from_db(id)

    if not job:
        return "Not Found", 404
    return render_template("jobpage.html", job=job)

# make an application for a job 
@app.route("/job/<id>/apply", methods=["post"])
def apply_job(id):
    data = request.form
    job = load_job_from_db(id)

    add_application_to_db(id, data)
    return render_template("application_submitted.html", 
                           application=data, job=job)

# view all the list of applications 
@app.route("/admin/applications/")
def view_applications():
    applications =  load_applications_from_db()
    return render_template("view_applications.html", applications=applications)

# view a single application 
@app.route("/admin/application/<job_id>/<application_id>/view/")
def view_application(job_id, application_id):
    application = load_application_from_db(job_id, application_id)
    return render_template("view_application.html", application=application)

# show list of jobs in api format 
@app.route("/api/jobs")
def all_jobs_apis():
    jobs = load_jobs_from_db()
    return jsonify(jobs)

# show single jobs in api format 
@app.route("/api/job/<id>")
def job_api(id):
    job = load_job_from_db(id)
    return jsonify(job)


if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)