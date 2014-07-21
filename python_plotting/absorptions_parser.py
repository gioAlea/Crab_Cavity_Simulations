import os
import re

class Solver:

    def __init__(self, inname=None):
        self.inname = "all_absorptions.dat"
        self.outname = "all_absorptions.csv"

    def run(self):
        with open(self.inname, "r") as infile:
            self.clean_input(infile)
            for line in infile:
                columns = line.strip().split()
                del columns[0]
                self.write_line(columns)

    def write_line(self, columns):
        with open(self.outname, "a") as outfile:
            outfile.write(",".join(columns)+"\n")

    def clean_input(self, infile):
        for line in infile:
            if line[0] == "#":
                break

if __name__ == "__main__":
    Solver().run()

# tn		=	[]
# sn		=	[]
# for	line in	open("all_absorptions.dat"):
# 		values	=	line.strip("\n").split(' ',1)
# 		tn.append(values[1])

# bn		=	[]
# for line in tn:
# 	b 		=	line.strip().split()
# 	bn.append(",".join(b)+"\n")
# 	bnn		=	sorted(bn, key=lambda tup: tup[0])
