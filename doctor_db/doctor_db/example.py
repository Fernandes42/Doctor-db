from django.db import models
from django.contrib.postgres.fields import JSONField

class text_data(models.Model):
    id = models.AutoField(primary_key=True)
    user_id = models.PositiveSmallIntegerField()
    paragraph = models.PositiveSmallIntegerField()
    summary = models.TextField()
    keywords = models.TextField()
    entity = JSONField()


def insert_text_data(user_id, data):
    for x in data.keys():
        connection = psycopg2.connect('dbname=easy_notes_db')
        mark = connection.cursor()
        statement = """INSERT INTO application_text_data (
            user_id,
            paragraph,
            summary,
            keywords,
            entity
        ) VALUES (%s, %s, %s, %s, %s);"""
        mark = connection.cursor()
        mark.execute(statement,(user_id, x, str(data[x][0]), stringify_list(data[x][1]), json.dumps(data[x][2])))
        mark.close()
        connection.commit()

def retrieve_text_data(user_id):
    connection = psycopg2.connect('dbname=easy_notes_db')
    mark = connection.cursor()
    statement = 'SELECT paragraph, summary, keywords, entity  FROM application_text_data WHERE user_id=%s' % user_id
    mark.execute(statement)
    transcript_data = mark.fetchall()

    results_dict = {}

    for x in transcript_data:
        results_dict[x[0]] = [x[1].split(' '),listify_string(x[2]),x[3]]
    return results_dict
