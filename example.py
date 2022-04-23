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

def get(path):
	with open(path,"r")as f:
		f=f.read()
	f=f.replace("\n","")
	return str(f)
desk()
mode=input('请输入模式:')
if mode=='1':
	print("\n1.输入内容加密\n2.文件内容加密\n")
	moe=input("请输入模式:")
	if moe=='1':
		thing=input('请输入需要加密的内容(仅限英文字母,空格和英文状态的逗号):')
		r=endecode.encode(thing)
		do(r,"加密")
	if moe=='2':
		path=input("请输入文件路径:")
		thing=get(path)
		r=endecode.encode(thing)
		do(r,"加密")
if mode=='2':
	print("\n1.输入内容解密\n2.文件内容解密\n")
	mod=input("请输入模式:")
	if mod=='1':
		code=input('请输入需要解密的内容(仅限数字):')
		r=endecode.decode(code)
		do(r,"解密")
	if mod=='2':
		path=input("请输入文件路径:")
		code=get(path)
		r=endecode.decode(code)
		do(r,"解密")
