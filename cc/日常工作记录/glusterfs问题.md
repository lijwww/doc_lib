### <a href="#1.1挂载大小不一致">挂载大小不一致 </a> 

- ### <a href="#1.1挂载大小不一致">挂载大小不一致 </a> 

- ### 



> ### 1.1挂载大小不一致

 218.60.53.79

```
Filesystem          Size  Used Avail Use% Mounted on
/dev/sda6           164G   18G  138G  12% /
udev                7.8G  4.0K  7.8G   1% /dev
tmpfs               1.6G  268K  1.6G   1% /run
none                5.0M     0  5.0M   0% /run/lock
none                7.8G     0  7.8G   0% /run/shm
/dev/sdb1            61T   55T  6.1T  91% /srv
/dev/sda5            93G  1.5G   87G   2% /u
127.0.0.1:/Storage  1.1P  880T  172T  84% /GlusterFS
```

218.60.53.87

```
Filesystem          Size  Used Avail Use% Mounted on
/dev/sda6           164G   18G  138G  12% /
udev                7.8G  4.0K  7.8G   1% /dev
tmpfs               1.6G  268K  1.6G   1% /run
none                5.0M     0  5.0M   0% /run/lock
none                7.8G     0  7.8G   0% /run/shm
/dev/sdb1            61T   55T  6.1T  91% /srv
/dev/sda5            93G  1.5G   87G   2% /u
127.0.0.1:/Storage  1.1P  880T  172T  84% /GlusterFS

```



GlusterFS 看到大小不一致







### 1.2 GlusterFS: {path} or a prefix of it is already part of a volume

问题:  在创建volume时出现错误

解决方案:

```
setfattr -x trusted.glusterfs.volume-id $brick_path
setfattr -x trusted.gfid $brick_path
rm -rf $brick_path/.glusterfs
```

[]: https://blog.csdn.net/xluren/article/details/43115729	"参考"

