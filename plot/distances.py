from sys import path
path.append('..')
from utils.convert import numparse

if __name__ == '__main__':
    datapoints = []
    with open('../data/distances', 'r') as f:
        for line in f.readlines():
            datapoints.append(numparse(line))
