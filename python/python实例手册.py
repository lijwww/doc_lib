	python实例手册

0说明

	手册制作: 雪松
	更新日期: 2013-09-11
	欢迎系统运维加入Q群: 198173206

	请勿删除信息，转载请说明出处，抵制不道德行为。
	错误在所难免，还望指正！

	# python实例手册下载地址:
	http://hi.baidu.com/quanzhou722/item/cf4471f8e23d3149932af2a7
	
	# shell实例手册最新下载地址:
	http://hi.baidu.com/quanzhou722/item/f4a4f3c9eb37f02d46d5c0d9

	# LazyManage运维批量管理软件下载(shell):
	http://hi.baidu.com/quanzhou722/item/4ccf7e88a877eaccef083d1a
	
# -*- coding:utf-8 -*-
#encoding:utf8
# 设定编码-支持中文

变量

	global x         # 全局变量
	a = 0 or 2 or 1  # 布尔运算赋值,a值为True既不处理后面,a值为2.  None、字符串''、空元组()、空列表[],空字典{}、0、空字符串都是false
	name = raw_input("input:").strip()        # 输入字符串变量
	num = int(raw_input("input:").strip())    # 输入字符串str转为int型

打印

# 字符串 %s  整数 %d  浮点 %f  原样打印 %r
	print '字符串: %s 整数: %d 浮点: %f 原样打印: %r' % ('aa',2,1.0,'r')

列表

	shoplist = ['apple', 'mango', 'carrot', 'banana']
	shoplist[2] = 'aa'
	del shoplist[0]
	shoplist.insert('4','www')
	shoplist.append('aaa')

元组

# 不可变
	zoo = ('wolf', 'elephant', 'penguin')

字典

	ab = {       'Swaroop'   : 'swaroopch@byteofpython.info',
				 'Larry'     : 'larry@wall.org',
		 }
	ab['c'] = 80      # 添加字典元素
	del ab['Larry']   # 删除字典元素
	ab.keys()         # 查看所有键值
	ab.values()       # 打印所有值
	ab.has_key('a')   # 查看键值是否存在
	ab.items()        # 返回整个字典列表

if判断

	# 布尔值操作符 and or not 实现多重判断
	if a == b:
		print '=='
	elif a < b:
		print b
	else:
		print a
	fi

while循环

	while True:
		if a == b:
			print "=="
			break
		print "!="
	else:
		print 'over'
	
	count=0
	while(count<9):
		print count
		count += 1

for循环

	sorted()           # 返回一个序列(列表)
	zip()              # 返回一个序列(列表)
	enumerate()        # 返回迭代器(类似序列)
	reversed()         # 反序迭代器对象
	dict.iterkeys()    # 通过键迭代
	dict.itervalues()  # 通过值迭代
	dict.iteritems()   # 通过键-值对迭代
	randline()         # 文件迭代
	iter(obj)          # 得到obj迭代器 检查obj是不是一个序列
	iter(a,b)          # 重复调用a,直到迭代器的下一个值等于b
	for i in range(1, 5):
		print i
	else:
		print 'over'

	list = ['a','b','c','b']
	for i in range(len(list)):
		print list[i]
	for x, Lee in enumerate(list):
		print "%d %s Lee" % (x+1,Lee)

tab补全

	# vim /usr/lib/python2.7/dist-packages/tab.py
	# python startup file
	import sys
	import readline
	import rlcompleter
	import atexit
	import os
	# tab completion
	readline.parse_and_bind('tab: complete')
	# history file
	histfile = os.path.join(os.environ['HOME'], '.pythonhistory')

函数

	def printMax(a, b = 1):
		if a > b:
			print a
			return a
		else:
			print b
			return b
	x = 5
	y = 7
	printMax(x, y)
	
	斐波那契
		#将函数结果作为列表可用于循环
		def fab(max): 
		n, a, b = 0, 0, 1 
		while n < max: 
			yield b         
			a, b = b, a + b 
			n = n + 1 
		for n in fab(5): 
			print n

模块

	# Filename: mymodule.py
	def sayhi():
		print 'mymodule'
	version = '0.1'

	# 导入模块
	import mymodule
	from mymodule import sayhi, version
	# 使用模块中函数
	mymodule.sayhi()

取参数

	import sys
	for i in sys.argv:
		print i
	
对象的方法

	class Person:
		# 实例化初始化的方法
		def __init__(self, name ,age):
			self.name = name
			self.age = age
			print self.name
		# 有self此函数为方法
		def sayHi(self):
			print 'Hello, my name is', self.name
		#对象消逝的时候被调用
		def __del__(self):
			print 'over'
	# 实例化对象
	p = Person('Swaroop')
	# 使用对象方法
	p.sayHi()
	# 继承
	class Teacher(Person):
		def __init__(self, name, age, salary):
			Person.__init__(self, name, age)
			self.salary = salary
			print '(Initialized Teacher: %s)' % self.name
		def tell(self):
			Person.tell(self)
			print 'Salary: "%d"' % self.salary
	t = Teacher('Mrs. Shrividya', 40, 30000)

文件处理

	# 模式: 读'r'  写'w' 追加'a' 读写'r+' 二进制文件'b'  'rb','wb','rb+'

	poem = '''\
		use Python!
	'''

	# 写文件  直接到文件尾部
	f = file('poem.txt', 'w') 
	f.write("string")
	f.write(str(i))
	f.flush()
	f.close() 

	# 读文件
	f = file('/etc/passwd','r')
	while True:
		line = f.readline()    # 返回一行
		if len(line) == 0:
			break
		x = line.split(":")                  # 冒号分割定义序列
        #x = [ x for x in line.split(":") ]  # 冒号分割定义序列
		#x = [ x.split("/") for x in line.split(":") ]  # 先冒号分割,在/分割 打印x[6][1]
		print x[6],"\n",
	f.close() 
	
	f = file('/etc/passwd')
	c = f.readlines()
	for line in c:
		print line.rstrip(),
	f.close()
	
	#追加日志
	log = open('/home/peterli/xuesong','a')
	print >> log,'faaa'
	log.close()

触发异常

	class ShortInputException(Exception):
		'''A user-defined exception class.'''
		def __init__(self, length, atleast):
			Exception.__init__(self)
			self.length = length
			self.atleast = atleast
	try:
		s = raw_input('Enter something --> ')
		if len(s) < 3:
			raise ShortInputException(len(s), 3)
	except EOFError:
		print '\nWhy did you do an EOF on me?'
	except ShortInputException, x:
		print 'ShortInputException: The input was of length %d, \
			  was expecting at least %d' % (x.length, x.atleast)
	else:
		print 'No exception was raised.' 

内建函数

	dir(sys)            # 显示对象的属性
	help(sys)           # 交互式帮助
	int(obj)            # 转型为整形
	str(obj)            # 转为字符串
	len(obj)            # 返回对象或序列长度
	open(file,mode)     # 打开文件 #mode (r 读,w 写, a追加)
	range(0,3)          # 返回一个整形列表
	raw_input("str:")   # 等待用户输入
	type(obj)           # 返回对象类型
	abs(-22)            # 绝对值
	random              # 随机数
	choice()            # 随机返回给定序列的一个元素
	divmod(x,y)         # 函数完成除法运算，返回商和余数。
	isinstance(object,int)    # 测试对象类型 int 
	round(x[,n])        # 函数返回浮点数x的四舍五入值，如给出n值，则代表舍入到小数点后的位数
	xrange()            # 函数与range()类似，但xrnage()并不创建列表，而是返回一个xrange对象
		xrange([lower,]stop[,step])
	strip()             # 是去除字符串两端多于空格,该句是去除序列中的所有字串两端多余的空格
	del                 # 删除列表里面的数据
	cmp(x,y)            # 比较两个对象    #根据比较结果返回一个整数，如果x<y，则返回-1；如果x>y，则返回1,如果x==y则返回0
	max()               # 字符串中最大的字符
	min()               # 字符串中最小的字符
	sorted()            # 对序列排序
	reversed()          # 对序列倒序
	enumerate()         # 返回索引位置和对应的值
	sum()               # 总和
	list()              # 变成列表可用于迭代
	tuple()             # 变成元组可用于迭代   #一旦初始化便不能更改的数据结构,速度比list快
	zip()               # 返回一个列表
		>>> s = ['11','22','33']
		>>> t = ['aa','bb','cc']
		>>> zip(s,t)
		[('11', 'aa'), ('22', 'bb'), ('33', 'cc')]

与字符串相关的模块

	string         # 字符串操作相关函数和工具
	re             # 正则表达式
	struct         # 字符串和二进制之间的转换
	c/StringIO     # 字符串缓冲对象,操作方法类似于file对象
	base64         # Base16\32\64数据编解码
	codecs         # 解码器注册和基类
	crypt          # 进行单方面加密
	difflib        # 找出序列间的不同
	hashlib        # 多种不同安全哈希算法和信息摘要算法的API
	hma            # HMAC信息鉴权算法的python实现
	md5            # RSA的MD5信息摘要鉴权
	rotor          # 提供多平台的加解密服务
	sha            # NIAT的安全哈希算法SHA
	stringprep     # 提供用于IP协议的Unicode字符串
	textwrap       # 文本包装和填充
	unicodedate    # unicode数据库

列表类型内建函数

	list.append(obj)                 # 向列表中添加一个对象obj
	list.count(obj)                  # 返回一个对象obj在列表中出现的次数
	list.extend(seq)                 # 把序列seq的内容添加到列表中
	list.index(obj,i=0,j=len(list))  # 返回list[k] == obj 的k值,并且k的范围在i<=k<j;否则异常
	list.insert(index.obj)           # 在索引量为index的位置插入对象obj
	list.pop(index=-1)               # 删除并返回指定位置的对象,默认是最后一个对象
	list.remove(obj)                 # 从列表中删除对象obj
	list.reverse()                   # 原地翻转列表
	list.sort(func=None,key=None,reverse=False)  # 以指定的方式排序列表中成员,如果func和key参数指定,则按照指定的方式比较各个元素,如果reverse标志被置为True,则列表以反序排列

序列类型操作符

	seq[ind]              # 获取下标为ind的元素
	seq[ind1:ind2]        # 获得下标从ind1到ind2的元素集合
	seq * expr            # 序列重复expr次
	seq1 + seq2           # 连接seq1和seq2
	obj in seq            # 判断obj元素是否包含在seq中
	obj not in seq        # 判断obj元素是否不包含在seq中

字符串类型内建方法

	string.expandtabs(tabsize=8)                  # tab符号转为空格 #默认8个空格
	string.endswith(obj,beg=0,end=len(staring))   # 检测字符串是否已obj结束,如果是返回True #如果beg或end指定检测范围是否已obj结束
	string.count(str,beg=0,end=len(string))       # 检测str在string里出现次数
	string.find(str,beg=0,end=len(string))        # 检测str是否包含在string中
	string.index(str,beg=0,end=len(string))       # 检测str不在string中,会报异常
	string.isalnum()                              # 如果string至少有一个字符并且所有字符都是字母或数字则返回True
	string.isalpha()                              # 如果string至少有一个字符并且所有字符都是字母则返回True
	string.isnumeric()                            # 如果string只包含数字字符,则返回True
	string.isspace()                              # 如果string包含空格则返回True
	string.isupper()                              # 字符串都是大写返回True
	string.islower()                              # 字符串都是小写返回True
	string.lower()                                # 转换字符串中所有大写为小写
	string.upper()                                # 转换字符串中所有小写为大写
	string.lstrip()                               # 截掉string左边的空格
	string.rstrip()                               # 删除string字符末尾的空格
	string.replace(str1,str2,num=string.count(str1))  # 把string中的str1替换成str2,如果num指定,则替换不超过num次
	string.startswith(obj,beg=0,end=len(string))  # 检测字符串是否以obj开头
	string.zfill(width)                           # 返回字符长度为width的字符,原字符串右对齐,前面填充0
	string.isdigit()                              # 只包含数字返回True
	string.split("分隔符")                        # 把string切片成一个列表
	":".join(string.split())                      # 以:作为分隔符,将所有元素合并为一个新的字符串

列表解析

	[ i * 2 for i in [8,-2,5]]
	[16,-4,10]
	[ i for i in range(8) if i %2 == 0 ]
	[0,2,4,6]

序列类型相关的模块

	array         # 一种受限制的可变序列类型,元素必须相同类型
	copy          # 提供浅拷贝和深拷贝的能力
	operator      # 包含函数调用形式的序列操作符 operator.concat(m,n)
	re            # perl风格的正则表达式查找
	StringIO      # 把长字符串作为文件来操作 如: read() \ seek()
	cStringIO     # 把长字符串作为文件来操,作速度更快,但不能被继承
	textwrap      # 用作包装/填充文本的函数,也有一个类
	types         # 包含python支持的所有类型
	collections   # 高性能容器数据类型

字典相关函数

	dict([container])     # 创建字典的工厂函数。提供容器类(container),就用其中的条目填充字典
	len(mapping)          # 返回映射的长度(键-值对的个数)
	hash(obj)             # 返回obj哈希值,判断某个对象是否可做一个字典的键值
	
字典内建方法

	dict.clear()                            # 删除字典中所有元素
	dict copy()                             # 返回字典(浅复制)的一个副本
	dict.fromkeys(seq,val=None)             # 创建并返回一个新字典,以seq中的元素做该字典的键,val做该字典中所有键对的初始值
	dict.get(key,default=None)              # 对字典dict中的键key,返回它对应的值value,如果字典中不存在此键,则返回default值
	dict.has_key(key)                       # 如果键在字典中存在,则返回True 用in和not in代替
	dicr.items()                            # 返回一个包含字典中键、值对元组的列表
	dict.keys()                             # 返回一个包含字典中键的列表
	dict.iter()                             # 方法iteritems()、iterkeys()、itervalues()与它们对应的非迭代方法一样,不同的是它们返回一个迭代子,而不是一个列表
	dict.pop(key[,default])                 # 和方法get()相似.如果字典中key键存在,删除并返回dict[key]
	dict.setdefault(key,default=None)       # 和set()相似,但如果字典中不存在key键,由dict[key]=default为它赋值
	dict.update(dict2)                      # 将字典dict2的键值对添加到字典dict
	dict.values()                           # 返回一个包含字典中所有值得列表      
	
集合方法
	
	s.issubset(t)                # 如果s是t的子集,则返回True   s <= t
	s.issuperset(t)              # 如果t是s的超集,则返回True   s >= t
	s.union(t)                   # 合并操作;返回一个新集合,该集合是s和t的并集   s | t
	s.intersection(t)            # 交集操作;返回一个新集合,该集合是s和t的交集   s & t
	s.difference(t)              # 返回一个新集合,改集合是s的成员,但不是t的成员  s - t
	s.symmetric_difference(t)    # 返回一个新集合,该集合是s或t的成员,但不是s和t共有的成员   s ^ t
	s.copy()                     # 返回一个新集合,它是集合s的浅复制
	obj in s                     # 成员测试;obj是s中的元素 返回True
	obj not in s                 # 非成员测试:obj不是s中元素 返回True
	s == t                       # 等价测试 是否具有相同元素
	s != t                       # 不等价测试 
	s < t                        # 子集测试;s!=t且s中所有元素都是t的成员
	s > t                        # 超集测试;s!=t且t中所有元素都是s的成员

可变集合方法

	s.update(t)                         # 用t中的元素修改s,s现在包含s或t的成员   s |= t
	s.intersection_update(t)            # s中的成员是共用属于s和t的元素          s &= t
	s.difference_update(t)              # s中的成员是属于s但不包含在t中的元素    s -= t
	s.symmetric_difference_update(t)    # s中的成员更新为那些包含在s或t中,但不是s和t共有的元素  s ^= t
	s.add(obj)                          # 在集合s中添加对象obj
	s.remove(obj)                       # 从集合s中删除对象obj;如果obj不是集合s中的元素(obj not in s),将引发KeyError错误
	s.discard(obj)                      # 如果obj是集合s中的元素,从集合s中删除对象obj
	s.pop()                             # 删除集合s中的任意一个对象,并返回它
	s.clear()                           # 删除集合s中的所有元素

序列化

	#!/usr/bin/python
	import cPickle
	obj = {'1':['4124','1241','124'],'2':['12412','142','1241']}

	pkl_file = open('account.pkl','wb')
	cPickle.down(obj,pkl_file)
	pkl_file.close()

	pkl_file = open('account.pkl','rb')
	account_list = cPickle.load(pkl_file)
	pkl_file.close()

文件对象方法
	
	file.close()                     # 关闭文件
	file.fileno()                    # 返回文件的描述符
	file.flush()                     # 刷新文件的内部缓冲区
	file.isatty()                    # 判断file是否是一个类tty设备
	file.next()                      # 返回文件的下一行,或在没有其他行时引发StopIteration异常
	file.read(size=-1)               # 从文件读取size个字节,当未给定size或给定负值的时候,读取剩余的所有字节,然后作为字符串返回
	file.readline(size=-1)           # 从文件中读取并返回一行(包括行结束符),或返回最大size个字符
	file.readlines(sizhint=0)        # 读取文件的所有行作为一个列表返回
	file.xreadlines()                # 用于迭代,可替换readlines()的一个更高效的方法
	file.seek(off, whence=0)         # 在文件中移动文件指针,从whence(0代表文件起始,1代表当前位置,2代表文件末尾)偏移off字节
	file.tell()                      # 返回当前在文件中的位置
	file.truncate(size=file.tell())  # 截取文件到最大size字节,默认为当前文件位置
	file.write(str)                  # 向文件写入字符串
	file.writelines(seq)             # 向文件写入字符串序列seq;seq应该是一个返回字符串的可迭代对象

文件对象的属性
	
	file.closed          # 表示文件已被关闭,否则为False
	file.encoding        # 文件所使用的编码  当unicode字符串被写入数据时,它将自动使用file.encoding转换为字节字符串;若file.encoding为None时使用系统默认编码
	file.mode            # Access文件打开时使用的访问模式
	file.name            # 文件名
	file.newlines        # 未读取到行分隔符时为None,只有一种行分隔符时为一个字符串,当文件有多种类型的行结束符时,则为一个包含所有当前所遇到的行结束符的列表
	file.softspace       # 为0表示在输出一数据后,要加上一个空格符,1表示不加

文件系统

	# os模块实现
	
	文件处理
		mkfifo()/mknod()       # 创建命名管道/创建文件系统节点
		remove()/unlink()      # 删除文件
		rename()/renames()     # 重命名文件
		*stat()                # 返回文件信息
		symlink()              # 创建符号链接
		utime()                # 更新时间戳
		tmpfile()              # 创建并打开('w+b')一个新的临时文件
		walk()                 # 遍历目录树下的所有文件名
	
	目录/文件夹
		chdir()/fchdir()       # 改变当前工作目录/通过一个文件描述符改变当前工作目录
		chroot()               # 改变当前进程的根目录
		listdir()              # 列出指定目录的文件
		getcwd()/getcwdu()     # 返回当前工作目录/功能相同,但返回一个unicode对象
		mkdir()/makedirs()     # 创建目录/创建多层目录
		rmdir()/removedirs()   # 删除目录/删除多层目录
	
	访问/权限
		saccess()              # 检验权限模式
		chmod()                # 改变权限模式
		chown()/lchown()       # 改变owner和groupID功能相同,但不会跟踪链接
		umask()                # 设置默认权限模式
		
	文件描述符操作
		open()                 # 底层的操作系统open(对于稳健,使用标准的内建open()函数)
		read()/write()         # 根据文件描述符读取/写入数据 按大小读取文件部分内容
		dup()/dup2()           # 复制文件描述符号/功能相同,但是复制到另一个文件描述符
	
	设备号
		makedev()              # 从major和minor设备号创建一个原始设备号
		major()/minor()        # 从原始设备号获得major/minor设备号
	
	os.path模块

		分隔
			basename()         # 去掉目录路径,返回文件名
			dirname()          # 去掉文件名,返回目录路径
			join()             # 将分离的各部分组合成一个路径名
			spllt()            # 返回(dirname(),basename())元组
			splitdrive()       # 返回(drivename,pathname)元组
			splitext()         # 返回(filename,extension)元组
		
		信息
			getatime()         # 返回最近访问时间
			getctime()         # 返回文件创建时间
			getmtime()         # 返回最近文件修改时间
			getsize()          # 返回文件大小(字节)
		
		查询
			exists()          # 指定路径(文件或目录)是否存在
			isabs()           # 指定路径是否为绝对路径
			isdir()           # 指定路径是否存在且为一个目录
			isfile()          # 指定路径是否存在且为一个文件
			islink()          # 指定路径是否存在且为一个符号链接
			ismount()         # 指定路径是否存在且为一个挂载点
			samefile()        # 两个路径名是否指向同一个文件
	
	相关模块
		base64              # 提供二进制字符串和文本字符串间的编码/解码操作
		binascii            # 提供二进制和ASCII编码的二进制字符串间的编码/解码操作
		bz2                 # 访问BZ2格式的压缩文件
		csv                 # 访问csv文件(逗号分隔文件)
		filecmp             # 用于比较目录和文件
		fileinput           # 提供多个文本文件的行迭代器
		getopt/optparse     # 提供了命令行参数的解析/处理
		glob/fnmatch        # 提供unix样式的通配符匹配的功能
		gzip/zlib           # 读写GNU zip(gzip)文件(压缩需要zlib模块)
		shutil              # 提供高级文件访问功能
		c/StringIO          # 对字符串对象提供类文件接口
		tarfile             # 读写TAR归档文件,支持压缩文件
		tempfile            # 创建一个临时文件
		uu                  # uu格式的编码和解码
		zipfile             # 用于读取zip归档文件的工具
		environ['HOME']     # 查看系统环境变量
		
异常

	NameError:              # 尝试访问一个未申明的变量
	ZeroDivisionError:      # 除数为零
	SyntaxErrot:            # 解释器语法错误
	IndexError:             # 请求的索引元素超出序列范围
	KeyError:               # 请求一个不存在的字典关键字
	IOError:                # 输入/输出错误
	AttributeError:         # 尝试访问未知的对象属性
	ImportError             # 没有模块
	IndentationError        # 语法缩进错误
	KeyboardInterrupt       # ctrl+C
	SyntaxError             # 代码语法错误
	ValueError              # 值错误
	TypeError               # 传入对象类型与要求不符合
	try-except              # 检测和处理异常	
		class MyException(Exception):   # 继承Exception异常的类,定义自己的异常
				pass
		try:                          # 监控这里的异常
				option=int(raw_input('my age:'))
				if option != 28:
						raise MyException,'a1'  #触发异常
		except MyException,a:         # 异常处理代码
				print 'MyExceptionaa'
				print a    # 打印异常处内容
		except:            # 捕捉所有其它错误
				print 'except'
		finally:           # 无论什么情况都会执行 关闭文件或断开连接等
			   print 'finally' 
		else:             # 无任何异常 无法和finally同用
		        print 'no Exception'

触发异常

	raise exclass            # 触发异常,从exclass生成一个实例(不含任何异常参数)
	raise exclass()          # 触发异常,但现在不是类;通过函数调用操作符(function calloperator:"()")作用于类名生成一个新的exclass实例,同样也没有异常参数
	raise exclass, args      # 触发异常,但同时提供的异常参数args,可以是一个参数也可以是元组
	raise exclass(args)      # 触发异常,同上
	raise exclass, args, tb  # 触发异常,但提供一个跟踪记录(traceback)对象tb供使用
	raise exclass,instance   # 通过实例触发异常(通常是exclass的实例)
	raise instance           # 通过实例触发异常;异常类型是实例的类型:等价于raise instance.__class__, instance
	raise string             # 触发字符串异常
	raise string, srgs       # 触发字符串异常,但触发伴随着args
	raise string,args,tb     # 触发字符串异常,但提供一个跟踪记录(traceback)对象tb供使用
	raise                    # 重新触发前一个异常,如果之前没有异常,触发TypeError
	
内建异常
	
	BaseException                # 所有异常的基类
	SystemExit                   # python解释器请求退出
	KeyboardInterrupt            # 用户中断执行
	Exception                    # 常规错误的基类
	StopIteration                # 迭代器没有更多的值
	GeneratorExit                # 生成器发生异常来通知退出
	SystemExit                   # python解释器请求退出
	StandardError                # 所有的内建标准异常的基类
	ArithmeticError              # 所有数值计算错误的基类
	FloatingPointError           # 浮点计算错误
	OverflowError                # 数值运算超出最大限制
	AssertionError               # 断言语句失败
	AttributeError               # 对象没有这个属性
	EOFError                     # 没有内建输入,到达EOF标记
	EnvironmentError             # 操作系统错误的基类
	IOError                      # 输入/输出操作失败
	OSError                      # 操作系统错误
	WindowsError                 # windows系统调用失败
	ImportError                  # 导入模块/对象失败
	KeyboardInterrupt            # 用户中断执行(通常是ctrl+c)
	LookupError                  # 无效数据查询的基类
	IndexError                   # 序列中没有此索引(index)
	KeyError                     # 映射中没有这个键
	MemoryError                  # 内存溢出错误(对于python解释器不是致命的)
	NameError                    # 未声明/初始化对象(没有属性)
	UnboundLocalError            # 访问未初始化的本地变量
	ReferenceError               # 若引用试图访问已经垃圾回收了的对象
	RuntimeError                 # 一般的运行时错误
	NotImplementedError          # 尚未实现的方法
	SyntaxError                  # python语法错误
	IndentationError             # 缩进错误
	TabError                     # tab和空格混用
	SystemError                  # 一般的解释器系统错误
	TypeError                    # 对类型无效的操作
	ValueError                   # 传入无效的参数
	UnicodeError                 # Unicode相关的错误
	UnicodeDecodeError           # Unicode解码时的错误
	UnicodeEncodeError           # Unicode编码时的错误
	UnicodeTranslateError        # Unicode转换时错误
	Warning                      # 警告的基类
	DeprecationWarning           # 关于被弃用的特征的警告
	FutureWarning                # 关于构造将来语义会有改变的警告
	OverflowWarning              # 旧的关于自动提升为长整形的警告
	PendingDeprecationWarning    # 关于特性将会被废弃的警告
	RuntimeWarning               # 可疑的运行时行为的警告
	SyntaxWarning                # 可疑的语法的警告
	UserWarning                  # 用户代码生成的警告

跨平台os模块属性

	linesep         # 用于在文件中分隔行的字符串
	sep             # 用来分隔文件路径名字的字符串
	pathsep         # 用于分割文件路径的字符串
	curdir          # 当前工作目录的字符串名称
	pardir          # 父目录字符串名称
	
函数式编程的内建函数

	apply(func[,nkw][,kw])          # 用可选的参数来调用func,nkw为非关键字参数,kw为关键字参数;返回值是函数调用的返回值
	filter(func,seq)                # 调用一个布尔函数func来迭代遍历每个seq中的元素;返回一个使func返回值为true的元素的序列
	map(func,seq1[,seq2])           # 将函数func作用于给定序列(s)的每个元素,并用一个列表来提供返回值;如果func为None,func表现为一个身份函数,返回一个含有每个序列中元素集合的n个元组的列表
	reduce(func,seq[,init])         # 将二元函数作用于seq序列的元素,每次携带一堆(先前的结果以及下一个序列元素),连续地将现有的结果和下一个值作用在获得的随后的结果上,最后减少我们的序列为一个单一的返回值;如果初始值init给定,第一个比较会是init和第一个序列元素而不是序列的头两个元素

re正则

	compile(pattern,flags=0)          # 对正则表达式模式pattern进行编译,flags是可选标识符,并返回一个regex对象
	match(pattern,string,flags=0)     # 尝试用正则表达式模式pattern匹配字符串string,flags是可选标识符,如果匹配成功,则返回一个匹配对象;否则返回None
	search(pattern,string,flags=0)    # 在字符串string中搜索正则表达式模式pattern的第一次出现,flags是可选标识符,如果匹配成功,则返回一个匹配对象;否则返回None
	findall(pattern,string[,flags])   # 在字符串string中搜索正则表达式模式pattern的所有(非重复)出现:返回一个匹配对象的列表
	finditer(pattern,string[,flags])  # 和findall()相同,但返回的不是列表而是迭代器;对于每个匹配,该迭代器返回一个匹配对象
	split(pattern,string,max=0)       # 根据正则表达式pattern中的分隔符把字符string分割为一个列表,返回成功匹配的列表,最多分割max次(默认所有)
	sub(pattern,repl,string,max=0)    # 把字符串string中所有匹配正则表达式pattern的地方替换成字符串repl,如果max的值没有给出,则对所有匹配的地方进行替换(subn()会返回一个表示替换次数的数值)
	group(num=0)                      # 返回全部匹配对象(或指定编号是num的子组)
	groups()                          # 返回一个包含全部匹配的子组的元组(如果没匹配成功,返回一个空元组)
	re.sub('[abc]','A','alex')        # 替换

多线程

	thread
		start_new_thread(function,args kwargs=None)    # 产生一个新的线程
		allocate_lock()                                # 分配一个LockType类型的锁对象
		exit()                                         # 让线程退出
		acquire(wait=None)                             # 尝试获取锁对象
		locked()                                       # 如果获取了锁对象返回True
		release()                                      # 释放锁
	
	threading
		Thread                   # 表示一个线程的执行的对象
			start()              # 开始线程的执行
			run()                # 定义线程的功能的函数(一般会被子类重写)
			join(timeout=None)   # 程序挂起,知道线程结束;如果给了timeout,则最多阻塞timeout秒
			getName()            # 返回线程的名字
			setName(name)        # 设置线程的名字
			isAlive()            # 布尔标志,表示这个线程是否还在运行中
			isDaemon()           # 返回线程的daemon标志
			setDaemon(daemonic)  # 把线程的daemon标志设置为daemonic(一定要在调用start()函数前调用)
		Lock              # 锁原语对象
		Rlock             # 可重入锁对象.使单线程可以在此获得已获得了的锁(递归锁定)
		Condition         # 条件变量对象能让一个线程停下来,等待其他线程满足了某个条件.如状态改变或值的改变
		Event             # 通用的条件变量.多个线程可以等待某个事件的发生,在事件发生后,所有的线程都会被激活
		Semaphore         # 为等待锁的线程提供一个类似等候室的结构
		BoundedSemaphore  # 与Semaphore类似,只是不允许超过初始值
		Time              # 与Thread相似,只是他要等待一段时间后才开始运行
		activeCount()     # 当前活动的线程对象的数量
		currentThread()   # 返回当前线程对象
		enumerate()       # 返回当前活动线程的列表
		settrace(func)    # 为所有线程设置一个跟踪函数
		setprofile(func)  # 为所有线程设置一个profile函数

	thread例子

		#!/usr/bin/env python
		#thread_test.py
		#不支持守护进程
		import thread
		from time import sleep,ctime

		loops = [4,2]

		def loop(nloop,nsec,lock):
			print 'start loop %s at:%s' % (nloop,ctime())
			sleep(nsec)
			print 'loop %s done at: %s' % (nloop, ctime())
			lock.release()              # 分配已获得的锁,操作结束后释放相应的锁通知主线程

		def main():
			print 'starting at:',ctime()
			locks = []
			nloops = range(len(loops))
			
			for i in nloops:
				lock = thread.allocate_lock()     # 创建一个锁
				lock.acquire()                    # 调用各个锁的acquire()函数获得锁
				locks.append(lock)                # 把锁放到锁列表locks中
			for i in nloops:
				thread.start_new_thread(loop,(i,loops[i],locks[i]))   # 创建线程
			for i in nloops:
				while locks[i].locked():pass      # 等待全部解锁才继续运行
			print 'all DONE at:',ctime()

		if __name__ == '__main__':
			main()

	multiprocessing例子

		并发

			from multiprocessing import Process,Lock
			import time,os

			def sayhi(i):
				print 'hello',i
				time.sleep(10)
			#lock = Lock()

			for n in range(100):
				p = Process(target=sayhi,args=(n,))
				p.start()
				#p.join()  # 等待上一行执行完成
			
		并发例子
		
			import multiprocessing
			import time,os

			result = []
			def run(h):
				print 'threading:' ,h,os.getpid()
			p = multiprocessing.Pool(processes=20)

			for i in range(100):
				result.append(p.apply_async(run,(i,)))
			p.close()
			
			for res in result:
				res.get(timeout=5)

socket通讯

	from socket import *         # 避免 socket.socket()
	
	s.bind()         # 绑定地址到套接字
	s.listen()       # 开始TCP监听
	s.accept()       # 被动接受TCP客户端连接，等待连接的到来
	s.connect()      # 主动初始化TCP服务器连接
	s.connect_ex()   # connect()函数的扩展版本，出错时返回出错码，而不是跑出异常
	s.recv()         # 接收TCP数据
	s.send()         # 发送TCP数据
	s.sendall()      # 完整发送TCP数据
	s.recvfrom()     # 接收UDP数据
	s.sendto()       # 发送UDP数据
	s.getpeername()  # 连接到当前套接字的远端的地址(TCP连接)
	s.getsockname()  # 当前套接字的地址
	s.getsockopt()   # 返回指定套接字的参数
	s.setsockopt()   # 设置指定套接字的参数
	s.close()        # 关闭套接字
	s.setblocking()  # 设置套接字的阻塞与非阻塞模式
	s.settimeout()   # 设置阻塞套接字操作的超时时间
	s.gettimeout()   # 得到阻塞套接字操作的超时时间
	s.filen0()       # 套接字的文件描述符
	s.makefile()     # 创建一个与该套接字关联的文件对象

	socket.AF_UNIX	 # 只能够用于单一的Unix系统进程间通信
	socket.AF_INET 	 # 服务器之间网络通信
	socket.AF_INET6	 # IPv6

	socket.SOCK_STREAM	  # 流式socket , for TCP
	socket.SOCK_DGRAM	  # 数据报式socket , for UDP
	socket.SOCK_RAW	      # 原始套接字，普通的套接字无法处理ICMP、IGMP等网络报文，而SOCK_RAW可以；其次，SOCK_RAW也可以处理特殊的IPv4报文；此外，利用原始套接字，可以通过IP_HDRINCL套接字选项由用户构造IP头。

	socket.SOCK_RDM 	  # 是一种可靠的UDP形式，即保证交付数据报但不保证顺序。SOCK_RAM用来提供对原始协议的低级访问，在需要执行某些特殊操作时使用，如发送ICMP报文。SOCK_RAM通常仅限于高级用户或管理员运行的程序使用。

	socket.SOCK_SEQPACKET	 # 可靠的连续数据包服务

	SocketServer
	
		#!/usr/bin/python
		#server.py
		import SocketServer
		import os
		class MyTCP(SocketServer.BaseRequestHandler):
			def handle(self):
				while True:
					self.data=self.request.recv(1024).strip()
					if self.data == 'quit' or not self.data:break
					
					cmd=os.popen(self.data).read()
					if cmd == '':cmd= self.data + ': Command not found'
					self.request.sendall(cmd)
		if __name__ == '__main__':
			HOST,PORT = '10.0.0.119',50007
			server = SocketServer.ThreadingTCPServer((HOST,PORT),MyTCP)
			server.serve_forever()

	SocketClient

		#!/usr/bin/python
		#client.py
		import socket

		HOST='10.0.0.119'
		PORT=50007
		s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
		s.connect((HOST,PORT))

		while True:
			while True:
				cmd=raw_input('CMD:').strip()
				if cmd != '':break
			s.sendall(cmd)      
			data=s.recv(1024).split('\n')
			print 'cmd:'
			for line in data:print line
		s.close()

	ftp

		ftpserver

			#!/usr/bin/python
			#ftpserver.py

			import SocketServer
			import os
			import cPickle
			import md5
			from time import sleep

			def filer(file1):
				try:
					f = file(file1,'rb')
					return cPickle.load(f)
				except IOError:
					return {}
				except EOFError:
					return {}
				f.close()

			def filew(file1,content):
				f = file(file1,'wb')
				cPickle.dump(content,f)
				f.close()

			class MyTCP(SocketServer.BaseRequestHandler):
				def handle(self):
					i = 0
					while i<3:
						user=self.request.recv(1024).strip()
						userinfo=filer('user.pkl')
						if userinfo.has_key(user.split()[0]):
							if md5.new(user.split()[1]).hexdigest() == userinfo[user.split()[0]]:
								results='login successful'
								self.request.sendall(results)
								login='successful'
								break
							else:
								i = i + 1
								results='Error:password not correct'
								self.request.sendall(results)
								continue
						else:
							i = i + 1
							results='Error:password not correct'
							self.request.sendall(results)
							continue
						break
					else:
						results = 'Error:Wrong password too many times'
						self.request.sendall(results)
						login='failure'
					home_path = os.popen('pwd').read().strip() + '/' + user.split()[0]
					current_path = '/'
					print home_path
					while True:
						if login == 'failure':
							break
						print 'home_path:%s=current_path:%s' %(home_path,current_path)
						cmd=self.request.recv(1024).strip()
						print cmd
						if cmd == 'quit':
							break
						elif cmd == 'dir':
							list=os.listdir('%s%s' %(home_path,current_path))
							if list:
								dirlist,filelist = '',''
								for i in list:
									if os.path.isdir('%s%s%s' %(home_path,current_path,i)):
										dirlist = dirlist + '\033[32m' + i + '\033[m\t'
									else:
										filelist = filelist + i + '\t'
								results = dirlist + filelist
							else:
								results = '\033[31mnot find\033[m'
							self.request.sendall(results)
						elif cmd == 'pdir':
							self.request.sendall(current_path)
						elif cmd.split()[0] == 'mdir':
							if cmd.split()[1].isalnum():
								tmppath='%s%s%s' %(home_path,current_path,cmd.split()[1])
								os.makedirs(tmppath)
								self.request.sendall('\033[32mcreating successful\033[m')
							else:
								self.request.sendall('\033[31mcreate failure\033[m')
						elif cmd.split()[0] == 'cdir':
							if cmd.split()[1] == '/':
								tmppath='%s%s' %(home_path,cmd.split()[1])
								if os.path.isdir(tmppath):
									current_path = cmd.split()[1]
									self.request.sendall(current_path)
								else:
									self.request.sendall('\033[31mnot_directory\033[m')
							elif cmd.split()[1].startswith('/'):
								tmppath='%s%s' %(home_path,cmd.split()[1])
								if os.path.isdir(tmppath):
									current_path = cmd.split()[1] + '/'
									self.request.sendall(current_path)
								else:
									self.request.sendall('\033[31mnot_directory\033[m')
							else:
								tmppath='%s%s%s' %(home_path,current_path,cmd.split()[1])
								if os.path.isdir(tmppath):
									current_path = current_path + cmd.split()[1] + '/'
									self.request.sendall(current_path)
								else:
									self.request.sendall('\033[31mnot_directory\033[m')
						elif cmd.split()[0] == 'get':
							if os.path.isfile('%s%s%s' %(home_path,current_path,cmd.split()[1])):
								f = file('%s%s%s' %(home_path,current_path,cmd.split()[1]),'rb')
								self.request.sendall('ready_file')
								sleep(0.5)
								self.request.send(f.read())
								f.close()
								sleep(0.5)
							elif os.path.isdir('%s%s%s' %(home_path,current_path,cmd.split()[1])):
								self.request.sendall('ready_dir')
								sleep(0.5)
								for dirpath in os.walk('%s%s%s' %(home_path,current_path,cmd.split()[1])):
									dir=dirpath[0].replace('%s%s' %(home_path,current_path),'',1)
									self.request.sendall(dir)
									sleep(0.5)
									for filename in dirpath[2]:
										self.request.sendall(filename)
										sleep(0.5)
										f = file('%s/%s' %(dirpath[0],filename),'rb')
										self.request.send(f.read())
										f.close()
										sleep(0.5)
										self.request.sendall('file_get_done')
										sleep(0.5)
									else:
										self.request.sendall('dir_get_done')
									sleep(0.5)
							else:
								self.request.sendall('get_failure')
								continue
							self.request.sendall('get_done')
					
						elif cmd.split()[0] == 'send':
							if os.path.exists('%s%s%s' %(home_path,current_path,cmd.split()[1])):
								self.request.sendall('existing')
								action=self.request.recv(1024)
								if action == 'cancel':
									continue
							self.request.sendall('ready')
							msg=self.request.recv(1024)
							if msg == 'ready_file':
								f = file('%s%s%s' %(home_path,current_path,cmd.split()[1]),'wb')
								while True:
									data=self.request.recv(1024)
									if data == 'file_send_done':break
									f.write(data)
								f.close()

							elif msg == 'ready_dir':
								os.system('mkdir -p %s%s%s' %(home_path,current_path,cmd.split()[1]))
								while True:
									dir=self.request.recv(1024)
									if dir == 'get_done':break
									os.system('mkdir -p %s%s%s' %(home_path,current_path,dir))
									while True:
										filename=self.request.recv(1024)
										if filename == 'dir_send_done':break
										f = file('%s%s%s/%s' %(home_path,current_path,dir,filename),'wb')
										while True:
											data=self.request.recv(1024)
											if data == 'file_send_done':break 
											f.write(data)
										f.close()
										self.request.sendall('%s/%s\t\033[32mfile_done\033[m' %(dir,filename))
									self.request.sendall('%s\t\033[32mdir_done\033[m' %(dir))
							elif msg == 'unknown_file':
								continue
							
						else:
							results = cmd.split()[0] + ': Command not found'
							self.request.sendall(results)

			if __name__ == '__main__':
				HOST,PORT = '10.152.14.85',50007
				server = SocketServer.ThreadingTCPServer((HOST,PORT),MyTCP)
				server.serve_forever()

		ftpmanage

			#!/usr/bin/python
			#manage_ftp.py
			import cPickle
			import sys
			import md5
			import os
			import getpass

			def filer(file1):
				try:
					f = file(file1,'rb')
					return cPickle.load(f)
				except IOError:
					return {}
				except EOFError:
					return {}
				f.close()

			def filew(file1,content):
				f = file(file1,'wb')
				cPickle.dump(content,f)
				f.close()

			while True:
				print '''
				1.add user
				2.del user
				3.change password
				4.query user
				0.exit
				'''
				i = raw_input(':').strip()
				userinfo=filer('user.pkl')
				if i == '':
					continue
				elif i == '1':
					while True:
						user=raw_input('user name:').strip()
						if user.isalnum():
							i = 0
							while i<3:
								passwd=getpass.getpass('passwd:').strip()
								if passwd == '':
									continue
								else:
									passwd1=getpass.getpass('Confirm password:').strip()
									if passwd == passwd1:
										mpasswd = md5.new(passwd).hexdigest()
										userinfo[user] = mpasswd
										os.system('mkdir -p %s' %user)
										print '%s creating successful ' %user
										break
									else:
										print "Passwords don't match "
										i = i + 1
										continue
							else:
								print 'Too many wrong'
								continue
							break
						else:
							print 'user not legal'
							continue
				elif i == '2':
					user=raw_input('user name:').strip()
					if userinfo.has_key(user):
						del userinfo[user]
						print 'Delete users successfully'
					else:
						print 'user not exist'
						continue
				elif i == '3':
					user=raw_input('user name:').strip()
					if userinfo.has_key(user):
						i = 0
						while i<3:
							passwd=getpass.getpass('passwd:').strip()
							if passwd == '':
								continue
							else:
								passwd1=getpass.getpass('Confirm password:').strip()
								if passwd == passwd1:
									mpasswd = md5.new(passwd).hexdigest()
									userinfo[user] = mpasswd
									print '%s password is changed' %user
									break
								else:
									print "Passwords don't match "
									i = i + 1
									continue
						else:
							print 'Too many wrong'
							continue
					else:
						print 'user not exist'
						continue
				elif i == '4':
					print userinfo.keys()
				elif i == '0':
					sys.exit()
				else:
					print 'select error'
					continue
				filew('user.pkl',content=userinfo)
		
		ftpclient

			#!/usr/bin/python
			#ftpclient.py

			import socket
			import os
			import getpass
			from time import sleep

			HOST='10.152.14.85'
			PORT=50007
			s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
			s.connect((HOST,PORT))
				
			while True:
				user = raw_input('user:').strip()
				if user.isalnum():
					while True:
						passwd = getpass.getpass('passwd:').strip()
						s.sendall(user + ' ' + passwd)
						servercmd=s.recv(1024)
						if servercmd == 'login successful':
							print '\033[32m%s\033[m' %servercmd
							break
						else:
							print servercmd

					while True:
						cmd=raw_input('FTP>').strip()
						if cmd == '':
							continue
						if cmd.split()[0] == 'get':
							if cmd == 'get':continue
							for i in cmd.split()[1:]:
								if os.path.exists(i):
									confirm = raw_input("\033[31mPlease confirm whether the cover %s(Y/N):\033[m" %(i)).upper().startswith('Y')
									if not confirm:
										print '%s cancel' %i
										continue
								s.sendall('get ' + i)
								servercmd=s.recv(1024)
								if servercmd == 'inexistence':
									print '%s \t\033[32minexistence\033[m' %i
									continue
								elif servercmd == 'ready_file':
									f = file(i,'wb')
									while True:
										data=s.recv(1024)
										if data == 'get_done':break 
										f.write(data)
									f.close()
									print '%s \t\033[32mfile_done\033[m' %(i)
								elif servercmd == 'ready_dir':
									try:
										os.makedirs(i)
									except:
										pass
									while True:
										serverdir=s.recv(1024)
										if serverdir == 'get_done':break 
										os.system('mkdir -p %s' %serverdir)
										print '%s \t\033[32mdir_done\033[m' %(serverdir)
										while True:
											serverfile=s.recv(1024)
											if serverfile == 'dir_get_done':break 
											f = file('%s/%s' %(serverdir,serverfile),'wb')
											while True:
												data=s.recv(1024)
												if data == 'file_get_done':break 
												f.write(data)
											f.close()
											print '%s/%s \t\033[32mfile_done\033[m' %(serverdir,serverfile)

						elif cmd.split()[0] == 'send':
						
							if cmd == 'send':continue
							for i in cmd.split()[1:]:
								if not os.path.exists(i):
									print '%s\t\033[31minexistence\033[m' %i
									continue
							
								s.sendall('send ' + i)
								servercmd=s.recv(1024)
								if servercmd == 'existing':
									confirm = raw_input("\033[31mPlease confirm whether the cover %s(Y/N):\033[m" %(i)).upper().startswith('Y')
									if confirm:
										s.sendall('cover')
										servercmd=s.recv(1024)
									else:
										s.sendall('cancel')
										print '%s\tcancel' %i
										continue
								
								if os.path.isfile(i):
									s.sendall('ready_file')
									sleep(0.5)
									f = file(i,'rb')
									s.send(f.read())
									sleep(0.5)
									s.sendall('file_send_done')
									print '%s\t\033[32mfile done\033[m' %(cmd.split()[1])
									f.close()
								elif os.path.isdir(i):
									s.sendall('ready_dir')
									sleep(0.5)
									for dirpath in os.walk(i):
										dir=dirpath[0].replace('%s/' %os.popen('pwd').read().strip(),'',1)
										s.sendall(dir)
										sleep(0.5)
										for filename in dirpath[2]:
											s.sendall(filename)
											sleep(0.5)
											f = file('%s/%s' %(dirpath[0],filename),'rb')
											s.send(f.read())
											f.close()
											sleep(0.5)
											s.sendall('file_send_done')
											msg=s.recv(1024)
											print msg

										else:
											s.sendall('dir_send_done')
											msg=s.recv(1024)
											print msg
									
								else:
									s.sendall('unknown_file')
									print '%s\t\033[31munknown type\033[m' %i
									continue
								sleep(0.5)
								s.sendall('get_done')
							
						elif cmd.split()[0] == 'cdir':
							if cmd == 'cdir':continue
							s.sendall(cmd)
							data=s.recv(1024)
							print data
							continue
						elif cmd == 'ls':
							list=os.popen(cmd).read().strip().split('\n')
							if list:
								dirlist,filelist = '',''
								for i in list:
									if os.path.isdir(i):
										dirlist = dirlist + '\033[32m' + i + '\033[m\t'
									else:
										filelist = filelist + i + '\t'
								results = dirlist + filelist
							else:
								results = '\033[31mnot find\033[m'
							print results
							continue
						elif cmd == 'pwd':
							os.system(cmd)
						elif cmd.split()[0] == 'cd':
							try:
								os.chdir(cmd.split()[1])
							except:
								print '\033[31mcd failure\033[m'
						elif cmd == 'dir':
							s.sendall(cmd)
							data=s.recv(1024)
							print data
							continue
						elif cmd == 'pdir':
							s.sendall(cmd)
							data=s.recv(1024)
							print data
							continue
						elif cmd.split()[0] == 'mdir':
							if cmd == 'mdir':continue
							s.sendall(cmd)
							data=s.recv(1024)
							print data
							continue
						elif cmd.split()[0] == 'help':
							print '''
				get [file] [dir]
				send [file] [dir]

				dir
				mdir
				cdir
				pdir
				
				pwd
				md
				cd
				ls
				
				help
				quit
				'''
							continue
						elif cmd == 'quit':
							break
						else:
							print '\033[31m%s: Command not found,Please see the "help"\033[m' %cmd
				else:
					continue		
				break
			s.close()

	扫描主机开放端口
		#!/usr/bin/env python

		import socket

		def check_server(address,port):
			s=socket.socket()
			try:
				s.connect((address,port))
				return True
			except socket.error,e:
				return False

		if __name__=='__main__':
			from optparse import OptionParser
			parser=OptionParser()
			parser.add_option("-a","--address",dest="address",default='localhost',help="Address for server",metavar="ADDRESS")
			parser.add_option("-s","--start",dest="start_port",type="int",default=1,help="start port",metavar="SPORT")
			parser.add_option("-e","--end",dest="end_port",type="int",default=1,help="end port",metavar="EPORT")
			(options,args)=parser.parse_args()
			print 'options: %s, args: %s' % (options, args)
			port=options.start_port
			while(port<=options.end_port):
				check = check_server(options.address, port)
				if (check):
					print 'Port  %s is on' % port
				port=port+1

mysql
	
	#apt-get install mysql-server
	#apt-get install python-MySQLdb

	conn=MySQLdb.connect(host='localhost',user='root',passwd='123456',db='fortress',port=3306)    # 定义连接
	cur=conn.cursor()                                            # 定义游标
	conn.select_db('fortress')                                   # 选择数据库
	sqlcmd = 'insert into user(name,age) value(%s,%s)'           # 定义sql命令
	cur.executemany(sqlcmd,[('aa',1),('bb',2),('cc',3)])         # 插入多条值
	cur.execute('delete from user where id=20')                  # 删除一条记录
	cur.execute("update user set name='a' where id=20")          # 更细数据
	sqlresult = cur.fetchall()                                   # 接收全部返回结果
	conn.commit()                                                # 提交
	cur.close()                                                  # 关闭游标
	conn.close()                                                 # 关闭连接
	
	import MySQLdb
	def mydb(dbcmdlist):
		try:
			conn=MySQLdb.connect(host='localhost',user='root',passwd='123456',db='fortress',port=3306)
			cur=conn.cursor()
			
			cur.execute('create database if not exists fortress;')  # 创建数据库
			conn.select_db('fortress')                              # 选择数据库
			cur.execute('drop table if exists log;')                # 删除表
			cur.execute('CREATE TABLE log ( id BIGINT(20) NOT NULL AUTO_INCREMENT, loginuser VARCHAR(50) DEFAULT NULL, remoteip VARCHAR(50) DEFAULT NULL, PRIMARY KEY (id) );')  # 创建表
			
			result=[]
			for dbcmd in dbcmdlist:
				cur.execute(dbcmd)           # 执行sql
				sqlresult = cur.fetchall()   # 接收全部返回结果
				result.append(sqlresult)
			conn.commit()                    # 提交
			cur.close()
			conn.close()
			return result
		except MySQLdb.Error,e:
			print 'mysql error msg: ',e
	sqlcmd=[]
	sqlcmd.append("insert into log (loginuser,remoteip)values('%s','%s');" %(loginuser,remoteip))
	mydb(sqlcmd)

	sqlcmd=[]
	sqlcmd.append("select * from log;")
	result = mydb(sqlcmd)
	for i in result[0]:
		print i

ASCII码转换

	ord('4')     # 字符转ASCII码
	chr(52)      # ASCII码转字符

通用队列模块属性

	queue(size)          # 创建一个大小为size的Queue对象
	qsize()              # 返回队列的大小
	empty()              # 如果队列为空返回True
	full()               # 如果队列已满返回True
	put(item,block=0)    # 把item放到队列中,如果给了block(不为0),函数会一直阻塞到队列中有空间为止
	get(block=0)         # 从队列中取一个对象,如果给了block(不为0),函数会一直阻塞到队列中有对象为止

时间

	import time
	time.strftime('%Y-%m-%d_%X',time.localtime( time.time() ) )

	格式化时间
		tomorrow.strftime('%Y%m%d_%H%M')

	上一个月最后一天
		import datetime
		lastMonth=datetime.date(datetime.date.today().year,datetime.date.today().month,1)-datetime.timedelta(1)
		lastMonth.strftime("%Y/%m")

	上个月
		time.localtime()[1] - 1
		
	时间戳转换可读时间
		a=time.time()
		time.strftime("%Y-%m-%d %H:%M:%S",time.localtime(a))

取系统返回值赋给序列

	cmd = os.popen("df -Ph|awk 'NR!=1{print $5}'").readlines();
	cmd = os.popen('df -h').read().split('\n')
	cmd = os.popen('lo 2>&1').read()
	
	#取磁盘使用空间
	import commands
	df = commands.getoutput("df -hP")
	[ x.split()[4] for x in df.split("\n") ] 
	[ (x.split()[0],x.split()[4]) for x in df.split("\n") if x.split()[4].endswith("%") ] 

将列表转换成字符串

	'\t'.join(li)

curses框

	import curses
	myscreen = curses.initscr()   # 初始化一个图形框
	myscreen.border(0)   # 定义边框宽度
	myscreen.addstr(12, 25, "Python curses in action!")  # 打印的位置
	myscreen.refresh()   # 使框生效
	myscreen.getch()     # 等待键盘输入
	curses.endwin()      # 关闭

curses菜单

	#!/usr/bin/env python
	#menu.py
	 
	from os import system
	import curses
	 
	def get_param(prompt_string):
		 screen.clear()
		 screen.border(0)
		 screen.addstr(2, 2, prompt_string)
		 screen.refresh()
		 input = screen.getstr(10, 10, 60)    # 等待用户输入内容赋值变量
		 return input
	 
	def execute_cmd(cmd_string):
		 system("clear")
		 a = system(cmd_string)
		 print ""
		 if a == 0:
			  print "Command executed correctly"
		 else:
			  print "Command terminated with error"
		 raw_input("Press enter")
		 print ""
	 
	x = 0
	 
	while x != ord('4'):           # 字符转ASCII码  chr
		 screen = curses.initscr()
	 
		 screen.clear()
		 screen.border(0)
		 screen.addstr(2, 2, "Please enter a number...")
		 screen.addstr(4, 4, "1 - Add a user")
		 screen.addstr(5, 4, "2 - Restart Apache")
		 screen.addstr(6, 4, "3 - Show disk space")
		 screen.addstr(7, 4, "4 - Exit")
		 screen.refresh()
	 
		 x = screen.getch()
	 
		 if x == ord('1'):
			  username = get_param("Enter the username")
			  homedir = get_param("Enter the home directory, eg /home/nate")
			  groups = get_param("Enter comma-separated groups, eg adm,dialout,cdrom")
			  shell = get_param("Enter the shell, eg /bin/bash:")
			  curses.endwin()
			  execute_cmd("useradd -d " + homedir + " -g 1000 -G " + groups + " -m -s " + shell + " " + username)
		 if x == ord('2'):
			  curses.endwin()
			  execute_cmd("apachectl restart")
		 if x == ord('3'):
			  curses.endwin()
			  execute_cmd("df -h")
	 
	curses.endwin()

打印表格

	map = [["a","b","c"],
		   ["d","e","f"],
		   ["g","h","i"]]
	def print_board():
		for i in range(0,3):
			for j in range(0,3):
				print "|",map[i][j],
				#if j != 2:
			print '|'

井字游戏

	#!/usr/bin/python
	# http://www.admin10000.com/document/2506.html
	def print_board():
		for i in range(0,3):
			for j in range(0,3):
				print map[2-i][j],
				if j != 2:
					print "|",
			print ""
	 
	def check_done():
		for i in range(0,3):
			if map[i][0] == map[i][1] == map[i][2] != " " \
			or map[0][i] == map[1][i] == map[2][i] != " ":
				print turn, "won!!!"
				return True
	 
		if map[0][0] == map[1][1] == map[2][2] != " " \
		or map[0][2] == map[1][1] == map[2][0] != " ":
			print turn, "won!!!"
			return True
	 
		if " " not in map[0] and " " not in map[1] and " " not in map[2]:
			print "Draw"
			return True
	 
		return False
	 
	turn = "X"
	map = [[" "," "," "],
		   [" "," "," "],
		   [" "," "," "]]
	done = False
	 
	while done != True:
		print_board()
	 
		print turn, "'s turn"
		print
	 
		moved = False
		while moved != True:
			print "Please select position by typing in a number between 1 and 9, see below for which number that is which position..."
			print "7|8|9"
			print "4|5|6"
			print "1|2|3"
			print
	 
			try:
				pos = input("Select: ")
				if pos <=9 and pos >=1:
					Y = pos/3
					X = pos%3
					if X != 0:
						X -=1
					else:
						 X = 2
						 Y -=1
	 
					if map[Y][X] == " ":
						map[Y][X] = turn
						moved = True
						done = check_done()
	 
						if done == False:
							if turn == "X":
								turn = "O"
							else:
								turn = "X"
	 
			except:
				print "You need to add a numeric value"

md5加密

	import md5
	m = md5.new('123456').hexdigest()

隐藏输入密码

	import getpass
	passwd=getpass.getpass()

遍历递归

	[os.path.join(x[0],y) for x in os.walk('/root/python/5') for y in x[2]]

	for i in os.walk('/root/python/5/work/server'):
		print i

paramiko

	#sudo apt-get install python-setuptools 
	#easy_install
	#sudo apt-get install python-all-dev
	#sudo apt-get install build-essential

	#!/usr/bin/python
	#ssh
	import paramiko
	import sys,os

	host = '10.152.15.234'
	user = 'peterli'
	password = '123456'

	s = paramiko.SSHClient()                                 # 绑定实例
	s.load_system_host_keys()                                # 加载本地HOST主机文件

	s.set_missing_host_key_policy(paramiko.AutoAddPolicy())  # 允许连接不在know_hosts文件中的主机

	s.connect(host,22,user,password,timeout=5)               # 连接远程主机
	while True:
			cmd=raw_input('cmd:')
			stdin,stdout,stderr = s.exec_command(cmd)        # 执行命令
			cmd_result = stdout.read(),stderr.read()         # 读取命令结果
			for line in cmd_result:
					print line,
					
	#sftp = paramiko.SFTPClient.from_transport(t)
	#sftp.get('/etc/passwd','pwd')                           # 下载
	#sftp.put('pwd','/tmp')                                  # 上传
	s.close()
			
	ssh并发

		#!/usr/bin/env python
		#encoding:utf8
		#ssh_concurrent.py

		import multiprocessing
		import sys,os,time
		import paramiko

		def ssh_cmd(host,port,user,passwd,cmd):
			msg = "-----------Result:%s----------" % host

			s = paramiko.SSHClient()
			s.load_system_host_keys()
			s.set_missing_host_key_policy(paramiko.AutoAddPolicy())
			try:
				s.connect(host,22,user,passwd,timeout=5) 
				stdin,stdout,stderr = s.exec_command(cmd)

				cmd_result = stdout.read(),stderr.read()
				print msg
				for line in cmd_result:
						print line,

				s.close()
			except paramiko.AuthenticationException:
				print msg
				print 'AuthenticationException Failed'
			except paramiko.BadHostKeyException:
				print msg
				print "Bad host key"	

		result = []
		p = multiprocessing.Pool(processes=20)
		cmd=raw_input('CMD:')
		f=open('serverlist.conf')
		list = f.readlines()
		f.close()
		for IP in list:
			print IP
			host=IP.split()[0]
			port=int(IP.split()[1])
			user=IP.split()[2]
			passwd=IP.split()[3]
			result.append(p.apply_async(ssh_cmd,(host,port,user,passwd,cmd)))

		p.close()

		for res in result:
			res.get(timeout=35)

读取网页信息

	下载文件

		#!/usr/bin/env python
		#encoding:utf8
		import urllib2

		url = 'http://www.01happy.com/wp-content/uploads/2012/09/bg.png'
		file("./pic/%04d.png" % i, "wb").write(urllib2.urlopen(url).read())

	读取网页指定内容
		
		#读取整个网页,正则截取匹配信息
		#!/usr/bin/env python
		#encoding=utf-8
		import  re, urllib,datetime
		def getPageCode(url, fromCharset, toCharset):
			fr = urllib.urlopen(url)
			pageCode = fr.read()
			fr.close()
			return pageCode
		def getImgUrl(pageCode):
			pattern = re.compile(r'(\d*\-\d*\-\d* \d*:\d*:\d*)')
			return  re.findall(pattern, pageCode)

		if __name__ == '__main__':
			f = file('url.conf')
			c = f.readlines()
			f.close()
			for url in c:
				pageCode = getPageCode(url.rstrip(), 'gb2312', 'utf8')
				imgUrl = getImgUrl(pageCode)
				print imgUrl

	读取网页图片大小
		
		# 根据http头,得到content-type的值
		#!/usr/bin/env python
		#encoding=utf-8
		import urllib2
		url = 'http://www.01happy.com/wp-content/uploads/2012/09/bg.png'
		reqst = urllib2.Request(url)
		opener = urllib2.build_opener()
		con = opener.open(reqst)
		Type = con.headers.dict['content-type'][:5]
		Length = int(con.headers.dict['content-length'])
		if Length > 0:
			print(Length)
			print(Type)

	查看网页图片尺寸类型
		
		#将图片读入内存
		#!/usr/bin/env python
		#encoding=utf-8
		import cStringIO, urllib2, Image
		url = 'http://www.01happy.com/wp-content/uploads/2012/09/bg.png'
		file = urllib2.urlopen(url)
		tmpIm = cStringIO.StringIO(file.read())
		im = Image.open(tmpIm)
		print im.format, im.size, im.mode

	requests读取网页信息

		#Requests是一个Python的HTTP客户端库
		#安装: sudo pip install requests
		import requests
		r = requests.get('http://baidu.com')
		#r = requests.get('https://baidu.com', auth=('user', 'pass'))   # https需登录加auth
		r.status_code                  # 状态码
		r.headers                      # 网页头信息
		r.headers['content-type']      # 网页头信息
		r.headers['content-length']    # 网页头信息
		r.text                         # 网页源码
		r.content                      # 网页源码

	爬虫

		#!/usr/bin/env python
		#coding = utf-8
		#sudo pip install BeautifulSoup

		import requests
		from BeautifulSoup import BeautifulSoup
		import re

		baseurl = 'http://blog.sina.com.cn/s/articlelist_1191258123_0_1.html'

		r = requests.get(baseurl)

		for url in re.findall('<a.*?</a>', r.content, re.S):
			if url.startswith('<a title='):
				with open(r'd:/final.txt', 'ab') as f:
					f.write(url + '\n')

		linkfile = open(r'd:/final.txt', 'rb')
		soup = BeautifulSoup(linkfile)
		for link in soup.findAll('a'):
			#print link.get('title') + ':    ' + link.get('href')
			ss = requests.get(link.get('href'))
			for content in re.findall('<div id="sina_keyword_ad_area2" class="articalContent  ">.*?</div>', ss.content, re.S):
				with open(r'd:/myftp/%s.txt'%link.get('title').strip('<>'), 'wb') as f:
					f.write(content)
					print '%s   has been copied.' % link.get('title')

PIL图像处理

	import Image
	im = Image.open("j.jpg")            # 打开图片
	print im.format, im.size, im.mode   # 打印图像格式、像素宽和高、模式
	# JPEG (440, 330) RGB
	im.show()                           # 显示最新加载图像
	box = (100, 100, 200, 200)
	region = im.crop(box)               # 从图像中提取出某个矩形大小的图像

图片等比缩小

	# -*- coding: cp936 -*-
	import Image  
	import glob, os  
	  
	#图片批处理  
	def timage():  
		for files in glob.glob('D:\\1\\*.JPG'):  
			filepath,filename = os.path.split(files)  
			filterame,exts = os.path.splitext(filename)  
			#输出路径  
			opfile = r'D:\\22\\'  
			#判断opfile是否存在，不存在则创建  
			if (os.path.isdir(opfile)==False):  
				os.mkdir(opfile)  
			im = Image.open(files)  
			w,h = im.size  
			#im_ss = im.resize((400,400))  
			#im_ss = im.convert('P')  
			im_ss = im.resize((int(w*0.12), int(h*0.12)))  
			im_ss.save(opfile+filterame+'.jpg')  
	  
	if __name__=='__main__':  
		timage()










