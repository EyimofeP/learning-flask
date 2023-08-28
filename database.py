from sqlalchemy import create_engine, text

db_connection_string = "mysql://LZgJYDwGsBDVdrM.root:BJ10Nl6rXI4ta99R@gateway01.us-west-2.prod.aws.tidbcloud.com:4000/pintycareers"

engine = create_engine(db_connection_string, connect_args={
        "ssl": {
            "ssl_ca": "/etc/ssl/cert.pem",
        }
    })

with engine.connect() as conn:
    result = conn.execute(text("SELECT * FROM jobs"))
    print(result.all())

