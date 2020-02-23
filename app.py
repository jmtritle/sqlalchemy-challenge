from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
'''
  * List all routes that are available.
'''

@app.route('/api/v1.0/precipitation')
def precipitation():

'''
  * Convert the query results to a Dictionary using `date` as the key and `prcp` as the value.

  * Return the JSON representation of your dictionary.
'''

@app.route('/api/v1.0/stations')
def stations():

'''  

* Return a JSON list of stations from the dataset.
'''
@app.route('/api/v1.0/tobs')
def tobs():

'''
  * query for the dates and temperature observations from a year from the last data point.
  * Return a JSON list of Temperature Observations (tobs) for the previous year.
'''

@app.route('')
def start():

@app.route('')
def end():
    
'''
* `/api/v1.0/<start>` and `/api/v1.0/<start>/<end>`

  * Return a JSON list of the minimum temperature, the average temperature, and the max temperature for a given start or start-end range.

  * When given the start only, calculate `TMIN`, `TAVG`, and `TMAX` for all dates greater than and equal to the start date.

  * When given the start and the end date, calculate the `TMIN`, `TAVG`, and `TMAX` for dates between the start and end date inclusive.'''