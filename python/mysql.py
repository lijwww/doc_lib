#!/usr/bin/python

import MySQLdb

def mysql_check(ip, user, password, table):
	con = MySQLdb.connect(host=ip, user=user, passwd=password, db='dbname', connect_timeout=5)
	curs = con.cursor()
	sql = "SELECT COUNT(*) FROM %s" % table
	curs.execute(sql)
	data = curs.fetchall()
	count = data[0][0]
	return ip + ':\t' + str(count)

def main():
	dbmain = {'ip':'192.168.1.10', 'user':'root', 'passwd':'pass', 'db':'dbname', 'table':'tablename'}
	dbback = {'ip':'192.168.1.10', 'user':'root', 'passwd':'pass', 'db':'dbname', 'table':'tablename'}
	count_main = mysql_check(dbmain['ip'], dbmain['user'], dbmain['passwd'], dbmain['db'], dbmain['table'])
	count_back =  mysql_check(dbback['ip'], dbback['user'], dbback['passwd'], dbback['db'], dbback['table'])
	print count_main
	print count_back


if __name__ == '__main__':
	main()


#def ydcit():
#	word = raw_input(The word you are looking for: ')
#	url = 'http://dict.youdao.com/search?le=eng&q=%s' % word
#	content = requests.get(url)
#
#
#while True:
#	ydcit()