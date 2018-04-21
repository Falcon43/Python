import sys

for arg in sys.argv[1:]:
    try:
        f = open(arg,'r')
    except IOError:
        print("Cannot open %s" %arg)
    else:   # optional else clause in try except statements, must follow all except clauses, must be exe if try clause does not raise exception
        print("%s  has %3d lines" % (arg,len(f.readlines())))
        f.close()