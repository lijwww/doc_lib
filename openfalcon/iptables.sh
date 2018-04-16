#!/bin/sh
endpoint=host254
metric=iptables
tags=


# Source function library.
. /etc/init.d/functions

IPTABLES=iptables
IPTABLES_DATA=/etc/sysconfig/$IPTABLES
IPTABLES_FALLBACK_DATA=${IPTABLES_DATA}.fallback
IPTABLES_CONFIG=/etc/sysconfig/${IPTABLES}-config
IPV=${IPTABLES%tables} # ip for ipv4 | ip6 for ipv6
[ "$IPV" = "ip" ] && _IPV="ipv4" || _IPV="ipv6"
PROC_IPTABLES_NAMES=/proc/net/${IPV}_tables_names
VAR_SUBSYS_IPTABLES=/var/lock/subsys/$IPTABLES

# only usable for root
[ $EUID = 0 ] || exit 4

if [ ! -x /sbin/$IPTABLES ]; then
    echo -n $"${IPTABLES}: /sbin/$IPTABLES does not exist."; warning; echo
    exit 5
fi

# Old or new modutils
/sbin/modprobe --version 2>&1 | grep -q module-init-tools \
    && NEW_MODUTILS=1 \
    || NEW_MODUTILS=0

# Default firewall configuration:
IPTABLES_MODULES=""
IPTABLES_MODULES_UNLOAD="yes"
IPTABLES_SAVE_ON_STOP="no"
IPTABLES_SAVE_ON_RESTART="no"
IPTABLES_SAVE_COUNTER="no"
IPTABLES_STATUS_NUMERIC="yes"
IPTABLES_STATUS_VERBOSE="no"
IPTABLES_STATUS_LINENUMBERS="yes"
IPTABLES_SYSCTL_LOAD_LIST=""

# Load firewall configuration.
[ -f "$IPTABLES_CONFIG" ] && . "$IPTABLES_CONFIG"

# Netfilter modules
NF_MODULES=($(lsmod | awk "/^${IPV}table_/ {print \$1}") ${IPV}_tables)
NF_MODULES_COMMON=(x_tables nf_nat nf_conntrack) # Used by netfilter v4 and v6

# Get active tables
NF_TABLES=$(cat "$PROC_IPTABLES_NAMES" 2>/dev/null)







ts=`date +%s`;
status() {
    if [ ! -f "$VAR_SUBSYS_IPTABLES" -a -z "$NF_TABLES" ]; then
	echo $"${IPTABLES}: Firewall is not running. $ts"
	return 3
    fi

    # Do not print status if lockfile is missing and iptables modules are not 
    # loaded.
    # Check if iptable modules are loaded
    if [ ! -e "$PROC_IPTABLES_NAMES" ]; then
	echo $"${IPTABLES}: Firewall modules are not loaded. $ts"
	return 3
    fi

    # Check if firewall is configured (has tables)
    if [ -z "$NF_TABLES" ]; then
	echo $"${IPTABLES}: Firewall is not configured. $ts"
	return 3
    fi
    
    return 0
}
status
value=$?
curl -X POST -d "[{\"metric\": \"$metric\", \"endpoint\": \"$endpoint\", \"timestamp\": $ts,\"step\": 60,\"value\": $value,\"counterType\": \"GAUGE\",\"tags\": \"$tags\"}]" http://192.168.1.28:1988/v1/push
