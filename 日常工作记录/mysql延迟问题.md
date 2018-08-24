| name                     | 主库 | 备注 |
| ------------------------ | ---- | ---- |
| cc-h35.bokecc.com        |      |      |
| vdn52-vod-0.bokecc.com   |      |      |
| vdn52-vod-162.bokecc.com |      |      |









##### vdn52-vod-162.bokecc.com

	/var/www/dream/mysql-mercury

| 主库信息        |
| --------------- |
| 101.132.176.188 |
| 3309            |
| rep             |













### 告警机制

           if int(Seconds_Behind_Master) < 60 :
    
    return 0 

