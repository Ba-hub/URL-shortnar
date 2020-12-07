import pyshorteners
url = input("Enter Your Valid URL ==>")
s = pyshorteners.Shortener().tinyurl.short(url)
print("Your URL shorted is ==>", s) 
