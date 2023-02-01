# -*- coding: UTF-8 -*-
# Time: 2023/2/1 13:21
# Author: Forsaken996
# @file: test.py
# @software: PyCharm
import torch
if __name__ == '__main__':
    print("Hello World")
    device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
    print(torch.device)
    print(device)