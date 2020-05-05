import pandas as pd
from flask import Flask, request, jsonify
import os 
import csv

file = '/Users/lars/Documents/Github/project2lars/merged_data.csv'
with open(file) as fh:
    rd = csv.DictReader(fh, delimiter=',')
    dictionary = []
    for row in rd:
        dictionary.append(row)
        
reader=pd.read_csv("/Users/lars/Documents/Github/project2lars/merged_data.csv")

dict_row={}
movies_dict={}
for index, row in reader.iterrows():
    d=row.to_dict()
    dict_row={d['title']:d}
    movies_dict.update(dict_row)


app = Flask(__name__)

@app.route("/", methods=["GET"])
def index():
    return jsonify(movies_dict)

@app.route("/movies/", methods=["GET"])
def movies():
    movies_list=[]
    for index, row in reader.iterrows():
        d=row.to_dict()
        movies_list.append(d['title'])
    return jsonify(movies_list)

@app.route("/movies/<moviename>/", methods=["GET"])
def movie_name(moviename):
    return jsonify(movies_dict[moviename])

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
