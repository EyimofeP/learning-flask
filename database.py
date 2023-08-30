import os
from sqlalchemy import create_engine, text

db_connection_string = os.environ["DB_connection"]

# connect to the cloud database
engine = create_engine(db_connection_string, connect_args={
        "ssl": {
            "ssl_ca": "/etc/ssl/cert.pem",
        }
    })

# fetch jobs data from database
def load_jobs_from_db():
    with engine.connect() as conn:
        result = conn.execute(text("SELECT * FROM jobs"))
        
        jobs = []
        for row in result.all():
            jobs.append(dict(row._mapping))

        return jobs

# fetch data of one single row
def load_job_from_db(id):
    with engine.connect() as conn:
        result = conn.execute(text(f"SELECT * FROM jobs WHERE id={id}"))
        
        #spool all the rows
        results = result.all()

        # if more than one row, turn to dict else return None
        if len(results) == 0:
            return None
        else:
            return dict(results[0]._mapping)


# add application data to the database
def add_application_to_db(job_id, application):
    with engine.connect() as conn:
        query = text("INSERT INTO applications (job_id, full_name, email, linkedin_url, education, work_experience, resume_url) VALUES (:job_id, :full_name, :email, :linkedin_url, :education, :work_experience, :resume_url)")
    
        params = {
            "job_id": job_id,
            "full_name": application['full_name'],
            "email": application['email'],
            "linkedin_url": application['linkedin_url'],
            "education": application['education'],
            "work_experience": application['work_experience'],
            "resume_url": application['resume_url']
        }
        
        conn.execute(query, params)
        conn.commit()

# fetch applications from Database
def load_applications_from_db():
    with engine.connect() as conn:
        result = conn.execute(text("SELECT * FROM jobs JOIN applications ON jobs.id = applications.job_id"))

        #spool all rows
        applications = []
        for row in result.all():
            applications.append(dict(row._mapping))

        return applications