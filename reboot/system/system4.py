import os
import select

fds =  os.open("data", os.O_RDONLY)

while True:
    reads, _, _ = select.select(fds, [], [], 2.0)
    if 0 < len(reads):
        d = os.read(reads[0], 10)
        if d:
            print "-> ", d
        else:
            break
    else:
        print "timeout"
