import glob
import os
for f in glob.glob("all_absorptions*.dat"):
	os.system("cat "+f+" >> all_absorptions.dat")
