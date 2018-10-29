#!/bin/bash
logfile="run.log"

log()
{
	ts=`date +%F_%T`
	echo $ts $* >> $logfile 
}

to_pro(){
	PID=$1
	TOMCATDIR=$2

	#备份文件
	src = "$TOMCATDIR/videonode/WEB-INF/classes/config.properties"
	log "config file $src"
	dest =  "$TOMCATDIR/videonode/WEB-INF/classes/config.properties_`date +%F_%T`"
	/bin/cp  -f  $src $dest

	#sed修改
	sed -i '/allow_ip/callow_ip=119.254.91.45,119.254.91.91,119.254.91.99,119.254.91.107,119.254.91.108,101.132.151.2,108,101.132.41.191,101.132.178.103,106.15.185.105' $src 
        log "$src  sed modify " 



	#重启Tomcat
	kill -9 $PID
	if [ $?  -eq 0 ]; then
		log "$pid killed"
		log "exec $TOMCATDIR/bin/startup.sh"
		/bin/bash $TOMCATDIR/bin/startup.sh
                log "$TOMCATDIR  started"  
	else
		log "$pid killed faild"
	fi
}



check_proc()
	{	
		TOMCATDIR=$1
		re="ps -ef|grep -v grep |grep $TOMCATDIR/conf/logging|wc -l "
		if [ $re -eq 1  ] ;then
			log "$TOMCATDIR  is exist"
		else
			log "please check_proc $TOMCATDIR" 
		fi

	}

#start  on    here
tomcat_list=`ps -ef|grep /var/www/dream/tomcat|grep -v grep |awk '{print $2,$9}'|sed -e 's/-Djava.util.logging.config.file=//' -e 's#/conf/logging.properties##' |tee tomcat_list.txt`

log " tomcat list -----  $tomcat_list" 
while  read line 
do
PID=`echo $line |awk '{print $1}' `
TOMCATDIR=`echo $line|awk '{print $2}'`
to_pro $PID $TOMCATDIR
sleep 3
check_proc $TOMCATDIR
read -p "go on to $PID $TOMCATDIR"

done<"tomcat_list.txt"
