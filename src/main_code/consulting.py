"""
This piece of code help to users to looking for
a new property regarding to specific criteria
"""
from db_code.db import SQLConnection #for test this code
#from src.db_code.db import SQLConnection # for run pytest

def ConsultingProperties(filters):
    sql_obj = SQLConnection()
    resultado = sql_obj.make_query()
    if filters['city'] == [] and filters['year'] == [] and filters['city'] == []:
        return resultado
    if filters['city'] != []:
        resultado = list(filter(lambda d: d['city'] in filters['city'],resultado))
    if filters['year'] != []:
        resultado = list(filter(lambda d: d['year'] in filters['year'],resultado))
    if filters['status'] != []:
        resultado = list(filter(lambda d: d['status'] in filters['status'],resultado))
    return resultado


if __name__ == '__main__':
    filters = {
        'city':['bogota','medellin'],
        'year': [2021,2020,2018],
        'status': ['pre_venta','en_venta']
    }
    print(ConsultingProperties(filters))
