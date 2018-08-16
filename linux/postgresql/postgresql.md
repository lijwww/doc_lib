### yum安装

yum install postgresql postgresql-devel postgresql-libs postgresql-server  postgresql-contrib   -y







|      |      |
| ---- | ---- |
|      |      |
|      |      |
|      |      |

#### 初始化

/usr/bin/postgresql-setup initdb

#### 启动服务

systemctl  enable postgresql.service

systemctl  start postgresql.service

#### 用户

passwd postgres

su - postgres

### 用户管理

 create  user sentry;

GRANT ALL ON sentry to sentry;

ALTER USER sentry WITH PASSWORD 'sentry'

|                |                                                        |
| -------------- | ------------------------------------------------------ |
|                |                                                        |
| 删除用户的密码 | `sudo`  `passwd` `-d postgres`                         |
|                | sudo  -u postgres passwd                               |
|                | GRANT SELECT ON ALL TABLES IN SCHEMA sentry to sentry; |
|                |                                                        |
| \?             | 帮助                                                   |
| \du            | 所有用户                                               |
| \l             | 所有数据库                                             |
|                |                                                        |



/var/lib/pgsql/data/postgresql.conf