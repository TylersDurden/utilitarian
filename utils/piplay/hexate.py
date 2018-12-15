import sys


def usage():
    print 'Incorrect Usage!'
    print ':~# python hexate.py <payload>'
    
 
def hexate(cmd):
    payload = {'slash':[],
               'hex':[]}
    for letter in list(cmd):
        payload['slash'].append('\\x'+letter.encode('hex'))
        payload['hex'].append(letter.encode('hex'))
    return payload    
   
def arr2str(strngarr):
    s = ''
    for i in strngarr:
        s+= i + ' '
    return s
    

def main():
    if len(sys.argv)<2:
        usage()
    else:
        sys.argv.pop(0)
        cmd = arr2str(sys.argv)
        payload = hexate(cmd)
        print '0x'+arr2str(payload['hex']).replace(' ',"") +\
        "\t["+arr2str(payload['slash']).replace(' ',"")+"]"
if __name__ == '__main__':
    main()
#EOF
