import os, time


def swapper(fname, destroy):
    data = []
    for line in open(fname,'r').readlines():
        data.append(line.replace('\n',''))
    if destroy:
        os.system('rm '+fname)
    return data


def fastswap(fname, destroy):
    fp = open(fname)
    data = fp.readlines()
    if destroy:
        os.remove(fname)
    return data


s0 = time.time()
data_1 = swapper('example.txt', False)
s1 = time.time()
data_2 = fastswap('example.txt', False)
s2 = time.time()

print "Old Technique Reads "+str(len(data_1))+" lines in "+str(s1-s0)+"s [Linux Only]"
print "New Technique Reads "+str(len(data_2))+" lines in "+str(s2-s1)+"s [Cross-Platform also]"
