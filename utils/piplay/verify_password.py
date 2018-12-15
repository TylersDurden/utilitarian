import os, sys, crypt


def swap(fname, destroy):
    data = []
    for line in open(fname, 'r').readlines():
        data.append(line.replace('\n',''))
    if destroy:
        os.remove(fname)
    return data


algos = {'$1$':'md5',
         '$2a$':'Blowfish',
         '$2y$':'8bit-Blowfish',
         '$5$':'sha256',
         '$6':'sha512'}
         
os.system('cat /media/root/8294bf0f-20f9-49ad-82d5-6894ce4def75/etc/shadow >> pass.txt')
password_data = swap('pass.txt',True)      
for line in password_data:
    try:
        user = line.split(':')
        #print user[0]+'='+user[1]
        if user[1] == '*':
            print user[0].replace('\n','') + ' has no password'
        else:
            print user[0] + ' has password with hash:\n' + user[1]
            print '====================================================================================='
    except IndexError:
            pass
print crypt.crypt(sys.argv[1],'$6$')
print "Does it match?"   
