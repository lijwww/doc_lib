#!/usr/bin/python
# -*- coding: UTF-8 -*-
import commands
import json
import os
import time
import datetime
import socket
from copy import deepcopy

timestamp = int(time.time())
hostname = socket.gethostname()

data = {
    "endpoint": hostname,
    "tag": "",
    "timestamp": timestamp,
    "metric": None,
    "value": 0,
    "counterType": "GAUGE",
    "step": 300
}


cmd = commands.getoutput
date_time = time.strftime("%Y-%m-%d", time.localtime())
data_dir = "/var/www/dream/ControlCenter/logs/json/nginx_5min/%s" %date_time
json_log = "/var/www/dream/ControlCenter/logs/cdn_domain/json.log"
dic = {}
result = {}
datas = []
file_names = ['vdn34_03', 'vdn34_04', 'vdn34_51', 'vdn34_60',
              'vdn33_29', 'vdn33_32','vdn33_37', 'vdn33_39', 'vdn33_44', 'vdn33_80',
              'vdn42_15', 'vdn42_38', 'vdn42_55', 'vdn42_75', 'vdn42_188',
              'vdn44_142', 'vdn44_163', 'vdn44_166']

def get_file_data():
    '''
    文件合并后统计域名流量值
    '''
    if os.path.exists(json_log):
        os.remove(json_log)
    file_log = open('/var/www/dream/falcon-agents/plugin/sys/net/access_json.log','w') 
    if os.path.exists(data_dir) is False:
       exit(-1)
    for file_name in file_names:
        file_name = "access." + file_name
        file_com = os.path.join(data_dir,file_name) + ".log"
        if os.path.exists(file_com):
            for line in open(file_com):
                file_log.writelines(line)
        else:
            cmd("echo %s is not exist >> /tmp/data.log"  %file_com)
    file_log.close()  
    
    file_datas = open("/var/www/dream/falcon-agents/plugin/sys/net/access_json.log").readlines()
    for file_data in file_datas:
        data = eval(file_data)
        domain_name = data.get("domain", None)
        domain_size = data.get("size", None)
        if domain_name in dic.keys():
            dic[domain_name] += domain_size
        else:
            dic[domain_name] = domain_size

    with open("/var/www/dream/falcon-agents/plugin/sys/net/cdn.domain") as f:
        for i in f.readlines():
            play = i.split()[0]
            stor = i.split()[1]
            if dic.has_key(play) and dic.has_key(stor):
                dic[play] = dic.get(play) + dic.get(stor)
                dic.pop(stor)
            else:
                pass

    for x, y in dic.items():
        size_end = y * 8/300/1024/1024*1.05
        result[x] = float('%.3f' %int(size_end))
    if result.has_key(""): result.pop("")
#    for x,y in result.items():
#        data_end = '{"%s": %s}' %(x,y)
#        with open("/var/www/dream/ControlCenter/logs/cdn_domain/json.log", 'a') as f:
#            f.writelines(data_end +"\n")
    return result

try:
    get_file_data()
    for key, val in result.iteritems():
        _v = deepcopy(data)
        _v['metric'] = key
        _v['value'] = val
        datas.append(_v)
except Exception, e:
    print str(e)

print json.dumps(datas)
