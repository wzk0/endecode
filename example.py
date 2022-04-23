import endecode

def desk():
	print('''1.加密
		\n2.解密\n''')

desk()
mode=input('请输入模式:')
if mode=='1':
	thing=input('请输入需要加密的内容(仅限英文字母,空格和英文状态的逗号):')
	r=endecode.encode(thing)
	print(r)
if mode=='2':
	code=input('请输入需要解密的内容(仅限数字):')
	r=endecode.decode(code)
	print(r)
