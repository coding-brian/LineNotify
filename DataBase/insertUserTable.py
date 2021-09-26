import psycopg2

def insertUserFromUserID():
  
  DATABASE_URL=''

  conn = psycopg2.connect(DATABASE_URL, sslmode='require')

  cursor = conn.cursor()

  SQL="INSERT INTO lineuser (AccessToken) VALUES ('temp') RETURNING userId"
  
  cursor.execute(SQL)
  conn.commit()

  result=cursor.fetchone()[0]

  cursor.close()
  conn.close()

  return result