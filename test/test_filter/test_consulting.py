import pytest

from src.main_code import consulting

@pytest.mark.parametrize(
    "expected",
    [
        [{'address': 'calle 95 # 78 - 49', 'city': 'bogota', 'price': 120000000, 'description': 'hermoso acabado, listo para estrenar', 'year': 2020, 'status': 'pre_venta'},
        {'address': 'calle 95 # 78 - 123', 'city': 'bogota', 'price': 120000000, 'description': 'hermoso acabado, listo para estrenar', 'year': 2020, 'status': 'pre_venta'},
        {'address': 'diagonal 23 #28-21e', 'city': 'bogota', 'price': 270000000, 'description': 'Apartamento con hermosas vistas', 'year': 2018, 'status': 'en_venta'}]
    ]
)
def test_filtering_properties(json_config,expected):
    assert type(consulting.ConsultingProperties(json_config)) is list
    assert consulting.ConsultingProperties(json_config) == expected