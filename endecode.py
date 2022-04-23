alpha=[]
##生成字母表
bet=list(map(chr, range(97, 123)))
lists=[]

##生成数字表
for num in range(0,26):
	alpha.append(num)
##十进制与二进制进行转换
for num in alpha:
	##把列表传递出循环
	newalpha=[]
	zero=0
	while zero<=25:
		##删除二进制转换中的多余符号
		ele=bin(int(alpha[zero])).replace('0b', '')
		newalpha.append(ele)
		zero+=1
##合并新列表--字母表和二进制表
alphabet=dict(zip(bet,newalpha))

##你可以在此自定义其他符号
alphabet[' ']='3'
alphabet[',']='4'

##字母表键值反转,并添加对特殊符号的处理
betalpha=dict(zip(alphabet.values(),alphabet.keys()))
betalpha[' ']=' '
betalpha['']=''

##加密函数
def encode(thing):
	for elements in thing:
		lists.append(elements)
	length=len(lists)
	zero=0
	before=lists[zero]
	##跟上面一样,传递出列表
	final=[]
	while zero<=length-1:
		before=lists[zero]
		after=alphabet[before]
		final.append(after)
		zero+=1
	##移除无用符号
	wait=str(final).replace(',','2')
	wait=wait.replace('[','')
	wait=wait.replace(']','')
	wait=wait.replace("'",'')
	wait=wait.replace(' ','')
	##提高严谨度,增加首尾的2(单词间字母的间隔)
	wait='2'+wait+'2'
	return wait

##解密函数
def decode(code):
	##数值变换
	code=code.replace('3',' ')
	code=code.split('2')
	zero=0
	##又又一次传递列表
	listsafter=[]
	for i in code:
		##字典对应
		i=betalpha[i]
		listsafter.append(i)
	##合并列表中的元素
	str=''
	return str.join(listsafter)
