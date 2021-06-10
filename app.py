from flask import Flask,request
from DataBase import insertUserTable,updateUser,getUserTable
from lineLib import SendtoNotify
from Crawler import pluginversion
import urllib
import json
app = Flask(__name__)

@app.route("/notify/register")
def lineNotifyAutorize():
  lineauthorizeurl='https://notify-bot.line.me/oauth/authorize'

  userid=insertUserTable.insertUserFromUserID()

  query={
    "response_type":"code",
    "client_id":"KBKGkMPGxTXVFylQaGuWKl",
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
      "client_id":"KBKGkMPGxTXVFylQaGuWKl",
      "client_secret":"fVgKxRnmByDL2JKZRVGBhTpZ4oGu8EjttyOiQ0Iv4pl"
    }

    data = urllib.parse.urlencode(body).encode()
    req = urllib.request.Request(accessTokenUrl, data=data, headers=headers)
    response = urllib.request.urlopen(req).read()

    result=json.loads(response.decode('utf-8'))

    accessToken=result["access_token"]

    if(accessToken):
      dataresult=updateUser.updateUser(state,accessToken)
      if (dataresult>0): 
        sendMessagebyaccessToke(accessToken)
        return '連動完成'
      else:
       return '有點問題，請重新使用'

    return '有點問題，請重新使用'
  else:
    errodescription=request.args.get('error_description')

    return 'state: '+state+' ,'+'error:'+error+' ,errodescription: '+errodescription

@app.route("/notify/send",methods=['Get'])
def sendMessage():
  users=getUserTable.selectUser()
  lenght=len(users)

  if(lenght>0):
    messsage=pluginversion.getVersioninfo('https://www.nopcommerceplus.com/discount-on-current-shopping-cart-subtotal')
    for user in users:
      sendresult=SendtoNotify.SendMessage(messsage,user['accesstoken'])

  return 'None'

def sendMessagebyaccessToke(accseeToken):
  messsage=pluginversion.getVersioninfo('https://www.nopcommerceplus.com/discount-on-current-shopping-cart-subtotal')
  sendresult=SendtoNotify.SendMessage(messsage,accseeToken)
  return sendresult

if(__name__=='__main__'):
  app.run()