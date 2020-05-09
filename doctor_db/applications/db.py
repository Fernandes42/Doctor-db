import psycopg2

def insert_into_db(data):
    connection = psycopg2.connect('dbname=postgresql-transparent-18692')
    mark = connection.cursor()
    statement = """INSERT INTO applications_covid_tb (
        age,
        sex,
        race,
        country,
        hospital,
        covid_strain,
        pre-existing,
        hospitalised,
        respirator_required,
        medicine_applied,
        current_status
        ) VALUES (%s, %s, %s, %s, %s,%s, %s, %s, %s, %s);"""
    mark = connection.cursor()
    mark.execute(statement,(
        data['age'],
        data['sex'],
        data['race'],
        data['country'],
        data['hospital'],
        data['covid_strain'],
        data['pre_exisiting'],
        data['hospitalised'],
        data['respirator_required'],
        data['medicine_applied'],
        data['current_status']
    ))
    mark.close()
    connection.commit()
