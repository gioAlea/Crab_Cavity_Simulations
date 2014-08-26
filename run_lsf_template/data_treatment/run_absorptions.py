import sys
import os

sys.path.append("/afs/cern.ch/work/a/ansantam/private/simulations/python_modules/")

from data_treatment_module import *
from plot_absorptions_module import *

#TREAT THE APERTURE FILES
concatenate1('../result/lowb.coll/LPI*.s')
convert_to_csv('out1.dat', 'aperture.csv')

#TREAT THE ABSORPTIONS FILES
concatenate2('../result/lowb.coll/all_absorptions.lowb*.dat')
convert_to_csv('out2.dat', 'collimators.csv')

#ERASE TEMP FILES
os.remove(r'out1.dat')
os.remove(r'out2.dat')

#PLOT THEM TOGETHER
plot_absorptions('collimators.csv', 'aperture.csv')


