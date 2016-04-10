# -*- coding: utf-8 -*-
__author__ = 'zjm'


class CityBo(object):
    id = 0
    name = ''

    def __init__(self, id, name):
        self.id = id
        self.name = name


def read():
    try:
        file_read = open("/data/python/myReadFile.json");
        line_list = file_read.readlines()
        city_list = []
        for line in line_list:
            strs = line.split(',')
            city = CityBo(strs[0], strs[1].strip('\n'))
            city_list.append(city)
        return city_list;
    finally:
        file_read.close()


def write(city_list=[]):
    try:
        file_write = open("/data/python/myWriteFile.json", "w")
        for city in city_list:
            print city.id, city.name
            file_write.write(city.id + ' ' + city.name + '\n')
            # file_write.writelines(city_list_strings)
    finally:
        file_write.close()


# run
city_list = read()
write(city_list)
