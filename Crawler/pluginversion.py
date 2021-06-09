from Crawler import htmlrequest

def getVersioninfo(url):
  soup=htmlrequest.htmlparse(url)

  description=soup.find(class_="short-description")
  versioninfo=description.find("p").find("br")

  return versioninfo.text