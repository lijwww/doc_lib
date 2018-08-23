route-nopull
可以使VPN连接后，并不修改默认路由，也就不会有任何网络请求走VPN。
client-cert-not-required则代表只使用用户名密码方式验证登录，如果不加，则代表需要证书和用户名密码双重验证登录



```
openvpn --remote 111.206.170.241  --port 10083 --proto tcp-server --dev tun1 --ifconfig 10.0.1.2 10.0.1.1
openvpn --remote www.lijw.net  --port 10083 --proto tcp-client --dev tun1 --ifconfig 10.0.1.1 10.0.1.2
```


