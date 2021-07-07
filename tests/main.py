#!/usr/bin/env python3
import sys
sys.path.append('..')
from utils.convert import numparse

if __name__ == '__main__':
    numparse('1+2*4+8/16+32-64-128*256/512')
