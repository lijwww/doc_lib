## 要升级的vdn



## 

### 要升级的vdn

![要升级nginx的vdn](图片/要升级nginx的vdn.png)







**vdn44-l7-142:**

![QQ截图20180816101235](图片/QQ截图20180816101235.png)



7483进程不退出

root@vdn44-l7-142:/var/www/dream/nginx/logs# strace  -p 7483

Process 7483 attached - interrupt to quit
	futex(0x7fcd7884e720, FUTEX_WAIT_PRIVATE, 2, NULL



***FUTEX_WAIT_PRIVATE***   状态







```
 ansible xinjiang -m shell -a "/var/www/dream/nginx/sbin/nginx -V"
 ansible xinjiang -m shell -a "mv /var/www/dream/nginx/sbin/nginx /var/www/dream/nginx/sbin/nginx_20180821"
 ansible xinjiang -m copy -a "src=nginx_v2 dest=/var/www/dream/nginx/sbin/nginx mode=0755"
 ansible xinjiang -m shell -a "/var/www/dream/nginx/sbin/nginx -t"
 ansible xinjiang -m shell -a   'kill -USR2 $(cat /var/www/dream/nginx/logs/nginx.pid)'
 ansible xinjiang -m shell -a   'kill -WINCH $(cat /var/www/dream/nginx/logs/nginx.pid.oldbin)'
 ansible xinjiang -m shell -a   'kill -QUIT $(cat /var/www/dream/nginx/logs/nginx.pid.oldbin)'
```

