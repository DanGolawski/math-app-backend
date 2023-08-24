development_db_url = 'postgres://mathmasters:2NdXFwI7icbLaAVIojPy4CAjEJdOEQmt@dpg-cgi42st269v5faa61dtg-a.frankfurt-postgres.render.com/mathapp'
production_db_url = 'postgres://mathmasters:2NdXFwI7icbLaAVIojPy4CAjEJdOEQmt@dpg-cgi42st269v5faa61dtg-a/mathapp'

LOCAL_DATABASE = {
    'host': 'localhost',
    'port': '5432',
    'database': 'mathapp',
    'user': 'postgres',
    'password':'12345'
}

PRODUCTION_DATABASE_EXTERNAL = {
    'host': '5.185.197.13',
    'port': '5432',
    'database': 'mathapp',
    'user': 'postgres',
    'password':'Zarabiac20TysiecyMiesiecznie()'
}

PRODUCTION_DATABASE_INTERNAL = {
    'host': 'localhost',
    'database': 'mathapp',
    'user': 'postgres',
    'password':'Zarabiac20TysiecyMiesiecznie()'
}

EMAIL_DATA = {
    'email': 'mathmasters.contact@gmail.com',
    'password': 'eubmxofncoaklwyw'
}

DATABASE = LOCAL_DATABASE