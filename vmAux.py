import os, subprocess, sys, funcAux

mPath = '"C:\\Program Files\\Oracle\\VirtualBox\\VBoxManage.exe"'

def executeCommand(command):
	full_command = mPath + command
	return subprocess.Popen(full_command, stdout=subprocess.PIPE, shell=True)

def getVMs():
	command = ' list -l vms'
	proc = executeCommand(command)
	
	return proc.communicate()

def createVM(name, ostype, basefolder):
	command = "VBoxManage createvm --name WinXP --ostype WindowsXP --register --basefolder /media/vm/maquinas/"
	

def createVM(name, ostype, basefolder):
	command =  "createvm --name {name} --ostype {ostype} --register --basefolder {basefolder}".format(name=name, ostype=ostype, basefolder=basefolder)

if(__name__ == '__main__'):
	pass