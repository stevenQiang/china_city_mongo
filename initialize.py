# -*- coding: utf-8 -*-
from flask.ext.script import Command
from backend.models.addresses import Addresses
from backend import mongo, app


class Initialize(Command):
    """
    初始化数据
    """
    def run(self):
        print ("initialize data。。。")
        self.init_city()

    @staticmethod
    def init_city():
        print("init city...")
        url = './city/'
        file_name = ['province.txt', 'city.txt', 'county.txt']
        mongo.db.addresses.drop()
        for i in file_name:
            f = open(url+i, 'r+')
            if i == 'province.txt':
                for j in f.readlines():
                    j = j.strip('\n')
                    result = j.split(',')
                    params = {
                        'id': result[0],
                        'country_id': result[1],
                        'name': result[2],
                        'level': 1
                    }
                    Addresses.create(**params)
            elif i == 'city.txt':
                for j in f.readlines():
                    j = j.strip('\n')
                    result = j.split(',')
                    params = {
                        'id': result[0],
                        'country_id': result[1],
                        'province_id': result[2],
                        'name': result[3],
                        'level': 2
                    }
                    Addresses.create(**params)
            elif i == 'county.txt':
                for j in f.readlines():
                    j = j.strip('\n')
                    result = j.split(',')
                    params = {
                        'id': result[0],
                        'country_id': result[1],
                        'province_id': result[2],
                        'city_id': result[3],
                        'name': result[4],
                        'level': 3
                    }
                    Addresses.create(**params)
