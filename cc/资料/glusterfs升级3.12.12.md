 /usr/bin/apt install software-properties-common
 add-apt-repository ppa:gluster/glusterfs-3.12
(
cat <<EOF
deb http://ppa.launchpad.net/gluster/glusterfs-3.12/ubuntu xenial main 
deb-src http://ppa.launchpad.net/gluster/glusterfs-3.12/ubuntu xenial main 
EOF
) >>  /etc/apt/sources.list

/usr/bin/apt update
/usr/bin/apt install glusterfs-server glusterfs-client glusterfs-common  -y

/etc/init.d/glusterfs-server restart



rm -rf  /srv/gluster

mkdir -p /srv/gluster  /GlusterFS
chown -R phenix.phenix /srv/gluster
chown -R phenix.phenix /GlusterFS
gluster peer probe 10.33.70.98

 gluster peer status

 gluster volume create Storage 10.33.70.3:/srv/gluster 10.33.70.98:/srv/gluster

 gluster volume info
 gluster volume start    Storage
 mount -t glusterfs 127.0.0.1:/Storage /GlusterFS/





### 源码安装有问题

 locate gluster
 apt-get install uuid-dev libacl1-dev liblzo2-dev  -y
 apt-get install  liburcu-dev  -y

apt-get install openssl libssl-dev  -y

 flex
 bison
 python-dev
 apt install libibverbs1 libibverbs-dev  -y
 apt install liblvm2app2.2  libxml2-dev 
 #
 Makefile:80: *** missing separator.  Stop.