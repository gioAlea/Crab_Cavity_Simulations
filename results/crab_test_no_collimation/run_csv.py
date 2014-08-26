import sys
sys.path.append("../../python_modules/")

from data_treatment_module import *
# from plot_csv_module import *
from plot_single_csv_module import *
# from plot_distributions_module import *


# TO PLOT NORMAL AND FAILURE
#--------------------------------------------------------------
# # 1 SIGMA BUNCHLENGTH
# convert_to_csv('normal/BPM1', 'normal.csv')

# # FAILURE, 1 SIGMA
# convert_to_csv('failure/BPM1', 'failure.csv')

# # PLOT THE DATA
# plot_csv(r'normal.csv', r'failure.csv')
#--------------------------------------------------------------


#TO COMPARE DIFFERENT EFFECTS IN THE CRABS
#--------------------------------------------------------------
# 1 SIGMA BUNCHLENGTH
# convert_to_csv('1s/BPM1', '1s.csv')

# # 3 SIGMA BUNCHLENGTH
# convert_to_csv('3s/BPM1', '3s.csv')

# # WITHOUT CRABS
# convert_to_csv('no_crabs/BPM1', 'no_crabs.csv')

# # PLOT THE DATA
# plot_csv(r'1s.csv', r'3s.csv', r'no_crabs.csv')
#--------------------------------------------------------------

# # PLOT THE DATA, SINGLE PLOT
plot_single_csv(r'1s.csv', r'3s.csv', r'no_crabs.csv')
#--------------------------------------------------------------

# TO SEE A 3D DISTRIBUTION
#--------------------------------------------------------------

# plot_distributions(r'3s.csv', r'no_crabs.csv')