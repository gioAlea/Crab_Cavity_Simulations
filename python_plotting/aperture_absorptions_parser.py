import os
import re

class Solver:

    def __init__(self, inname=None):
        self.inname = "aperture_absorptions.dat"
        self.outname = "aperture_absorptions.csv"

    def run(self):
        with open(self.inname, "r") as infile:
            regex =re.compile(r'#')
            for line in infile:
                columns = line.strip().split()
                del columns[0]
                if regex.match(line) is None:
                    self.write_line(columns)

    def write_line(self, columns):
        with open(self.outname, "a") as outfile:
            outfile.write(",".join(columns)+"\n")

if __name__ == "__main__":
    Solver().run()
