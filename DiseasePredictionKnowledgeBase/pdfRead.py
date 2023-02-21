# -*- coding: UTF-8 -*-
# Time: 2023/2/1 15:19
# Author: Forsaken996
# @file: pdfRead.py
# @software: PyCharm

import pdfplumber


def read_pdf(path):
    """
    :param path:    pdf文件路径
    :return: none
    """
    with pdfplumber.open(path) as pdf:
        for i, page in enumerate(pdf.pages):
            # 获取当前页面的全部文本信息，包括表格中的文字
            print(i)
            print(page.extract_text())
            print('---------- 分割线 ----------')

        pdf.close()

def 
if __name__ == '__main__':
    print("Hello World")
    path_pdf = r"中医预测疾病100法.pdf"
    path_txt = r"中医预测疾病100法_13008012.txt"
    read_pdf(path_pdf)
