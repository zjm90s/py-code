# -*- coding: utf-8 -*-
__author__ = 'zjm'

from os import path


def res_path(file_name):
    """资源路径

    :param file_name:
    :return: 文件完整路径
    """
    return "{}/{}".format(path.dirname(path.abspath(__file__)), file_name)
