import sys, getopt
import subprocess
#from subprocess import call
#call(["ls", "-l"])

#cssh -u <username> -c <command> <server1> <server2> <server n>
# apply ssh command to each server
# relies on ssh keys to be in place to logon without password

def main(argv):
    inputfile = ''
    outputfile = ''
    try:
        opts, args = getopt.getopt(argv,"hi:o:",["ifile=","ofile="])
        print('opts:', opts)
        print('args:', args)
    except getopt.GetoptError:
        print 'cssh.py -i <inputfile> -o <outputfile>'
        sys.exit(2)
    for opt, arg in opts:
        print('opt:', opt)
        print('arg:', arg)
        if opt == '-h':
            print 'cssh.py -i <inputfile> -o <outputfile>'
            sys.exit()
        elif opt in ("-i", "--ifile"):
            inputfile = arg
        elif opt in ("-o", "--ofile"):
            outputfile = arg
    print 'Input file is "', inputfile
    print 'Output file is "', outputfile

if __name__ == "__main__":
    print('Full - sys.argv:',sys.argv)
    main(sys.argv[1:])