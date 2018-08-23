##### Adding DHCP server IP address pool

/ip pool add name=dhcp-pool-1 ranges=192.168.88.2-192.168.88.254

##### Adding DHCP network

/ip dhcp-server network add address=192.168.88.0/24 dns-server=192.168.88.1 gateway=192.168.88.1 comment="added by setup"
#Adding DHCP server
/ip dhcp-server add interface=ether1 address-pool=dhcp-pool-1 lease-time=3d00:00:00 disabled=no
#Enabling interface
/interface enable ether2
#Adding IP address
/ip address add address=192.168.88.1/24 interface=ether2 comment="added by setup"s
#设置密码
/user set admin password="adwo88888"
password
#保存配置

#接口命名

#显示服务
ip server print

#设置web管理,端口
/ip service set www port=80 address=0.0.0.0/0

#接口重命令
 interface set ether2 name="lan2"
#接口配置地址
ip address add address=192.168.73.1/24 interface=lan2
#cpu,内存使用率
system resource  print
#接口dhcp获取地址,重新获取


#nat设置

ip firewall nat add chain=srcnat action=masquerade

#内网端口映射
ip firewall nat add action=dst-nat chain=dstnat dst-address=192.168.2.50 dst-port=80 protocol=tcp to-addresses=192.168.73.254 to-ports=80


chain=dstnat action=dst-nat to-addresses=192.168.1.205 to-ports=8080 protocol=tcp dst-address=61.50.130.250 dst-port=18080
#带宽控制
queue
#备份配置
system backup save name=""
system backup reload name=""
#系统复位
 system reset-configuration
#主机名
system identity print
#动态显示cpu使用率
system resource monitor
 system resource pci print
#生成技术支持文件
system sup-output
#设置默认网关

#自动获取
ip dhcp-client add interface=wan

#禁止来自公网的ping
/ip firewall filter add chain=output protocol=icmp action=drop comment="No Ping"

#端口状态

#系统时间
system clock \set time-zone=+08:00 time=17:42:26 date=Sep/25/2007

system clock set  time=10:05:05 date=oct/21/2016

#mac绑定
ip arp add address=192.168.0.11 mac-address=28:d2:44:67:d6:0c interface=lan0
#限速
:for ip from 1 to 254 do {/queue simple add target-addresses=("192.168.7." . $ip) max-limit=3M/3M }
#静态地址分配
 ip dhcp-server lease add address=192.168.0.11 mac-address=28:D2:44:67:D6:0C

#重定向dns服务器
ip firewall nat add chain=dstnat action=redirect to-ports=53 protocol=udp dst-port=53 log=no