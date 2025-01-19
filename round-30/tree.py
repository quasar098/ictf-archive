#!/usr/bin/env python3

import pickle

class WaveletTreeNode:
    def __init__(self, flag):
        self.alphabet = list(set(flag))
        self.length = len(flag)
        left_str = ''
        right_str = ''
        data = ''
        for char in flag:
            if self.alphabet.index(char) < len(self.alphabet)//2:
                data += '0'
                left_str += char
            else:
                data += '1'
                right_str += char
        self.data = int(data[::-1], 2)
        if len(self.alphabet) == 1:
            return
        self.left = WaveletTreeNode(left_str)
        self.right = WaveletTreeNode(right_str)

    def write_to_pickle_file(self, fname):
        with open(fname, 'wb') as handle:
            pickle.dump(self, handle, protocol=pickle.HIGHEST_PROTOCOL)


if __name__ == '__main__':
    flag = open("flag.txt").read().strip()
    tree = WaveletTreeNode(flag)
    tree.write_to_pickle_file("tree.pickle")
