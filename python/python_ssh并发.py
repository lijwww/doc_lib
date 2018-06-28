#!/usr/bin/env python
#encoding:utf8
#ssh_concurrent.py

import multiprocessing
import sys,os,time
import paramiko


def ssh_cmd(host,port,user,passwd,cmd):
	msg = "-----------Result:%s----------" % host

	s = paramiko.SSHClient()	#绑定实例
	s.load_system_host_keys()	#加载本机HOST主机文件
	s.set_missing_host_key_policy(paramiko.AutoAddPolicy())
	try:
		s.connect(host,22,user,passwd,timeout=5)   #连接远程主机
		stdin,stdout,stderr = s.exec_command(cmd)		#执行命令

		cmd_result = stdout.read(),stderr.read()		#读取命令结果
		print msg
		for line in cmd_result:
				print line,

		s.close()
	except paramiko.AuthenticationException:
		print msg
		print 'AuthenticationException Failed'
	except paramiko.BadHostKeyException:
		print msg
		print "Bad host key"	

result = []
p = multiprocessing.Pool(processes=20)
cmd=raw_input('CMD:')
f=open('serverlist.conf')
list = f.readlines()
f.close()
for IP in list:
	print IP
	host=IP.split()[0]
	port=int(IP.split()[1])
	user=IP.split()[2]
	passwd=IP.split()[3]
	result.append(p.apply_async(ssh_cmd,(host,port,user,passwd,cmd)))

p.close()
#p.join()

for res in result:
	res.get(timeout=35)

