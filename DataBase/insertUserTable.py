import psycopg2

def insertUserFromUserID():
  
  DATABASE_URL='postgres://ggohhcqkmvboto:01223202afc59e3f2a1f3dfc58e909a4fc4925e61ddb672993442a37bd395261@ec2-54-224-194-214.compute-1.amazonaws.com:5432/debntciff5iimr'

  conn = psycopg2.connect(DATABASE_URL, sslmode='require')

  cursor = conn.cursor()

  SQL="INSERT INTO lineuser (AccessToken) VALUES ('temp')"

  result=cursor.execute(SQL)
  conn.commit()

  cursor.close()
  conn.close()

  return result