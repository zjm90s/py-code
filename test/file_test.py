# -*- coding: utf-8 -*-
__author__ = 'zjm'


class CityBo(object):
    id = 0
    name = ''

    def __init__(self, id, name):
        self.id = id
        self.name = name


def read():
    with open("/data/python/myReadFile.json") as file_read:
        line_list = file_read.readlines()
        city_list = []
        for line in line_list:
            strs = line.split(',')
            city = CityBo(strs[0], strs[1].strip('\n'))
            city_list.append(city)
        return city_list;


def write(city_list=[]):
    with open("/data/python/myWriteFile.json", "w") as file_read:
        for city in city_list:
            print city.id, city.name
            file_write.write(city.id + ' ' + city.name + '\n')
            # file_write.writelines(city_list_strings)


# run
city_list = read()
write(city_list)
