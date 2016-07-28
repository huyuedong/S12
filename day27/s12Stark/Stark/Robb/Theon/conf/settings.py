#_*_coding:utf-8_*_
__author__ = 'Alex Li'


configs ={
    'HostID': 2,
    "Server": "localhost",
    "ServerPort": 8000,
    "urls":{

        'get_configs' :['monitor/api/client/config','get'],  #acquire all the services will be monitored
        'service_report': ['monitor/api/client/service/report/','post'],

    },
    'RequestTimeout':30,
    'ConfigUpdateInterval': 300, #5 mins as default

}