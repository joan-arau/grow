# from smb.SMBConnection import SMBConnection
from time import sleep

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
import pyminizip as zip
import zipfile
from distutils.dir_util import copy_tree
import os
def get_temp():
    todirectory = '/Users/joan/PycharmProjects/grow/temp/'


    try:
        fromdirectory = '/Volumes/Samsung Portable SSD T5/SSD SynDrive/Joan/grow'



        copy_tree(fromdirectory,todirectory)

    except:

        try:
            fromdirectory = '/Volumes/Joan Privat/grow/'



            copy_tree(fromdirectory,todirectory)

        except:
            try:
                fromdirectory = '/Volumes/schweizer-zinnfiguren.synology.me/Joan Privat/grow/'



                copy_tree(fromdirectory, todirectory)
            except:
                fromdirectory = '/Volumes/wszinn.dyndns.org/Joan Privat/grow'

                copy_tree(fromdirectory, todirectory)


    for i in os.listdir('/Users/joan/PycharmProjects/grow/temp'):
        # print(i)
        if i[0] == '.':
            os.remove('/Users/joan/PycharmProjects/grow/temp/'+i)

        if i.endswith('.zip') == True:
            print(i[:-4])
            if os.path.isfile('/Users/joan/PycharmProjects/grow/temp/'+i[:-4]+'.jpg') == False:
                with zipfile.ZipFile('/Users/joan/PycharmProjects/grow/temp/'+i) as file:
                    # password you pass must be in the bytes you converted 'str' into 'bytes'
                    file.extract(member =i[:-4]+'.jpg', pwd=bytes('growpic', 'utf-8'),path='/Users/joan/PycharmProjects/grow/temp/')
                # zip.uncompress('/Users/joan/PycharmProjects/grow/temp/'+i, "growpic", '/Users/joan/Desktop/test'+i[:-4]+'.jpg',1)
            os.remove('/Users/joan/PycharmProjects/grow/temp/'+i)




if __name__ == "__main__":
    get_temp()