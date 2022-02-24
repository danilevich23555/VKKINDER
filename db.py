import psycopg2

def write_db(id_user,id_user_find,url_profile,url_foto_1,url_foto_2,url_foto_3):
  con = psycopg2.connect(
    database="vkkinder",
    user="test",
    password="12345678",
    host="localhost",
    port="5432"
  )
  cur = con.cursor()
  print("Database opened successfully")
  postgres_insert_query = """INSERT INTO test1 (id_user,id_user_find,url_profile,url_foto_1,url_foto_2,url_foto_3) 
  VALUES (%s,%s,%s,%s,%s,%s);"""
  record_to_insert = (id_user, id_user_find, url_profile, url_foto_1, url_foto_2, url_foto_3)
  cur.execute(postgres_insert_query, record_to_insert)
  con.commit()

def select_count_id(id_user):
  temp = []
  con = psycopg2.connect(
    database="vkkinder",
    user="test",
    password="12345678",
    host="localhost",
    port="5432"
  )
  cur = con.cursor()
  postgreSQL_select_Query = "select id_user, count(*) from test1 where id_user = %s group by id_user;"
  cur.execute(postgreSQL_select_Query, (id_user,))
  records = cur.fetchall()
  temp.append(records)
  postgreSQL_select_Query = "select distinct id_user_find from test1 where id_user = %s;"
  cur.execute(postgreSQL_select_Query, (id_user,))
  records_id_count = cur.fetchall()
  if records_id_count == []:
    pass
  else:
    for i in range(len(records_id_count)):
      temp.append((records_id_count[i][0]))
  return temp