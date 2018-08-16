

## ubuntu16.04



***mysql_config***

apt install libmysqlclient20 libmysqlclient-dev  -y

***mysql.h***

apt install  libmysqld-dev libmysql-cil-dev libmysqlclient-dev  -y



### 编译参数

```
 ./configure --prefix=/usr/local/bind/  \
 --enable-threads=no \
 --enable-newstats   \
 --with-dlz-mysql    \
 --disable-openssl-version-check
```

