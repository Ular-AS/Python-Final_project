import requests.exceptions
from food_analysis.analysis.api.api_recepts import ReceptAnalysis
from tests.constants import BASE_NAME, BASE_INGRIDIENTS, STRING_INGRIDIENTS, MIS_INGRIDIENTS

def test_food_analysis():
    recept = ReceptAnalysis()

    dict_ok = recept._food_analysis(BASE_NAME, BASE_INGRIDIENTS)

    assert isinstance(dict_ok, dict), "Should return \"dict\""

    dict_ok1 = recept._food_analysis(BASE_NAME, STRING_INGRIDIENTS)

    assert isinstance(dict_ok1, dict), "Should return \"dict\""

    dict_false = recept._food_analysis(BASE_NAME, 1)

    assert dict_false == "Wrong type \"ingridients\"", "Should return type error"

    dict_500 = recept._food_analysis(BASE_NAME, MIS_INGRIDIENTS)

    assert dict_500 == "It's impossible to analyze the recipe", "Analysis should not be performed"

    recept_false = ReceptAnalysis("http://qwedwfqaqfsadawwdwqwavg")

    try:
        recept_false._food_analysis(BASE_NAME, BASE_INGRIDIENTS)
        assert False, "Must fail with this URL"
    except requests.exceptions.ConnectionError:
        assert True

def test_create_report():
    recept = ReceptAnalysis()
    assert recept.create_report(BASE_NAME, BASE_INGRIDIENTS) != "", "The report line should be returned"
    assert recept.create_report(BASE_NAME, MIS_INGRIDIENTS) == "It's impossible to analyze the recipe", "An empty string should be returned"

def test_get_calories():
    recept = ReceptAnalysis()
    assert recept.get_calories(BASE_NAME, BASE_INGRIDIENTS) != "", "The report line should be returned"
    assert recept.get_calories(BASE_NAME, MIS_INGRIDIENTS) == "It's impossible to analyze the recipe", "An empty string should be returned"

