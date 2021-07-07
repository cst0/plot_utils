#!/usr/bin/env python3
import re
from typing import List, Union
from io import UnsupportedOperation

def operate(a, b, op) -> float:
    if op == '*': return a * b
    if op == '/': return a / b
    if op == '+': return a + b
    if op == '-': return a - b
    raise UnsupportedOperation("that wasn't one of [*/+-], so operation failed.")

def numparse(string:str) -> Union[float, List[float]]:
    op_set = '*/+-'
    split_string:List[str] = re.split('(['+op_set+'])', string)
    split = []
    for s in split_string:
        split.append(float(s) if s.replace('.','',1).isdigit() else s)

    for _, operator in enumerate(op_set):
        for index in range(len(split)-1, -1, -1):
            if split[index] == operator:
                val = operate(split[index-1], split[index+1], operator)
                split[index-1] = val
                split.pop(index+1)
                split.pop(index)

    if len(split) == 1:
        return split[0]
    else:
        return 0.

