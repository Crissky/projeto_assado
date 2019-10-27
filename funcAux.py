def text2dic(text, list_sep='\r\n', dic_sep=':'):
	mList = text.split(list_sep)
	dic = dict()

	for line in mList:
		 pos = line.find(dic_sep)
		 key = line[:pos]
		 value = line[pos+1:].strip()
		 dic[key] = value

	return dic

def text2list(text, split_text='Name:'):
	if(text.find('Memory size:') == -1):
		text = text.replace('Memory size', 'Memory size:')

	mList = text.split(split_text)
	mList = mList[1:]
	mList = [split_text+line for line in mList]

	return mList

def VMsText2dics(text, split_text='Name:'):
	vm_text_list = text2list(text, split_text)
	vm_dic_list = list( map(text2dic, vm_text_list) )

	return vm_dic_list

if __name__ == '__main__':
	import subprocess
	mPath = '"C:\\Program Files\\Oracle\\VirtualBox\\VBoxManage.exe"'
	command = ' list -l vms'
	proc = subprocess.Popen(mPath+command, stdout=subprocess.PIPE, shell=True)
	(out, err) = proc.communicate()
	result = out.decode("utf-8")
	print(VMsText2dics(result))