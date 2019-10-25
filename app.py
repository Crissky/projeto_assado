from flask import Flask, request, render_template
import os, subprocess, sys, funcAux, vmAux

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
		pass

	print(request.json)
	pass

@app.route('/modifyRam', methods=["GET","POST"])
def modifyRamRoute():
	pass

@app.route('/modifyCPU', methods=["GET","POST"])
def modifyCPURoute():
	pass

if(__name__ == '__main__'):
	#os.system("\%programfiles\%\\Oracle\\VirtualBox\\VBoxManage list -1 vms")
	print( 'Python Versão: ' + str(sys.version) )
	app.run(port=5000)