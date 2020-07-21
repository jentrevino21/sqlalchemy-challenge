## Step 2 - Climate App
import numpy as np
import pandas as pd
import datetime as dt
import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, inspect, func
from flask import Flask, jsonify

engine = create_engine("sqlite:///Resources/hawaii.sqlite")

# reflect an existing database into a new model
Base = automap_base()
Base.prepare(engine, reflect=True)
# Base.classes.keys()

# session = Session(engine)
measurement = Base.classes.measurement
station = Base.classes.station

app = Flask(__name__)

@app.route ('/')

def welcome():
    
    return (
        f"Available Routes:<br/>"
        f"/api/v1.0/precipitation<br/>"
        f"/api/v1.0/stations<br/>"
        f"/api/v1.0/tobs<br/>")
    
@app.route("/api/v1.0/precipitation")

def precipitation():
#     #Create our session (link) from Python to the DB
    session = Session(engine)
    session.query(func.max(Measurement.date)).all()
    last_year = dt.date(2017,8,23)-dt.timedelta(days=365)
    result = session.query(Measurement.date, Measurement.prcp).\
    filter(Measurement.date >= last_year).order_by(Measurement.date).all()
#     # Create a dictionary from the row data and append to a list of all_dates
    all_dates = []
    for date, prcp in result:
        precipitation_dict = {}
        precipitation_dict["date"] = date
        precipitation_dict["prcp"] =prcp
        all_dates.append(precipitation_dict)
    return jsonify(all_dates)


if __name__ == "__main__":
    app.run(debug=True)


