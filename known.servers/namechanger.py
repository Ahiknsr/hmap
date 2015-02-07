import os

files1 = os.listdir('.')

files = []
for file in files1:
    if file[-2:]!='py':
        files.append(file)
    else:
        #print file
        'as'

for file in files:
    if ' ' in file:
        name = file.split(' ')[0]
        print name

"""
for file1 in files:
    f = open(file1,'r')
    con = f.readlines()
    f.close()
    for line in con:
        if 'SERVER_NAME' in line:
            break
    try :
        name = line.split(':')[1].split("'")[1]
        name = name.replace('/','.')
        print name
        #print name
        os.rename(file1,name)
        print 'asdf'
        try:
            #os.rename(file,name)
            ba = 'as'+'awer'
        except:
            print file
            print name
    except:
        pass
"""
