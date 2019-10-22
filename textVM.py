import virtualbox

vbox = virtualbox.VirtualBox()
mList = [m.name for m in vbox.machines]

print(mList)
