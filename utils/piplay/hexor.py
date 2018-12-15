import os, sys


def swap(fname, destroy):
    data = []
    for line in open(fname,'r').readlines():
        data.append(line.replace('\n',''))
    if destroy:
        os.remove(fname)
    return data


def commander(commands):
    os.system(commands+'>> command.txt')
    data = swap('command.txt',True)
    return data


def build_command(args):
    cmd = ""
    for element in args:
        cmd += element + " "
    return cmd


def main():
    if len(sys.argv) > 1:
        sys.argv.pop(0)
        if sys.argv[0] == '-CMD':
            sys.argv.pop(0)
            result = commander(build_command(sys.argv))
            for line in result:
                print line


if __name__ == '__main__':
    main()

