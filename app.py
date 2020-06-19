import numpy as np

import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func
from sqlalchemy import distinct

from flask import Flask, jsonify


#################################################
# Database Setup
#################################################
engine = create_engine("sqlite:///Countries.sqlite")

# reflect an existing database into a new model
Base = automap_base()
# reflect the tables
Base.prepare(engine, reflect=True)

# Save reference to the table
# Passenger = Base.classes.passenger

COVID_data = Base.classes.CountryData



#################################################
# Flask Setup
#################################################
app = Flask(__name__, template_folder="templates")


#################################################
# Flask Routes
#################################################

@app.route("/") # localhost:5000/ this is your index.html essentially
def welcome():
    """List all available api routes."""
    return (
        f"Available Routes:<br/>"
        f"/api/v1.0/names<br/>"
        f"/api/v1.0/sorted_COVID_data"
    )
    # inside your templates folder
    # return render_template("index.html", variable_in_html=variable_in_app)


# @app.route("/api/v1.0/names")
# def names():
#     # Create our session (link) from Python to the DB
#     session = Session(engine)

#     """Return a list of all passenger names"""
#     # Query all passengers
#  #   results = session.query(Passenger.name).all()

#     session.close()

#     # Convert list of tuples into normal list
#   #  all_names = list(np.ravel(results))

#     return jsonify(all_names)


@app.route("/api/v1.0/sorted_COVID_data")
def passengers():
    # Create our session (link) from Python to the DB
    session = Session(engine)

    """Return a list of passenger data including the name, age, and sex of each passenger"""
    # Query all passengers
    results = session.query(COVID_data.Country, COVID_data.total_cases1m_pop, COVID_data.test1m_pop, COVID_data.deaths1m_pop,COVID_data.death_rate).all()

    session.close()

    # Create a dictionary from the row data and append to a list of all_passengers
    all_Countries = []
    for Country in results:
        Country_dict = {}
        Country_dict["Country"] = Country[0]
        Country_dict['total_cases1m_pop'] = Country[1]
        Country_dict['test1m_pop'] = Country[2]
        Country_dict['deaths1m_pop'] = Country[3]
        Country_dict['death_rate(%)'] = Country[4]
        all_Countries.append(Country_dict)

    return jsonify(all_Countries)


if __name__ == '__main__':
    app.run(debug=True)
