#! /usr/bin/env python3

import PIL as p
import numpy as np
import argparse
import sys
from enum import Enum

class Algorithm:
    def __init__(self, type):
        self.selector = {
            AlgorithmType.k_means: self._k_means
        }
        

        
    def getType(self):
        return self._type


    def select(self):
        try:
            self._type = AlgorithmType(type)
        except ValueError as e:
            raise


class AlgorithmType(Enum):
    k_means = "k_means"

def set_args():
    parser = argparse.ArgumentParser(prog="temagen")
    parser.add_argument('image', help="image_path", type=str)
    parser.add_argument('-n', help="the number of the theme", dest="number", type=int, default=16)
    parser.add_argument('-p', '--picture', help="output a image", dest="image", type=str)
    parser.add_argument('-l', '--less', help="wild color mode", dest="number", action="store_const", const=8)
    parser.add_argument('-a', '--algorithm', help="")
    return parser.parse_args()



def k_means():
    pass
  
if __name__ == "__main__":
    args = set_args()
    print(args)
    Algorithm("")

