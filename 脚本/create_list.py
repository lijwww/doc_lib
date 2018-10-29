import redis
import ping3
import pickle
import os,sys
from prettytable import PrettyTable
from  termcolor import colored

pool = redis.ConnectionPool(host='localhost', port=6379, db=0)
rs_set_hostip="ip_host"

def host_ip2redis():
    f = open("host_ip","r")
    lines = f.readlines()
    ip_host_list=[]
    r = redis.Redis(connection_pool=pool)
    for line in lines:
        try:
            host,ip = line.strip().split(",")
            r.hset(rs_set_hostip,host,ip)
        except Exception as e:
            print(line,e)
        finally:
            r.close()

def ping_host(ip):
    return ping3.ping(dest_addr=ip, timeout=3)

def gethostip( hostname ):
    r = redis.Redis(connection_pool=pool)
    try:
        ip=r.hget(rs_set_hostip,hostname)
    except Exception as e:
        print("%s get error: %s" % ( hostname,e))
    finally:
        return ip


class check_hostalive_fromfile:
    def __init__(self,file,namenot=[],pingok_list= [],pingnot_list= []):
        if not os.path.exists(file):
            print("%s  not exists" % (file))
        with open(file,"r") as f:
            for line in  f.readlines():
                hostname=line.strip()
                ip=gethostip(hostname)
                if ip:
                    if ping_host(ip):
                        print("%s OK" % (hostname))
                        pingok_list.append(hostname)
                    else:
                        print("%s PING NOT" %(hostname))
                        pingnot_list.append(hostname)
                else:
                    print("%s  GET IP NOT" % (hostname) )

def print_ans(host,ip,passwd):
    print("%s ansible_ssh_host=%s ansible_ssh_port=12 ansible_ssh_user=phenix ansible_ssh_pass=\"%s\" ansible_sudo_pass=\"%s\"" % (host,ip,passwd,passwd))


def gen_ansible_string_dianbo(hostname,ip):
    if type(ip) == bytes:
        ip=ip.decode()
    last_num = ip.split(".")[3]
    passwd = "@videoCC%2018#m22_" + str(last_num)
    print_ans(hostname,ip,passwd)

# TODO: 判断服务器的属组


if __name__ == "__main__":
    pingok_list = []
    pingnot_list = []
    #filename = "host_category_by_jifang/zhoushan.list"
    filename = sys.argv[1]
    check_hostalive_fromfile(filename,pingok_list=pingok_list,pingnot_list=pingnot_list)
    for hostname in pingok_list:
        ip = gethostip(hostname)
        #print(ip)
        gen_ansible_string_dianbo(hostname, ip)



