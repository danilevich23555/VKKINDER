import psycopg2
from pathlib import Path
import os

from create_db_table import display_full_name


temp_param = []
path = os.path.join(Path(__file__).parents[1], 'connection_db')
with open(f"{path}\\connection_db.txt", 'r') as param:
  for string in param:
    if string.strip() == '':
      display_full_name()
    else:
      temp_param.append(string.strip())
      print(string.strip())




database = temp_param[0]
user = temp_param[1]
password = temp_param[2]
host = temp_param[3]
port = temp_param[4]

print(host)


def write_db(id_user,id_user_find,url_profile,url_foto_1,url_foto_2,url_foto_3):
  con = psycopg2.connect(
    database= database,
    user= user,
    password=password,
    host=host,
    port=port
  )
  cur = con.cursor()
  print("Database opened successfully")
  postgres_insert_query = """INSERT INTO vkkinder (id_user,id_user_find,url_profile,url_foto_1,url_foto_2,url_foto_3) 
  VALUES (%s,%s,%s,%s,%s,%s);"""
  record_to_insert = (id_user, id_user_find, url_profile, url_foto_1, url_foto_2, url_foto_3)
  cur.execute(postgres_insert_query, record_to_insert)
  con.commit()

def select_count_id(id_user):
  temp1 = []
  con = psycopg2.connect(
    database=database,
    user=user,
    password=password,
    host=host,
    port=port
  )
  cur = con.cursor()
  postgreSQL_select_Query = "select id_user, count(*) from vkkinder where id_user = %s group by id_user;"
  cur.execute(postgreSQL_select_Query, (id_user,))
  records = cur.fetchall()
  temp1.append(records)
  postgreSQL_select_Query = "select distinct id_user_find from vkkinder where id_user = %s;"
  cur.execute(postgreSQL_select_Query, (id_user,))
  records_id_count = cur.fetchall()
  if records_id_count == []:
    pass
  else:
    for i in range(len(records_id_count)):
      temp1.append((records_id_count[i][0]))
  return temp1