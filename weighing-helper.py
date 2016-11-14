# -*- coding: utf-8 -*-
"""
Created on Mon Nov 14 17:35:57 2016

@author: dotha
"""

import sys
ALLOWABLE_ERROR = 0.01


def comb(index_old, stacklist):
    sumstacklist = sum(stacklist)
    if mass + ALLOWABLE_ERROR <= sumstacklist:
        return False
    elif mass - ALLOWABLE_ERROR < sumstacklist:
        return stacklist
    else:
        for i in range(index_old, len(lines)):
            ret = comb(i+1, stacklist + [lines[i]])
            if ret is not False:
                return ret
        else:
            return False
    
    
def main():
    t = comb(0, [])
    print(t)
    print(mass,sum(t))



if __name__ == "__main__":
    mass = float(sys.argv[1])
    f = open(sys.argv[2], "r")
    lines = sorted(map(float,f.readlines()))
    lines.reverse()
    usedstack = []
    print(lines)
    f.close()
    main()