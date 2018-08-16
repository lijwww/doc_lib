

### 定义

```
systemd 是 Linux 下的一款系统和服务管理器，兼容 SysV 和 LSB 的启动脚本。systemd 的特性有：支持并行化任务；同一时候採用 socket 式与 D-Bus 总线式激活服务；按需启动守护进程（daemon）。利用 Linux 的 cgroups 监视进程；支持快照和系统恢复。维护挂载点和自己主动挂载点。各服务间基于依赖关系进行精密控制。 
和init比起来引导过程简化了很多
Systemd支持并发引导过程从而可以更快启动
通过控制组来追踪进程，而不是PID
优化了处理引导过程和服务之间依赖的方式
支持系统快照和恢复
监控已启动的服务；也支持重启已崩溃服务
包含了systemd-login模块用于控制用户登录
支持加载和卸载组件
低内存使用痕迹以及任务调度能力
记录事件的Journald模块和记录系统日志的syslogd模块
```

 在 systemctl 參数中加入 -H <username>@<主机名> 能够实现对其它机器的远程控制。 

 systemadm 是 systemd 的官方图形前端。官方软件仓库 提供了稳定版本号 systemd-ui。 



| 命令                                          | 解释                       |
| --------------------------------------------- | -------------------------- |
| systemctl status                              | 显示 系统状态:             |
| systemctl                                     | 输出激活的单元             |
| systemctl list-units                          | 和上面等效                 |
| systemctl --failed                            | 输出激活失败的单元         |
| systemctl list-unit-files                     | 查看全部已安装服务：       |
| systemctl is-enabled postfix.service          | 检查一个服务是否是开机启动 |
| systemctl reset-failed                        |                            |
| systemctl daemon-reload                       |                            |
| systemctl condrestart sshd                    | 重新加载配置文件           |
| systemd-analyze plot > boot.svg               | 启动分析保存为svg          |
| systemctl  list-dependencies   wpa_supplicant | 查看依赖                   |
|                                               |                            |
|                                               |                            |
|                                               |                            |
|                                               |                            |
|                                               |                            |
|                                               |                            |
|                                               |                            |
|                                               |                            |



| /usr/lib/systemd/system/ |            |
| ------------------------ | ---------- |
| /etc/systemd/system/     | 优先级更高 |
|                          |            |
|                          |            |










```
Systemd-analyze是一个内建的命令，可以用来检测引导过程。你可以找出在启动过程中出错的单元，然后跟踪并改正引导组件的问题 
systemd-analyze  显示系统启动时间
```

| 参考网页                             |      |
| ------------------------------------ | ---- |
| http://blog.51cto.com/xuding/1730952 |      |
|                                      |      |
|                                      |      |

