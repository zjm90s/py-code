# -*- encoding:utf-8 -*-

__author__ = 'zjm'

import urllib2
import json

from __init__ import res_path


class SoaClient():
    __providers = dict()

    @classmethod
    def request(self, method, parms):
        """python请求java soa接口

        :param method: package#method
        :param parms: {}
        :return: json数据
        """
        method_strs = method.split("#")
        iface = method_strs[0]
        method = method_strs[1]
        provider = self.__providers[iface]
        url = "http://{}/rpc".format(provider)
        post_data = {
            "ver": "1.0",
            "soa": {"req": "12345", "rpc": "1.4.5.2"},
            "iface": iface,
            "method": method,
            "args": parms
        }

        request = urllib2.Request(url, json.dumps(post_data))
        response = urllib2.urlopen(request)
        resp_body = response.read()

        json_body = json.loads(resp_body)
        result = json_body["result"]
        if result:
            return json.loads(result)
        else:
            return dict()

    @classmethod
    def _init_client(self):
        """初始化Client

        根据resources/client.json初始化
        """
        clients = json.load(file(res_path("client.json")))
        for client in clients:
            for iface in client["ifaces"]:
                self.__providers[iface] = client["provider"]


# init
SoaClient._init_client()
