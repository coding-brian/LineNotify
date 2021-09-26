import psycopg2

DATABASE_URL=''

conn = psycopg2.connect(DATABASE_URL, sslmode='require')

cursor = conn.cursor()

SQL='CREATE TABLE lineuser ( userID serial PRIMARY KEY, AccessToken varchar(200) );'

cursor.execute(SQL)
conn.commit()

cursor.close()
conn.close()