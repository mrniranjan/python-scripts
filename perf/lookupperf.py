#!/usr/bin/env python
from __future__ import print_function
import os
import subprocess
import argparse
import shlex
import errno
import sys

class LookupPerf(object):
    def __init__(self, maxlookup, datadir):
        self.lookup_max = maxlookup
        self.perf_data_dir = datadir
        self.mem_cache_data_dir = '%s/memory_cache' % (self.perf_data_dir)
        self.ldb_cache_dir = '%s/ldb_cache' % (self.perf_data_dir)
        self.getent_group_results = '%s/getent_group_results.txt' % (self.perf_data_dir)
        self.memcache_full_info = '%s/memcache_full_info.txt' % (self.mem_cache_data_dir)

    def prepare(self):
        """ Create directory structure """
        dirs = [self.perf_data_dir, self.mem_cache_data_dir, self.ldb_cache_dir]
        for directory in dirs:
            try:
                os.makedirs(directory)
            except OSError as e:
                if e.errno != errno.EEXIST:
                    raise

    def find_nss(self, tracefile, groupname):
        """ Find if nss socket in trace file """
        f = open(tracefile, 'r')
        lines = f.read()
        nss = lines.find('/var/lib/sss/pipes/nss')
        if nss != -1:
            move_trace_file = "mv -f %s %s" % (tracefile, self.ldb_cache_dir)
            self.execute(shlex.split(move_trace_file))
	    # copy /var/lib/sss/mc 
	    cp_mc = "cp -a /var/lib/sss/mc %s" % (self.perf_data_dir)
	    self.execute(shlex.split(cp_mc))
	    print("%s was looked through nss socket" % groupname)
            return True
        else:
            return False

    def run(self):
        """ Run performance loop """
	i = 0
	j = 0
        for i in range(1, int(self.lookup_max)):
            print("--------------loop %d---------------" % (i))
            idmgroup = 'idmgroup%d' % i
            getent_cmd = 'getent group %s' % (idmgroup)
            _, _, rc = self.execute(shlex.split(getent_cmd))
            print("i = %d, %s" % (i, idmgroup))
            for j in range(1, min(10, i)):
                idmgroup = 'idmgroup%d' % j
                print("j = %d, %s" % (j, idmgroup))
                strace_file = '%s/%s.trace' % (self.mem_cache_data_dir, idmgroup)
                strace_cmd = 'strace -fxvto %s getent group %s' % (strace_file, idmgroup)
                _, _, rc = self.execute(shlex.split(strace_cmd))
                if self.find_nss(strace_file, idmgroup):
		    print("Total groups stored in memcach is %d" % i)
                    sys.exit(1)
            k1 = int(i / 5)
            k2 = int((2 * i) / 5)
            k3 = int((3 * i) / 5)
            k4 = int((4 * i) / 5)
	    if i > 10:
	            my_list = [k1, k2, k3, k4]
        	    for k in my_list:
	                idmgroup = 'idmgroup%d' % k
                        print("k = %d, %s" % (k, idmgroup))
        	        strace_file = '%s/%s.trace' % (self.mem_cache_data_dir, idmgroup)
                	strace_cmd = 'strace -fxvto %s getent group %s' % (strace_file, idmgroup)
	                _, _, rc = self.execute(shlex.split(strace_cmd))
        	        if self.find_nss(strace_file, idmgroup):
		           print("Total groups stored in memcach is %d" % i)
                	   sys.exit(1)
	            a1 = max(i - 10, 0)
        	    a2 = i
	            for x in range(a1, a2):
        	        idmgroup = 'idmgroup%d' % x
                        print("x = %d, %s" % (x, idmgroup))
                	strace_file = '%s/%s.trace' % (self.mem_cache_data_dir, idmgroup)
	                strace_cmd = 'strace -fxvto %s getent group %s' % (strace_file, idmgroup)
        	        _, _, _ = self.execute(shlex.split(strace_cmd))
                	if self.find_nss(strace_file, idmgroup):
			    print("Total groups stored in memcach is %d" % i)
	                    sys.exit(1)

    def execute(self, args, stdin=None, capture_output=True,
                raiseonerr=False, env=None, cwd=None):
        """ Execute command """
        p_in = None
        p_out = None
        p_err = None
        if env is None:
            env = os.environ.copy()
        if capture_output:
            p_out = subprocess.PIPE
            p_err = subprocess.PIPE
        try:
            proc = subprocess.Popen(args, stdin=p_in, stdout=p_out,
                                    stderr=p_err, close_fds=True,
                                    env=env, cwd=cwd)
            stdout, stderr = proc.communicate(stdin)
        except KeyboardInterrupt:
            proc.wait()
            raise
        if proc.returncode != 0 and raiseonerr:
            raise subprocess.CalledProcessError(proc.returcode, args, stdout)
        else:
            return (stdout, stderr, proc.returncode)


def main():
    parser = argparse.ArgumentParser("Description=Mem Cache Performance")
    required = parser.add_argument_group('Mandatory Arguments')
    parser.add_argument('--datadir', type=str, help="Pass Directory path to save performance data")
    parser.add_argument('--maxlookup', type=int, help="Maximum lookup")
    args = parser.parse_args()
    e = LookupPerf(args.maxlookup, args.datadir)
    e.prepare()
    e.run()


if __name__ == '__main__':
    main()
