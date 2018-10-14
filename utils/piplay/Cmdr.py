import os, sys, time


def record_from_mic():
    # Get Audio Hardware device name
    os.system('audio_dev=$(pacmd list-sinks | grep -A1 "* index" | grep -oP "<\K[^ >]+");'
              'echo "Audio Device Found: "$audio_dev')

def create_dictionary():
    try:
        os.system('p=$PWD;cd /; find -name *dictionary >> dicts.txt; '
                  'cp dicts.txt $p; rm dicts.txt')
        dict_files = swap('dicts.txt')
        os.system('mkdir WORDS')
        for file in dict_files:
            os.system('cp -r '+file.replace("'",'').replace('.','')+" WORDS/")
        os.system('ls WORDS/')
    except:
        pass
    return dict_files


def swap(fname):
    data = []
    for line in open(fname, 'r').readlines():
        data.append(line.replace('\n',''))
    os.system('rm ' + fname)
    return data


def usage():
    print "INCORRECT USAGE!"
    print "Usage: python Cmdr.py -mode"
    print "Mode List: "


def nxconx():
    cmd = 'iw dev wlan0 scan dump'
    cmd2 = 'nmap -sU -p161 --script snmp-brute' \
           ' --script-args snmplist=community.lst 192.168.1.0/24'
    smb ='nmap -p 445 --script smb-os-discovery 192.168.1.0/24'
    os.system(cmd+' >> wlanscan.txt')
    wlan_scan = swap('wlanscan.txt')
    os.system(cmd2)
    os.system(smb)


def main():
    if len(sys.argv) < 2:
        usage()
    else:
        if sys.argv[1] == '-dict':
            dictionaries = create_dictionary()
        if sys.argv[1] == '-record':
            record_from_mic()
        if sys.argv[1] == '-nx':
            nxconx()


if __name__ == '__main__':
    main()
