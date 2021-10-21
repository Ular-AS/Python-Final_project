import requests
from food_analysis.analysis.api.constants import BASE_URL_ANALYSIS

class ReceptAnalysis:
    def __init__(self, url = BASE_URL_ANALYSIS):
        self.url = url

    def _food_analysis(self, name, ingridients):
        if isinstance(ingridients, str):
            ingridients = [ingridients]
        elif not isinstance(ingridients, list):
            return "Wrong type \"ingridients\""

        param = {
            'title': name,
            'ingr': ingridients
        }

        response = requests.post(self.url, json=param)
        if (response.status_code == 555)|(response.status_code == 500):
            return "It's impossible to analyze the recipe"
        elif response.status_code == 200:
            response_dict = response.json()
            response_str = response_dict["totalNutrients"]
            return response_str
        else:
            return "Server connection error"

    def create_report(self, name, ingridients):
        response_str = self._food_analysis(name, ingridients)
        if isinstance(response_str, str):
            return "It's impossible to analyze the recipe"
        l = response_str.keys()
        report = ""
        for i in l:
            report += "{}: {} {}\n".format(response_str[i]['label'], round(response_str[i]['quantity'], 2), response_str[i]['unit'])
        return report

    def get_calories(self, name, ingridients):
        response_str = self._food_analysis(name, ingridients)
        if isinstance(response_str, str):
            return "It's impossible to analyze the recipe"
        report = "{}: {} {}".format(response_str['ENERC_KCAL']['label'], round(response_str['ENERC_KCAL']['quantity'], 2), response_str['ENERC_KCAL']['unit'])
        return report