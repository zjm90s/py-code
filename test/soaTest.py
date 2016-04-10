# -*- coding: utf-8 -*-
__author__ = 'zjm'

from main.z.soa.soa_client import SoaClient


# run
method = "me.ele.family.agent.service.IAgentService#getUserCity"
parms = {"userId": 1}
result = SoaClient.request(method, parms)
if result:
    print "agent_id:{}".format(result["agent_id"])
