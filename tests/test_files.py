import os
import shutil

import pytest
from food_analysis.analysis.recepts_files.recepts_files import Recepts
from tests.constants import IN_DIR, OUT_DIR, R_1, R_2, R_3, R_4, BASE_NAME, BASE_INGRIDIENTS

def test_constructor():
    try:
        Recepts("abc", "abc")
        assert False, "ValueError for incorrect path must be raise"
    except ValueError:
        assert True

    try:
        Recepts(IN_DIR, "abc")
        assert False, "ValueError for incorrect path must be raise"
    except ValueError:
        assert True

def test_get_recept():
    r = Recepts(IN_DIR, R_1)
    dict_ok = r.get_recept()
    print(dict_ok["ingridients"])
    assert dict_ok["name"] == BASE_NAME, "Error in \"name\" format"
    assert dict_ok["ingridients"] == BASE_INGRIDIENTS, "Error in \"ingridients\" format"

    r = Recepts(IN_DIR, R_2)
    dict_ok = r.get_recept()
    assert dict_ok["name"] == BASE_NAME, "Error in \"name\" format"
    assert dict_ok["ingridients"] == BASE_INGRIDIENTS, "Error in \"ingridients\" format"

    r = Recepts(IN_DIR, R_3)
    dict_ok = r.get_recept()
    assert dict_ok["name"] == "", "Error in \"name\" format"

    r = Recepts(IN_DIR, R_4)
    dict_ok = r.get_recept()
    assert dict_ok["ingridients"] == [], "Error in \"ingridients\" format"

def test_make_out_dir():
    r = Recepts(IN_DIR, R_1)
    r._make_out_dir()
    assert os.path.isdir(OUT_DIR), "Path not created"

def test_write_report():
    r = Recepts(IN_DIR, R_1)
    ans = r.write_report()

    assert ans == "Recipe analysis is formed", "Error in creating the analysis"
    assert os.path.isfile(os.path.join(OUT_DIR, R_1)), "Error in file creation"

@pytest.fixture(autouse=True)
def file_struct():
    os.mkdir(IN_DIR)
    for file in os.listdir(r"tests\resources"):
        shutil.copy(os.path.join(r"tests\resources", file), os.path.join(IN_DIR, file))
    yield
    shutil.rmtree(IN_DIR)





