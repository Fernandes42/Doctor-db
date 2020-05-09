import psycopg2
import urllib.parse as urlparse
import os

DATABASE_URL = os.environ['DATABASE_URL']


def insert_into_db(data):
    connection = psycopg2.connect(DATABASE_URL, sslmode='require')
    mark = connection.cursor()
    statement = """INSERT INTO applications_covid_tb (
        age,
        sex,
        race,
        country,
        hospital,
        covid_strain,
        pre_exisiting,
        hospitalised,
        respirator_required,
        medicine_applied,
        current_status
        ) VALUES (%s, %s, %s, %s, %s,%s, %s, %s, %s, %s, %s);"""
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


def retrieve_from_db():
    connection = psycopg2.connect(DATABASE_URL, sslmode='require')
    mark = connection.cursor()
    statement = """SELECT * FROM applications_covid_tb ;"""
    print(statement)

    mark.execute(statement)
    status = mark.fetchall()
    mark.close()
    connection.commit()
    print(status)
