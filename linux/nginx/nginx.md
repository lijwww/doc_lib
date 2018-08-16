-- 目录列表
autoindex on;
default_type 'text/html';
charset utf-8;



### nginx几种信号

TERM,INT 快速关闭

QUIT 从容关闭

HUP 平滑重启，重新加载配置文件

USR1 重新打开日志文件，在切割日志时用途较大

USR2 平滑升级可执行程序

WINCH 从容关闭工作进程

### nginx平滑升级

```
 kill -USR2 $(cat /var/www/dream/nginx/logs/nginx.pid)
 kill -WINCH $(cat /var/www/dream/nginx/logs/nginx.pid.oldbin)
 kill -QUIT $(cat /var/www/dream/nginx/logs/nginx.pid.oldbin)
```

