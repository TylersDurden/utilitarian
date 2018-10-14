import sys, os

Commands = {'smb':'nmap -p 445 --script smb-os-discovery 192.168.1.0/24',
            'nosy':'nmap -T5 ',
            'snmp': 'nmap -sU -p161 --script snmp-brute'\
            ' --script-args snmplist=community.lst 192.168.1.0/24',
            'who':'iwlist wlan0 scan | grep "Cell" && '
                  'iwlist wlan0 scan | grep "ESSID"'}


def usage():
    print "Incorrect Usage!"


def main():
    if len(sys.argv) < 2:
        usage()
    else:
        if sys.argv[1] == '-whosnx':
            os.system(Commands['who'])
        if sys.argv[1] == '-finger':
            os.system(sys.argv[2])
            os.system(Commands['nosy']+' '+sys.argv[2])
        if sys.argv[1] == '-snmp':
            os.system(Commands['snmp'])
        if sys.argv[1] == '-smb':
            os.system(Commands['smb'])


if __name__ == '__main__':
    main()
