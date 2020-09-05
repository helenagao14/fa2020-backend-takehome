from flask import Flask, redirect
import csv
import json
import random
import pandas as pd

app = Flask(__name__)

"""

TASK

Implement an endpoint `/api/fetch` that returns the contents of `data.csv` as JSON

1) Load/transcribe `data.csv`
2) Save each entry's full name, time zone, and department
3) Return the JSON data at the endpoint


    employees: [
        {
            name: <full name of employee>,
            timezone: <timezone of employee>,
            dept: <department of employee>
        }

"""


# your work here
@app.route("/api/fetch")
def fetch_data():
    # data = {'employees': ['name', 'timezone', 'dept']}
    data = {}
    with open("data.csv") as csvFile:
        csvReader = csv.DictReader(csvFile)
        list = []
        for rows in csvReader:
            emp_details = {"name": None, "timezone": None, "dept": None}
            emp_details['name'] = rows['first_name'] + ' ' + rows['last_name']
            emp_details['timezone'] = rows['time_zone']
            emp_details['dept'] = rows['dept']
            list.append(emp_details)

    data['employees'] = list
    #print(data)   no pretty print
    #print(json.dumps(data, indent=1)) pretty print

    return json.dumps(data, indent=1)


"""

DOCUMENTATION WEBPAGE BELOW

"""


@app.route("/")
def redirect_to_api():
    return redirect("/api", code=301)


@app.route("/api")
def api_home():
    return """
        <style>
            body {
                font-family: sans-serif;
                max-width: 900px;
                width: 90%;
                margin: 0 auto 0 auto;
                padding: 5vh 30px 0 30px;
                background: rgb(240,240,240);
            }

            pre, code {
                background: #121212;
                color: white;
            }

            code {
                padding: 4px;
            }

            pre code {
                padding: 0;
            }

            pre {
                padding: 10px;
            }

            hr {
                margin: 2em 0;
            }
        </style>
        <h1>Founders Fall 2020 Backend Take-Home API</h1>
        <p>Add the endpoint <code>`/api/fetch`</code> accessible via a GET request which returns the list of employees from <code>`data.csv`</code> as JSON.</p><hr />
        <h2>API (to be implemented)</h2>
        <h4>Request</h4>
<pre><code><b>GET</b>
Scheme: http
Filename: /api/fetch</code></pre>
        <h4>Response</h4>
<pre><code>employees: [
            <br />  {
            <br />      name: <i>FULL NAME OF EMPLOYEE</i>,
            <br />      timezone: <i>TIMEZONE</i>,
            <br />      dept: <i>EMPLOYEE'S DEPARTMENT</i>,
            <br />  }
            <br />  ...
        <br />]</code></pre>"""
