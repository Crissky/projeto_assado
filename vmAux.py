#https://www.vivaolinux.com.br/dica/10-passos-para-criar-maquina-virtual-no-VirtualBox-na-linha-de-comando
#createVM command = "VBoxManage createvm --name WinXP --ostype WindowsXP --register --basefolder /media/vm/maquinas/"

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

def createVM(name, ostype):
	command =  "createvm --name {name} --ostype {ostype} --register".format(name=name, ostype=ostype)

	return getCommandCommunicate(command)

if(__name__ == '__main__'):
	#createVM('WinXP', 'WindowsXP')
	out, err = getVMs()
	result = out.decode("utf-8")
	vmList = funcAux.VMsText2dics(result)
	print(vmList[1].keys())
	pass