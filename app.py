from flask import Flask, url_for, jsonify
from markupsafe import escape

import numpy as np
import pandas as pd
import datetime as dt
import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import inspect, create_engine, func

engine = create_engine("sqlite:///Resources/hawaii.sqlite")
Base = automap_base()
Base.prepare(engine, reflect=True)
Measurement = Base.classes.measurement
Station = Base.classes.station
session = Session(engine)

app = Flask(__name__)

# List all routes that are available.

@app.route('/')
def home():
  return """<h2>List of all routes that are available:</h2>
  <p>
  <ul>
  <li><a href=/api/v1.0/precipitation>Precipitation</a> - JSON representation of precipitation
  <li><a href=/api/v1.0/stations>Stations</a> - List of stations
  <li><a href=/api/v1.0/tobs>TOBS</a> - List of Temperature Observations tobs) for previous year
  <li><a href=/api/v1.0/2017-06-01>2017-06-01</a> - JSON list of: min. temperature, avg. temperature, and max. temperature for all dates greater than or equal to start date.
  <li><a href=/api/v1.0/2017-06-01/2017-06-10>2017-06-01 - 2017-06-10</a> - JSON list of: min. temperature, avg. temperature, and max. temperature for all dates inclusive of the start and end date.
  </ul>"""

# Convert the query results to a Dictionary using `date` as the key and `prcp` as the value.
# Return the JSON representation of your dictionary.

@app.route('/api/v1.0/precipitation')
def precipitation():
  one_year_ago = dt.date(2017,8,23) - dt.timedelta(days=365)
  one_year_precip = session.query(Measurement.date, Measurement.prcp).filter(Measurement.date >= one_year_ago).order_by(Measurement.date).all()
  precip_dict = dict(one_year_precip)
  return jsonify(precip_dict)

# Return a JSON list of stations from the dataset.

@app.route('/api/v1.0/stations')
def stations():
  all_stations = session.query(Measurement.station, Station.name).group_by(Measurement.station).all()
  station_list = list(all_stations)
  return jsonify(station_list)

# query for the dates and temperature observations from a year from the last data point.
# Return a JSON list of Temperature Observations (tobs) for the previous year.

@app.route('/api/v1.0/tobs')
def tobs():
  one_year_ago = dt.date(2017,8,23) - dt.timedelta(days=365)
  one_year_tobs = session.query(Measurement.date, Measurement.tobs).filter(Measurement.date >= one_year_ago).order_by(Measurement.date).all()
  tobs_dict = dict(one_year_tobs)
  return jsonify(tobs_dict)

# Return a JSON list of the minimum temperature, the average temperature, and the max temperature for a given start or start-end range.
# When given the start only, calculate `TMIN`, `TAVG`, and `TMAX` for all dates greater than and equal to the start date.
# When given the start and the end date, calculate the `TMIN`, `TAVG`, and `TMAX` for dates between the start and end date inclusive.'''


#@app.route('/api/v1.0/2017-06-01')
#def start():
#  start_temp = session.query(Measurement.date, func.min(Measurement.tobs), func.avg(Measurement.tobs), func.max(Measurement.tobs)).filter(Measurement.date >= '2017-06-01').group_by(Measurement.date).all()
#  start_temp_list = list(start_temp)
#  return jsonify(start_temp_list)

#@app.route('/api/v1.0/2017-06-01/2017-06-10')
#def end():
    

# if __name__ == "__main__":
#  app.run(debug=True)