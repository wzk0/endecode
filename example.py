import endecode

def desk():
	print('''1.加密
		\n2.解密\n''')

def do(r,title):
	print('\n')
	print(title+"的结果如下:")
	print('\n')
	print(r)
	print('\n')
desk()
mode=input('请输入模式:')
if mode=='1':
	thing=input('请输入需要加密的内容(仅限英文字母,空格和英文状态的逗号):')
	r=endecode.encode(thing)
	do(r,"加密")
if mode=='2':
	code=input('请输入需要解密的内容(仅限数字):')
	r=endecode.decode(code)
	do(r,"解密")
