import pandas as pd
reader=pd.read_csv("/Users/lars/Documents/Github/project2lars/merged_data.csv")

for index, row in reader.iterrows():
    d=row.to_dict()
    print(d)



from flask import Flask, request, jsonify
import os 

app = Flask(__name__)

@app.route("/". methods=["GET"])
def

@app.route("/movies/", methods=["GET"])
def movies():
    session = Session(engine)

    entries=session.query(Movie.title, Movie.director).all()
    
    session.close()
    all_entries = []
    for m in entries:
        movies_dict = {m.title:{m.director:r.release_year}}
        all_entries.append(movies_dict)

    return jsonify(all_entries)

@app.route("/movies/<moviename>/", methods=["GET"])
def movie_name(moviename):
    session = Session(engine)

    session.close()
    return jsonify(session.query(Movie.title, Movie.director, Movie.release_year).filter(Movie.title == moviename).all())
        #add other fields 

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
