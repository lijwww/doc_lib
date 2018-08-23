客户端配置

```
*.* @192.168.1.7
```



服务端配置

$ModLoad imudp
$UDPServerRun 514

:fromhost-ip, isequal, "192.168.0.1" /var/log/host0.1.log