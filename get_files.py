# from smb.SMBConnection import SMBConnection
from time import sleep
import configparser

config = configparser.ConfigParser()
config.read('config.ini')
#
#
# conn = SMBConnection(config['NAS']['User'], config['NAS']['pwd'],config['NAS']['name'],config['NAS']['name'])
# conn.connect(config['NAS']['IP'])
# results = conn.listPath('Joan Privat', '/grow')
# print(results)
#
#
# l = []
# for x in results:
#     x = str(x.filename)
#
#     print(x,x[-4:])
#     if x[-4:] == '.jpg':
#         l.append(int(x[:-4]))
#
#
# print(sorted(l))



# from smb.SMBConnection import SMBConnection
# conn = SMBConnection(config['NAS']['User'], config['NAS']['pwd'],config['NAS']['name'],config['NAS']['name'])
# conn.connect(config['NAS']['IP'])
#
# local_path = '/Users/joan/PycharmProjects/grow/temp/abc.jpg'
#
#
# fp= open(local_path, 'wb')
# conn.retrieveFile('Joan Privat','/grow/abc.jpg', fp)
# sleep(5)


from distutils.dir_util import copy_tree

fromdirectory = '/Volumes/Joan Privat/grow/'

todirectory = '/Users/joan/PycharmProjects/grow/temp/'

copy_tree(fromdirectory,todirectory)