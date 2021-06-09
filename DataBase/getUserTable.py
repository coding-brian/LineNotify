import psycopg2

def getUserFromUserID(userid):
  DATABASE_URL='postgres://ggohhcqkmvboto:01223202afc59e3f2a1f3dfc58e909a4fc4925e61ddb672993442a37bd395261@ec2-54-224-194-214.compute-1.amazonaws.com:5432/debntciff5iimr'

  conn = psycopg2.connect(DATABASE_URL, sslmode='require')

  cursor = conn.cursor()

  SQL=f'select userID,AccessToken from lineuser where userID={userid}'

  cursor.execute(SQL)
  conn.commit()

  result=cursor.fetchall()

  cursor.close()
  conn.close()

  return result

def selectUser():
  
  DATABASE_URL='postgres://ggohhcqkmvboto:01223202afc59e3f2a1f3dfc58e909a4fc4925e61ddb672993442a37bd395261@ec2-54-224-194-214.compute-1.amazonaws.com:5432/debntciff5iimr'

  conn = psycopg2.connect(DATABASE_URL, sslmode='require')

  cursor = conn.cursor()

  SQL=f"SELECT userid,accesstoken FROM lineuser"

  cursor.execute(SQL)
  conn.commit()

  result=cursor.fetchall() 
  
  cursor.close()
  conn.close()

  return result
