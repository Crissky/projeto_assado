#https://www.vivaolinux.com.br/dica/10-passos-para-criar-maquina-virtual-no-VirtualBox-na-linha-de-comando
#createVM command = "VBoxManage createvm --name WinXP --ostype WindowsXP --register --basefolder /media/vm/maquinas/"

# "C:\Program Files\Oracle\VirtualBox\VBoxManage.exe" list -l vms
# "C:\Program Files\Oracle\VirtualBox\VBoxManage.exe" createvm --name WinXP --ostype WindowsXP --register

import os, subprocess, sys, funcAux

mPath = '"C:\\Program Files\\Oracle\\VirtualBox\\VBoxManage.exe"'

def executeCommand(command):
	full_command = mPath + ' ' + command
	return subprocess.Popen(full_command, stdout=subprocess.PIPE, shell=True)

def getCommandCommunicate(command):
	proc = executeCommand(command)

	return proc.communicate()

def getVMs():
	command = 'list -l vms'
	
	return getCommandCommunicate(command)

def createVM(vm_name, os_type):
	command = "createvm --name {vm_name} --ostype {os_type} --register".format(vm_name=vm_name, os_type=os_type)

	return getCommandCommunicate(command)

def modifyVM(vm_name, ram=None, vram=None, num_cpus=None):
	command = 'modifyvm "{vm_name}" '.format(vm_name=vm_name)
	
	if(ram):
		command += '--memory {ram} '.format(ram=ram)
	if(vram):
		command += '--vram {vram} '.format(vram=vram)
	if(num_cpus):
		command += '--cpus {num_cpus}'.format(num_cpus=num_cpus)

	return getCommandCommunicate(command)

def createHD(filename='/media/vm/hds/winxp-10gb.vdi', hd_size=10056):
	command = 'createhd --filename {filename} -size {hd_size}'.format(filename=filename, hd_size=hd_size)

	return getCommandCommunicate(command)

# def registerImage(iso_type='dvd', filename='/media/vm/iso/w2ppfpp_br.iso'):
# 	command = 'registerimage {iso_type} {filename}'.format(iso_type=iso_type, filename=filename)

# 	return getCommandCommunicate(command)

if(__name__ == '__main__'):
	#createVM('WinXP', 'WindowsXP')
	out, err = getVMs()
	result = out.decode("utf-8")
	vmList = funcAux.VMsText2dics(result)
	print(vmList[1])
	#modifyVM("Windows9", 512, 64)
	pass