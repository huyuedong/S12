from django.shortcuts import render,HttpResponse
import json
from  Stark import settings
from Robb.backends import redis_conn
from Robb.backends import data_processing
from Robb.backends import data_optimization
from Robb.serializer import  ClientHandler,get_host_triggers
from django.views.decorators.csrf import csrf_exempt
from Robb import models
# Create your views here.
REDIS_OBJ = redis_conn.redis_conn(settings)



def client_configs(request,client_id):
    print("--->",client_id)
    config_obj = ClientHandler(client_id)
    config = config_obj.fetch_configs()

    if config:
        return HttpResponse(json.dumps(config))


@csrf_exempt
def service_data_report(request):
    if request.method == 'POST':
        print("---->",request.POST)
        #REDIS_OBJ.set("test_alex",'hahaha')
        try:
            print('host=%s, service=%s' %(request.POST.get('client_id'),request.POST.get('service_name') ) )
            data =  json.loads(request.POST['data'])

            client_id = request.POST.get('client_id')
            service_name = request.POST.get('service_name')
            data_saveing_obj = data_optimization.DataStore(client_id,service_name,data,REDIS_OBJ)

            #redis_key_format = "StatusData_%s_%s_latest" %(client_id,service_name)
            #data['report_time'] = time.time()
            #REDIS_OBJ.lpush(redis_key_format,json.dumps(data))

            #在这里同时触发监控
            host_obj = models.Host.objects.get(id=client_id)
            service_triggers = get_host_triggers(host_obj)

            trigger_handler = data_processing.DataHandler(settings,connect_redis=False)
            for trigger in service_triggers:
                trigger_handler.load_service_data_and_calulating(host_obj,trigger,REDIS_OBJ)
            print("service trigger::",service_triggers)


            #更新主机存活状态
            #host_alive_key = "HostAliveFlag_%s" % client_id
            #REDIS_OBJ.set(host_alive_key,time.time())
        except IndexError as e:
            print('----->err:',e)


    return HttpResponse(json.dumps("---report success---"))
