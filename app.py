from flask import Flask, request, render_template
import os, subprocess, sys, funcAux, vmAux
from random import choice

app = Flask(__name__)
mPath = '"C:\\Program Files\\Oracle\\VirtualBox\\VBoxManage.exe"'

@app.route('/')
def defaultRoute():
	(out, err) = vmAux.getVMs()
	result = out.decode("utf-8")
	vmList = funcAux.VMsText2dics(result)

	return render_template('index.html', vmList=vmList, title="Teste ok")

@app.route('/createVM', methods=["GET","POST"])
def createVMRoute():
	if(request.method == "POST"):
		print('/createVM')
		print("Print REQUEST:",request)
		print("Print FORM", request.form)
		vm_name = request.form.get('name')
		os_type = request.form.get('guest_os')
		ram = request.form.get('memory_size')
		vram = request.form.get('vram_size')
		num_cpus = request.form.get('number_of_cpus')

		(out, err) = vmAux.createVM(vm_name, os_type)
		if(err):
			return err.decode("utf-8")

		(out, err) = vmAux.modifyVM(vm_name, ram, vram, num_cpus)
		if(err):
			return err.decode("utf-8")
	
	return '''<!DOCTYPE html>
				<html>
				   <head>
				      <title>Creating VM</title>
				      <meta http-equiv = "refresh" content = "0; url = http://localhost:5000/" />
				   </head>
				   <body>
				      <p>Creating Virtual Machine</p>
				   </body>
				</html>'''

@app.route('/modifyVM', methods=["GET","POST"])
def modifyVMRoute():
	if(request.method == "POST"):
		print('/modifyVM')
		print("Print REQUEST:",request)
		print("Print FORM", request.form)
		vm_name = request.form.get('name')
		os_type = request.form.get('guest_os')
		ram = request.form.get('memory_size')
		vram = request.form.get('vram_size')
		num_cpus = request.form.get('number_of_cpus')

		(out, err) = vmAux.modifyVM(vm_name, ram, vram, num_cpus)
		if(err):
			return err.decode("utf-8")
	
	return '''<!DOCTYPE html>
				<html>
				   <head>
				      <title>Creating VM</title>
				      <meta http-equiv = "refresh" content = "0; url = http://localhost:5000/" />
				   </head>
				   <body>
				      <p>Editing Virtual Machine</p>
				   </body>
				</html>'''

@app.route('/deleteVM', methods=["GET","POST"])
def deleteVMRoute():
	pass

if(__name__ == '__main__'):
	#os.system("\%programfiles\%\\Oracle\\VirtualBox\\VBoxManage list -1 vms")
	print( 'Python Versão: ' + str(sys.version) )
	app.run(port=5000)