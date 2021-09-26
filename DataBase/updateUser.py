import psycopg2

def updateUser(userid,accseetoken):
  
  DATABASE_URL=''

  conn = psycopg2.connect(DATABASE_URL, sslmode='require')

  cursor = conn.cursor()

  SQL=f"update lineuser set accessToken='{accseetoken}' where userid={userid}"
  
  cursor.execute(SQL)
  conn.commit()

  result=cursor.rowcount

  cursor.close()
  conn.close()

  return result