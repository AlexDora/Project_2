import os

import pandas as pd
import numpy as np

import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine

from config import dbuser, dbpasswd, dburi, dbport

from flask import Flask, jsonify, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)


#################################################
# Database Setup
#################################################

app.config["SQLALCHEMY_DATABASE_URI"] = f"mysql://{dbuser}:{dbpasswd}@localhost:3306/sobrepeso_mexico_db"
db = SQLAlchemy(app)

db.init_app(app)
db.reflect(app=app)

meta = db.metadata
engine = db.engine

#sp = db.Table('sobrepeso', meta, autoload=True, autoload_with=engine)
estados = []
coordenadas = []
total_mujeres = []
sobrepeso_mujeres = []
total_hombres = []
sobrepeso_hombres = []

est = db.Table('entidades', meta, autoload=True, autoload_with=engine) 
ft = db.Table('Final_Table', meta, autoload=True, autoload_with=engine)

for row in db.session.query(est).all():
	estados.append(row[2])
	coordenadas.append(row[3])

for row in db.session.query(ft).all():
	total_mujeres.append(row[1])
	sobrepeso_mujeres.append(row[2])
	total_hombres.append(row[3])
	sobrepeso_hombres.append(row[4])

info_mujeres = [] 
info_hombres = []
total_muestra = []
total_sobrepeso = []

for i in range (0,len(total_mujeres)):
	info_mujeres.append(sobrepeso_mujeres[i] / total_mujeres[i])
	info_hombres.append(sobrepeso_hombres[i] / total_hombres[i])
	total_muestra.append(total_mujeres[i] + total_hombres[i])
	total_sobrepeso.append(sobrepeso_mujeres[i] + sobrepeso_hombres[i])
	i = i+1


@app.route("/generaldata")
def data():
	info_general = {"estados":estados, "coordenadas": coordenadas, "data_mujeres": total_mujeres,
					"data_hombres": total_hombres, "porcentaje_mujeres": info_mujeres,
					"porcentaje_hombres": info_hombres, "total_muestra": total_muestra, "total_sobrepeso": total_sobrepeso}
	return jsonify(info_general)


@app.route("/")
def index():
    return render_template("index.html")

@app.route("/map")
def map():
    return render_template("Obesity_Map.html")

@app.route("/graphs")
def graphs():
    return render_template("Obesity_Graphics.html")

@app.route("/table")
def table():
    return render_template("Data.html")



if __name__ == "__main__":
    app.run()