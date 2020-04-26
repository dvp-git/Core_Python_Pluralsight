import argparse

# Creates a ArgumentParser
parser = argparse.ArgumentParser(description="Process some integers")

# Filling with arguments. the method takes string from command line and tells how to use them as objects
parser.add_argument('integers',metavar='N',type=float,nargs='+',help='an integer for accumulator')

parser.add_argument('--sum', dest='accumulate',action='store_const',\
                    const=sum,default=max,\
                    help='sum the integers (default: find the max)')
args = parser.parse_args()

print(args.accumulate(args.integers))

"""Outputs:
C:\Darryl_Files\Learnings_Trainings\PluralSight_Courses\Python_Learning_Path\Core_Python>python argparseExample.py --help
usage: argparseExample.py [-h] [--sum] N [N ...]

Process some integers

positional arguments:
  N           an integer for accumulator

optional arguments:
  -h, --help  show this help message and exit
  --sum       sum the integers (default: find the max)

C:\Darryl_Files\Learnings_Trainings\PluralSight_Courses\Python_Learning_Path\Core_Python>python argparseExample.py --sum 4 5
9.0
"""
