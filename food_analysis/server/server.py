import json
from flask import Flask, request
from food_analysis.analysis.api.api_recepts import ReceptAnalysis

app = Flask(__name__)

@app.route('/get_calories', methods=['POST'])
def get_calories():
    data = request.json
    print(request)
    if data is None:
        return "The request is missing json", 400

    if "name" not in data:
        return "Name should be in keys", 400
    if "ingridients" not in data:
        return "Ingridients should be in keys", 400

    name_new = data.get("name")
    ingridients_new = data.get("ingridients")
    if not isinstance(name_new, str):
        return "Name should be string", 400
    if not isinstance(ingridients_new, list):
        return "Ingridients should be list", 400

    api = ReceptAnalysis()
    calories = {"calories": api.get_calories(name_new, ingridients_new)}
    return json.dumps(calories)

@app.route('/get_analysis', methods=['POST'])
def get_analysis():
    data = request.json
    print(request)
    if data is None:
        return "The request is missing json", 400

    if "name" not in data:
        return "Name should be in keys", 400
    if "ingridients" not in data:
        return "Ingridients should be in keys", 400

    name_new = data.get("name")
    ingridients_new = data.get("ingridients")
    if not isinstance(name_new, str):
        return "Name should be string", 400
    if not isinstance(ingridients_new, list):
        return "Ingridients should be list", 400

    api = ReceptAnalysis()
    analysis = {"analysis": api.create_report(name_new, ingridients_new)}
    return json.dumps(analysis)
