import os
import re
import glob

def concatenate(regex):
	for f in glob.glob(regex):
		os.system("cat "+f+" >> out.dat")

def convert_to_csv(inp, outp):
	with open(inp, 'r') as infile:
	    with open(outp, 'w') as outfile:
	        regex =re.compile(r'#')
	        for line in infile:
	            columns = line.strip().split()
	            if regex.match(line) is None:
	                outfile.write(",".join(columns)+"\n")
