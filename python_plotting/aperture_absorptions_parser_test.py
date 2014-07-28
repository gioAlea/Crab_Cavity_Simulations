import os
import re

with open('aperture_absorptions.dat', 'r') as infile:
    with open('aperture_absorptions.csv', 'w') as outfile:
        regex =re.compile(r'#')
        for line in infile:
            columns = line.strip().split()
            del columns[0]
            if regex.match(line) is None:
                outfile.write(",".join(columns)+"\n")

