#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 解析车站代码文件，输出Python可直接载入的文件


import os
import pickle

ORIGIN_PATH = "../车站代码.txt"
PARSED_PATH = "../station_code.dat"

def main():
    code_dict = {}
    with open(ORIGIN_PATH, "r") as content:
        for line in content:
            parts = line.split("----")
            code_dict[parts[0]] = parts[1][:-1]

    with open(PARSED_PATH, "wb") as container:
        pickle.dump(code_dict, container)


if __name__ == '__main__':
    if not os.access(PARSED_PATH, os.R_OK):
        main()
        exit()
    
    code_dict = {}
    with open(PARSED_PATH, "r") as content:
        code_dict = pickle.load(content)

    print code_dict["深圳"]



