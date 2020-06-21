from flask import Flask, jsonify, request
from myclass_library import Film
from myclass_library import  FilmList
# from flask_cors import CORS
from pymongo import MongoClient

cluster = MongoClient('mongodb+srv://admin:Jhtk79@cluster0-3ijkd.mongodb.net/UntitledProject?retryWrites=true&w=majority')
db = cluster['UntitledProject']
collection = db['films']

app = Flask(__name__)
app.config['JSON_AS_ASCII'] = False
# CORS(app)
# cors = CORS(app, resources={r"/*": {"origins": "*"}})

@app.route('/catalog/<catalog_page_id>', methods=["GET"])
def main_page(catalog_page_id):
    list = FilmList()
    try: f_lst = int(catalog_page_id)*24
    except: f_lst= -1
    results = collection.find({"_id": {"$gte": f_lst-23, "$lte": f_lst}});
    for result in results:
        result = Film(result).dict_convert()
        list.add_film(result)
    return jsonify(list.show_list())

@app.route('/film/<film_id>', methods=["GET"])
def find_film(film_id):
    if request.method == "GET":
        list = FilmList()
        try: f_id = int(film_id)
        except: f_id = -1
        results = collection.find({"_id": f_id})
        for result in results:
            result = Film(result).dict_convert()
            list.add_film(result)
        return jsonify((list.show_list()))

@app.route('/film', methods=["POST"])
def insert_comment_fo_film():
    idd = int(dict(request.args)["id"])
    name = dict(request.args)["name"]
    comment = dict(request.args)["comment"]
    results = collection.find({"_id": idd})
    for result in results:
        result = Film(result).dict_convert()["comments"]
    result.append({
        "name": name,
        "comment": comment,
    })
    collection.update_one({"_id": idd}, {'$set': {"comments": result}})
    return('')
# app.run()
