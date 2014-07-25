import glob
import os
for f in glob.glob("LPI*.s"):
	os.system("cat "+f+" >> aperture_absorptions.dat")
