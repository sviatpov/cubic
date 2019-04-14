import argparse
import numpy as np
import math
import re

def parse_arg():
    parser = argparse.ArgumentParser(prog='my_program')
    parser.add_argument('-steps', type=str, default=False, help="steps for cubic")
    parser.add_argument('-i',"--iter", type=int, default=False, help="mix rubic")
    parser.add_argument('-gui', "--gui", action='store_true', default=False, help="gui")
    args = parser.parse_args()
    if not args.steps and not args.iter:
        print("add steps or mix for rubic")
        exit(1)
    return args

# class   ValidationManager:
#
#     def __init__(self, readBuffer):
#         self.readBuffer = readBuffer
#
#
#     def run(self):
#         self.validationSizeContainer()
#         self.validationLen()
#         self.validationSymbol()
#         self.validationSizeSymbol()
#
#     def     validationLen(self):
#         string = self.readBuffer.split('\n')
#         if (len(string) != 1):
#             errorExit("need one line")
#

def parse_line():
    arg = parse_arg()
    if not arg.steps:
        return math.fabs(arg.iter), arg.gui
    ss = arg.steps
    ss = ss.strip().split()
    for s in ss:
        if len(s) ==0 or len(s) > 2:
            print("wrong string")
            exit(1)
        match = re.search(r'[^FBRLUD2\']', s)
        if match:
            print("wrong string")
            exit(1)
        match = re.search(r'[A-Z]+', s)
        if match == None:
            print("wrong string")
            exit(1)
    return ss, arg.gui

if __name__ == '__main__':
    arg = parse_arg()
    s = arg.steps
    s = s.strip().split()
    print(s)