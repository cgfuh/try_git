#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# by Mariano
#
import getopt
import sys
from telnetlib import Telnet


def telnet_handler(host, dump, passw, set_name):
    if not host:
        host = '127.0.0.1'
    port = 23
    tftphost = '200.2.127.150'
    tftppath = ''  # e.g: tftppath = 'mdump/'

    # connect
    print "Connecting to %s..." % host
    tn = Telnet(host, port)
    #tn.set_debuglevel(5)

    #print "waiting for login string..."
    tn.read_until("login: ")
    tn.write('admin' + "\n")
    #print "waiting for password string..."
    tn.read_until("password: ")
    tn.write(passw + "\n")

    tn.read_until(set_name + "> ")
    cmd = "dump network %s %s" % (tftphost, tftppath + dump)
    print "running \"%s\" on host %s" % (cmd, host)
    tn.write(cmd + '\n')

    tn.read_until(set_name + "> ")
    tn.write('logout\n')
    print "Logging out from %s..." % host

    print tn.read_all()

    print "Bye."


def usage():
    print '''
    Usage: %s [-h] | [-d <device ip>] [-n <dump name>] [-p <password>] [-s <set_pront>] [-v]
        -h, --help:      display this output
        -d, --device:    host target
        -n, --dump_name: dump name to download
        -p, --password:  password DSLAM
        -s, --set_pront: set_pront del DSLAM
        -v:              be verbose
    ''' % (sys.argv[0])


def parse_args():
    try:
        opts, args = getopt.getopt(sys.argv[1:], "hd:n:p:s:v", ["help", "device=", "dump_name=", "password=", "set_pront="])
    except getopt.GetoptError, err:
        # print help information and exit:
        print str(err)  # will print something like "option -a not recognized"
        usage()
        sys.exit(4)
    device = None
    dump_name = None
    password = None
    set_pront = None
    verbose = False
    for o, a in opts:
        if o == "-v":
            verbose = True
        elif o in ("-h", "--help"):
            usage()
            sys.exit()
        elif o in ("-d", "--device"):
            device = a
        elif o in ("-n", "--dump_name"):
            dump_name = a
        elif o in ("-p", "--password"):
            password = a
        elif o in ("-s", "--set_pront"):
            set_pront = a
        else:
            assert False, "unhandled option"
        # ...
        #print "for: ", o, a

    #print "host: %s" % (device)
    #print "dump name: %s" % (dump_name)
    if device is not None and \
            dump_name is not None and \
            password is not None and \
            set_pront is not None:
        telnet_handler(device, dump_name, password, set_pront)


def main():
    parse_args()

if __name__ == "__main__":
    main()
