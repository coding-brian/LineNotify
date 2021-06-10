import urllib
import json

def SendMessage(message,accessToken):
  notifyurl='https://notify-api.line.me/api/notify'
  headers={
    "Content-Type":"application/x-www-form-urlencoded",
    "Authorization": "Bearer "+ accessToken
    }

  body={"message":message}

  data = urllib.parse.urlencode(body).encode()
  req = urllib.request.Request(notifyurl, data=data, headers=headers)
  try:
    httpresponse = urllib.request.urlopen(req)
    if(httpresponse.status==200):
      response=httpresponse.read()
      responsedata=json.loads(response.decode('utf-8'))
      return responsedata
    else:
      responsedata={"error":"Some error"}
      return responsedata    
  except urllib.error.URLError as e:
    responsedata={"error":e,"description":e.reason} 
    return responsedata

