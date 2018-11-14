-  设置设备盘 
MegaCli -PDHSP   -Set   -Dedicated  -Array1  -physdrv[32:8] -a0

- 重建
     MegaCli  -pdrbld  -progdsply  -physdrv[E:S]  -a0   查看重建的进度
     MegaCli  -AdpSetProp  RebuildRate  -val  -a0     调快重建的速度
     MegaCli  -AdpAutoRbld -Enbl -a0  设置自动重建，当一个盘坏掉时，热备盘可以自动重建，代替坏的盘
     MegaCli -PDRbld -Start -PhysDrv [E0:S0] -a0 手动开始重建，E0:S0表示坏的盘
 - 让硬盘LED灯闪烁
     MegaCli  -AdpSetProp UseDiskActivityforLocate -1 -a0 
     MegaCli  -PdLocate  -start  –physdrv[E:S]  -a0  让硬盘LED灯闪烁
     MegaCli  -PdLocate  -stopt  –physdrv[E:S]  -a0 停掉硬盘LED灯


 https://blog.csdn.net/heart_2011/article/details/7254404
