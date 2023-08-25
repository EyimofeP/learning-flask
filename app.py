from flask import Flask, render_template

app = Flask(__name__)

jobs = [
    {
        "id" : 1,
        "title" : "Data Analyst",
        "location" : "FCT, Nigeria",
        "salary" : "NGN 2,000,000"
    },
    {
        "id" : 2,
        "title" : "Data Scientist",
        "location" : "Lagos, Nigeria",
        "salary" : "NGN 20,000,000"
    },
    {
        "id" : 3,
        "title" : "Frontend Engineer",
        "location" : "Remote",
        # "salary" : "NGN 12,000,000"
    },
    {
        "id" : 4,
        "title" : "Backend Engineer",
        "location" : "New York, USA",
        "salary" : "$ 120,000"
    },
]

@app.route("/")
def hello():
    return render_template("home.html", jobs=jobs)

if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)