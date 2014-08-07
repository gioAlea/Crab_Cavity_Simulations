import sys
sys.path.append("../../../private/simulations/python_modules/")

from data_treatment_module import *
from plot_distributions_module import *

#TREAT THE INITIAL DISTRIBUTION
concatenate1('../result/lowb.coll/dist0*.dat')
convert_to_csv('out1.dat', 'dist0.csv')

#TREAT THE FINAL DISTRIBUTION
concatenate2('../result/lowb.coll/distn*.dat')
convert_to_csv('out2.dat', 'distn.csv')

#PLOT THEM TOGETHER
plot_distributions(r'dist0.csv', r'distn.csv')
