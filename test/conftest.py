import pytest
import json
import pathlib
from src.db_code import db


@pytest.fixture
def sql_fixture():
    """Return an instance of class SQLConnection"""
    return db.SQLConnection()

@pytest.fixture
def json_config(request):
    file = pathlib.Path(request.node.fspath.strpath)
    config = file.with_name('filter.json')
    with config.open() as fp:
        return json.load(fp)

