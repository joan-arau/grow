from smb.SMBConnection import SMBConnection
from time import sleep
import configparser

config = configparser.ConfigParser()
config.read('config.ini')


conn = SMBConnection(config['NAS']['User'], config['NAS']['pwd'],config['NAS']['name'],config['NAS']['name'])
conn.connect(config['NAS']['IP'])
results = conn.listPath('Joan Privat', '/grow')
print(results)
breakpoint()

l = []
for x in results:
    x = str(x.filename)

    print(x,x[-4:])
    if x[-4:] == '.jpg':
        l.append(int(x[:-4]))


print(sorted(l))


local_path = '/Users/joan/PycharmProjects/grow/temp/abc.jpg'


with open(local_path, 'wb') as fp:
    conn.retrieveFile('Joan Privat','/grow/12162020174839.jpg', fp)
    sleep(5)