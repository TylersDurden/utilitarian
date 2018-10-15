import sys, os, time


def swap(fname):
    data = []
    for line in open(fname, 'r'):
        data.append(line.replace('\n', ''))
    return data


def choose_dictionary():
    os.system('p=$PWD;cd /; find -name *dictionary >> dicts.txt; mv dicts.txt $p;')
    os.system('cat dicts.txt')
    dictionaries = swap('dicts.txt')
    os.system('rm dicts.txt')
    return dictionaries


def default_wordlist():
    os.system('cp /etc/dictionaries-common/words $PWD')
    return swap('words')


def choose_wordbank():
    if os.name != 'posix':
        dictionaries = choose_dictionary()
        # get the words from the dictionary.
        # make the commands windows friendly
        return dictionaries
    else:
        words = default_wordlist()
        print str(len(words)) + " words found"
        return words


def search_wordbank(query):
    os.system('cat words | grep "'+query+'" > wordsearch.txt')
    words = swap('wordsearch.txt')
    if query.lower() in list(words):
        print "Found "+query
    if len(list(words)) > 1:
        printout = ''
        for word in words:
            if word != query:
                printout += ', '+word
        print "Also found" + printout


def main():
    if sys.argv[1] == '-search':
        search_wordbank(sys.argv[2])


if __name__ == '__main__':
    main()
