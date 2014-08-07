import sys
sys.path.append("../../private/simulations/python_modules/")

from data_treatment_module import *
from plot_csv_module import *


# 1 SIGMA BUNCHLENGTH
convert_to_csv('BPM11', 'data1.csv')

# FAILURE, 1 SIGMA
convert_to_csv('BPM2', 'data2.csv')

# PLOT THE DATA
plot_csv(r'data1.csv', r'data2.csv')
