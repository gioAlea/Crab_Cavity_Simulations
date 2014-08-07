import sys
sys.path.append("../../../private/simulations/python_modules/")

from data_treatment_module import *
from plot_absorptions_module import *

#TREAT THE APERTURE FILES
concatenate1('../result/lowb.coll/LPI*.s')
convert_to_csv('out1.dat', 'aperture.csv')

#TREAT THE ABSORPTIONS FILES
concatenate2('../result/lowb.coll/all_absorptions.lowb*.dat')
convert_to_csv('out2.dat', 'collimators.csv')

#PLOT THEM TOGETHER
plot_absorptions('collimators.csv', 'aperture.csv')

