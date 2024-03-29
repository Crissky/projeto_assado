#https://www.vivaolinux.com.br/dica/10-passos-para-criar-maquina-virtual-no-VirtualBox-na-linha-de-comando
#createVM command = "VBoxManage createvm --name WinXP --ostype WindowsXP --register --basefolder /media/vm/maquinas/"

# "C:\Program Files\Oracle\VirtualBox\VBoxManage.exe" list -l vms
# "C:\Program Files\Oracle\VirtualBox\VBoxManage.exe" createvm --name WinXP --ostype WindowsXP --register

import os, subprocess, sys, funcAux

mPath = '"C:\\Program Files\\Oracle\\VirtualBox\\VBoxManage.exe"'

def executeCommand(command):
	full_command = mPath + ' ' + command
	print("Full Command:", full_command)
	
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

def modifyVM(vm_name, ram=None, vram=None, num_cpus=None, new_name=None):
	command = 'modifyvm "{vm_name}" '.format(vm_name=vm_name)
	
	if(ram):
		command += ' --memory {ram}'.format(ram=ram)
	if(vram):
		command += ' --vram {vram}'.format(vram=vram)
	if(num_cpus):
		command += ' --cpus {num_cpus}'.format(num_cpus=num_cpus)
	if(new_name):
		command += ' --name "{new_name}"'.format(new_name=new_name)

	return getCommandCommunicate(command)

def createHD(filename='/media/vm/hds/winxp-10gb.vdi', hd_size=10056):
	command = 'createhd --filename {filename} -size {hd_size}'.format(filename=filename, hd_size=hd_size)

	return getCommandCommunicate(command)

def startVM(vm_name):
	command = "startvm {vm_name}".format(vm_name=vm_name)

	return getCommandCommunicate(command)

def importVM(ova_name, vm_name):
	command = 'import "{ova_name}" --vsys 0 --vmname "{vm_name}" --eula accept'.format(ova_name=ova_name, vm_name=vm_name)

	return getCommandCommunicate(command)

def createHostOnly():
	command = "hostonlyif create"

	return getCommandCommunicate(command)

def listHostOnly():
	command = "list hostonlyifs"

	return getCommandCommunicate(command)

def printOut(out, err):
	if(out):
		result = out.decode("utf-8")
	else:
		result = err.decode("utf-8")
	
	print(result)

if(__name__ == '__main__'):
	# out, err = getVMs()
	# result = out.decode("utf-8")
	# vmList = funcAux.VMsText2dics(result)
	# print(vmList[1])
	
	# out, err = createHostOnly()
	# printOut(out, err)

	out, err = listHostOnly()
	printOut(out, err)
	pass