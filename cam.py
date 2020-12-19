from picamera import PiCamera
from time import sleep
from datetime import datetime
import configparser
config = configparser.ConfigParser()
config.read('config.ini')


import os
now = str(datetime.now().strftime("%m%d%Y%H%M%S"))
#now = 'abc'
camera = PiCamera()
camera.resolution = (2592, 1944)
camera.start_preview()
sleep(5)


local_path ='/home/pi/Desktop/'+now+'.jpg'

camera.capture(local_path)
camera.stop_preview()

#import zipfile
#zipfile.ZipFile('/home/pi/Desktop/'+now+'.zip', mode='w').write('/home/pi/Desktop/'+now+'.jpg')


from PIL import Image
from smb.SMBConnection import SMBConnection
host=config['NAS']['IP']  #ip or domain name
username=config['NAS']['User']
password=config['NAS']['pwd']
conn=SMBConnection(username,password,"","",use_ntlm_v2 = True)
result = conn.connect(host)
print("login successful")

#f = open(local_path, 'rb')
#localFile =  Image.open(f)

localFile=open('/home/pi/Desktop/'+now+'.jpg',"rb")
# Open local files, note that if a binary file, such as zip package, need to add the parameter b, that is binary mode, the default mode is t, that is, text text mode.
#sleep(5)
conn.storeFile("Joan Privat","/grow/"+now+'.jpg',localFile)
# Smb upload files to the server, the default 30-second timeout, you can modify: timeout = xx. Storage path is a relative path of the shared folder.
#sleep(5)
localFile.close()
#shut down
