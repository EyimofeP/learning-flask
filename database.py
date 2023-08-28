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
    
    
    