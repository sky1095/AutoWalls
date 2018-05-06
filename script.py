import urllib
from urllib.request import urlopen
import subprocess
import json
import win32api, win32con, win32gui

##################################Fetching the Images from API#####################################################
#query = input() #For User Defined Search
api_key = 'Your Unsplash API here'
url = 'https://api.unsplash.com/photos/random?orientation=landscape&w=1920&h=1080&client_id=' + api_key
f = urllib.request.urlopen(url)
json_string = f.read()
f.close()
parsed_json = json.loads(json_string)
pic = parsed_json['urls']['full']
urllib.request.urlretrieve(pic, "C://YourFolder//pic.jpeg")
###################################################################################################################

def setWallpaper(path):
    key = win32api.RegOpenKeyEx(win32con.HKEY_CURRENT_USER,"Control Panel\\Desktop",0,win32con.KEY_SET_VALUE)
    win32gui.SystemParametersInfo(win32con.SPI_SETDESKWALLPAPER, path, 1+2)
 
if __name__ == "__main__":
    path = r'C:\YourFolder\pic.jpeg'
    setWallpaper(path)
