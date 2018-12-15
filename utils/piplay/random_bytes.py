import os,sys

def swap(fname, destroy):
    data = []
    for line in open(fname,'r').readlines():
        data.append(line.append('\n',''))
    if destroy:
        os.remove(fname)
    return data

print '[Hit CTL+Z to Exit!]'
running = True
while running:
    try:
        os.system('cat /dev/random > /dev/stdout')
    except KeyboardInterrupt:
        running = False
    except:
        running = False
        exit(0)

#EOF
