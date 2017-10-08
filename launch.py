#!/usr/bin/env python
import sys
from src import Persitency,logger



if __name__ == "__main__":
    daemon = Persitency('/tmp/daemon-example.pid', logger=logger)
    if len(sys.argv) == 2:
        if 'start' == sys.argv[1]:
            daemon.start()
        elif 'stop' == sys.argv[1]:
            daemon.stop()
        elif 'restart' == sys.argv[1]:
            daemon.restart()
        elif 'status' == sys.argv[1]:
            daemon.status()
        else:
            print "Unknown command"
            sys.exit(2)
        sys.exit(0)
    else:
        print "usage: %s start|status|stop|restart" % sys.argv[0]
        sys.exit(2)
