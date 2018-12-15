import sys, os

def swap(fname, destroy):
    data = []
    for line in open(fname, 'r').readlines():
        data.append(line.replace('\n',''))
    if destroy:
        os.system('rm '+fname)
    return data


def main():
    # List Procs   
    os.system('netstat -l')
    proc = str(input('Enter the name of the process:'))
    # lsof <Proc>
    os.system('lsof '+proc)
    # dumpcore <PID>
    proc_data = swap
    
    
if __name__ == '__main__':
    main()

