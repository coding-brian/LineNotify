from flask import Flask,request
from DataBase import insertUserTable,updateUser
import urllib
import json
app = Flask(__name__)

@app.route("/notify/register")
def lineNotifyAutorize():
  lineauthorizeurl='https: //notify-bot.line.me/oauth/authorize'

  userid=insertUserTable.insertUserFromUserID()

  query={
    "response_type":"code",
    "client_id":"	KBKGkMPGxTXVFylQaGuWKl",
    "redirect_uri":"https://line-notify-appliaction.herokuapp.com/notify/code",
    "scope":"notify",
    "state":userid
  }

  querysting=urllib.parse.urlencode(query)

  return lineauthorizeurl+'?'+querysting

@app.route("/notify/code",methods=['Get'])
def notify_callback():
  error=request.args.get('error')
  state=request.args.get('state')

  if (error is None):
    code=request.args.get('code')
    accessTokenUrl='https://notify-bot.line.me/oauth/token'

    headers={"Content-Type":"application/x-www-form-urlencoded"}

    body={
      "grant_type":"authorization_code",
      "code":code,
      "redirect_uri":"https://line-notify-appliaction.herokuapp.com/notify/code",
      "client_id":"	KBKGkMPGxTXVFylQaGuWKl",
      "client_secret":"fVgKxRnmByDL2JKZRVGBhTpZ4oGu8EjttyOiQ0Iv4pl"
    }

    data = urllib.parse.urlencode(body).encode()
    req = urllib.request.Request(accessTokenUrl, data=data, headers=headers)
    response = urllib.request.urlopen(req).read()

    result=json.loads(response.decode('utf-8'))

    accessToken=result["access_token"]

    if(accessToken):
      result=updateUser.updateUser(state,accessToken)

    return result
  else:
    errodescription=request.args.get('error_description')

    return 'state: '+state+' ,'+'error:'+error+' ,errodescription: '+errodescription


if(__name__=='__main__'):
  app.run()