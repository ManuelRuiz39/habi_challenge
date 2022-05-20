import pytest

"""def test_cursor_mysql(sql_fixture):
    assert(sql_fixture.create_conecction())"""

def test_query_mysql(sql_fixture):
    assert type(sql_fixture.make_query()) is list

