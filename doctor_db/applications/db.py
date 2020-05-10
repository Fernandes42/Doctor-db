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


def retrieve_rows_from_db():
    connection = psycopg2.connect(DATABASE_URL, sslmode='require')
    mark = connection.cursor()
    statement = """SELECT * FROM applications_covid_tb ;"""
    mark.execute(statement)
    status = mark.fetchall()
    mark.close()
    connection.commit()
    return [list(elem) for elem in status]

def retrieve_treatment_data_recovered():
    connection = psycopg2.connect(DATABASE_URL, sslmode='require')
    mark = connection.cursor()
    statement = """SELECT medicine_applied FROM applications_covid_tb WHERE current_status='R' ;"""
    mark.execute(statement)
    status = mark.fetchall()
    mark.close()
    connection.commit()
    data = [list(elem) for elem in status]

def retrieve_treatment_data_dead():
    connection = psycopg2.connect(DATABASE_URL, sslmode='require')
    mark = connection.cursor()
    statement = """SELECT medicine_applied FROM applications_covid_tb WHERE current_status='D' ;"""
    mark.execute(statement)
    status = mark.fetchall()
    mark.close()
    connection.commit()
    data = [list(elem) for elem in status]

def retrieve_ages_from_db():
    # Default bounds for now
    bounds = (25, 45, 65)
    age_counts = []
    connection = psycopg2.connect(DATABASE_URL, sslmode='require')
    mark = connection.cursor()

    statement = """SELECT COUNT(*) FROM applications_covid_tb
                    WHERE age < 25;"""
    mark.execute(statement)
    status = mark.fetchall()
    age_counts.append(list(status))

    statement = """SELECT COUNT(*) FROM applications_covid_tb
                        WHERE age > 18 AND age < 45;"""
    mark.execute(statement)
    status = mark.fetchall()
    age_counts.append(list(status))

    statement = """SELECT COUNT(*) FROM applications_covid_tb
                        WHERE age > 45 AND age < 65;"""
    mark.execute(statement)
    status = mark.fetchall()
    age_counts.append(list(status))

    statement = """SELECT COUNT(*) FROM applications_covid_tb
                        WHERE age > 65;"""
    mark.execute(statement)
    status = mark.fetchall()
    age_counts.append(list(status))

    return age_counts
