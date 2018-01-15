from Tkinter import *
import paramiko
 
def getVmServerIP():
    if varVmSrvr.get() == 'Dell_T610':
        vmIP = '152.14.113.17'
    elif varVmSrvr.get() == 'Dell_T310':
        vmIP = '152.14.113.13'
    elif varVmSrvr.get() == 'Dell_PP390':
        vmIP = '152.14.113.12'

def getContrServerIP():
    if varContrSrvr.get() == 'Dell_T610':
        crIP = '152.14.113.117'
    elif varContrSrvr.get() == 'Dell_T310':
        crIP = '152.14.113.113'
    elif varContrSrvr.get() == 'Dell_PP390':
        crIP = '152.14.113.112'

def runIozoneVM():
    getVmServerIP()
    print("server ip:"+vmIP)
    client = paramiko.SSHClient()
    client.load_system_host_keys()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    client.connect(hostname=vmIP, port=22, username='root', password='team1-slamed')
    stdin, stdout, stderr = client.exec_command('python ~/1_iozone.py')
    print stdout.readlines()
    print stderr.readlines()
    client.close()
    print("run Iozone end..")

def runBonnieVM():
    getVmServerIP()
    print("server ip:"+vmIP)
    client = paramiko.SSHClient()
    client.load_system_host_keys()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    client.connect(hostname=vmIP, port=22, username='root', password='team1-slamed')
    stdin, stdout, stderr = client.exec_command('python ~/2_bonnie.py')
    print stdout.readlines()
    print stderr.readlines()
    client.close()
    print("run Bonnie end..")

def runCPUVM():
    getVmServerIP()
    print("server ip:"+vmIP)
    client = paramiko.SSHClient()
    client.load_system_host_keys()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    client.connect(hostname=vmIP, port=22, username='root', password='team1-slamed')
    stdin, stdout, stderr = client.exec_command('python ~/3_stress1.py')
    print stdout.readlines()
    client.close()
    print("run Stress for CPU end..")

def runMemoryVM():
    getVmServerIP()
    print("server ip:"+vmIP)
    client = paramiko.SSHClient()
    client.load_system_host_keys()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    client.connect(hostname=vmIP, port=22, username='root', password='team1-slamed')
    stdin, stdout, stderr = client.exec_command('python ~/4_stress2.py')
    print stdout.readlines()
    client.close()
    print("run Stress for Memory end..")

def runIozoneContr():
    getContrServerIP()
    print("server ip:"+crIP)
    client = paramiko.SSHClient()
    client.load_system_host_keys()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    client.connect(hostname=crIP, port=22, username='root', password='team1-slamed')
    stdin, stdout, stderr = client.exec_command('docker exec -it <container_id_or_name> iozone -a -g 512M -+u -b output_iozone_vm.xls')
    print stdout.readlines()
    print stderr.readlines()
    client.close()
    print("run Iozone end..")

def runBonnieContr():
    getContrServerIP()
    print("server ip:"+crIP)
    client = paramiko.SSHClient()
    client.load_system_host_keys()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    client.connect(hostname=crIP, port=22, username='root', password='team1-slamed')
    stdin, stdout, stderr = client.exec_command('docker exec -it <container_id_or_name> bonnie++ -u root -m bonnie_t610 -r NB -b')
    print stdout.readlines()
    print stderr.readlines()
    client.close()
    print("run Bonnie end..")

def runCPUContr():
    getContrServerIP()
    print("server ip:"+crIP)
    client = paramiko.SSHClient()
    client.load_system_host_keys()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    client.connect(hostname=crIP, port=22, username='root', password='team1-slamed')
    stdin, stdout, stderr = client.exec_command('docker exec -it <container_id_or_name> uptime; stress -m 2 --timeout 600s; uptime;')
    print stdout.readlines()
    client.close()
    print("run Stress for CPU end..")

def runMemoryContr():
    getContrServerIP()
    print("server ip:"+crIP)
    client = paramiko.SSHClient()
    client.load_system_host_keys()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    client.connect(hostname=crIP, port=22, username='root', password='team1-slamed')
    stdin, stdout, stderr = client.exec_command('docker exec -it <container_id_or_name> uptime; stress-ng -m 1 -vm-bytes 512M --timeout 600s --metrics-brief; uptime;')
    print stdout.readlines()
    client.close()
    print("run Stress for Memory end..")    


root = Tk()

frame = Frame(root, width=5, height=2, bd=2, relief=SUNKEN)
frame.pack(padx=12, pady=12)

Title = Label(frame, text="Containers v VM: Performance Test", bg="black", fg="white", font='Helvetica 18 bold')
Title.grid(row=1, columnspan=2)
line = Label(frame, text="\n")
line.grid(row=2)



subT1 = Label(frame, text="Virtual Machines System:", font='Helvetica 15 bold')
subT1.grid(row=3, columnspan=2, sticky=W)

menuLblA = Label(frame, text="Select Server:")
menuLblA.grid(row=4, column=0, sticky=W)
varVmSrvr = StringVar(frame)
varVmSrvr.set("Dell_T610")
menuVmSrvr = OptionMenu(frame, varVmSrvr, "Dell_T610", "Dell_T310", "Dell_PP390")
menuVmSrvr.grid(row=4, column=1, sticky=W)

appA = Label(frame, text="File Read & Write Speed and CPU Utilization: ")
appA.grid(row=5, column=0, sticky=W)
buttonA = Button(frame, text="Run IOzone", command=runIozoneVM)
buttonA.grid(row=5, column=1, sticky=W)

appB = Label(frame, text="Disk I/O Operations Completed per Sec and CPU time: ")
appB.grid(row=6, column=0, sticky=W)
buttonB = Button(frame, text="Run Bonnie++", command=runBonnieVM)
buttonB.grid(row=6, column=1, sticky=W)

appC = Label(frame, text="CPU and Load Utilization: ")
appC.grid(row=7, column=0, sticky=W)
buttonC = Button(frame, text="Run Stress for CPU", command=runCPUVM)
buttonC.grid(row=7, column=1, sticky=W)

appd = Label(frame, text="Memory Utilization: ")
appd.grid(row=8, column=0, sticky=W)
buttond = Button(frame, text="Run Stress for Memory", command=runMemoryVM)
buttond.grid(row=8, column=1, sticky=W)
line = Label(frame, text="\n")
line.grid(row=9)


subT2 = Label(frame, text="Containers System:", font='Helvetica 15 bold')
subT2.grid(row=10, columnspan=2, sticky=W)

menuLblB = Label(frame, text="Select Server:")
menuLblB.grid(row=11, column=0, sticky=W)
varContrSrvr = StringVar(frame)
varContrSrvr.set("Dell_T610")
menuContrSrvr = OptionMenu(frame, varContrSrvr, "Dell_T610", "Dell_T310", "Dell_PP390")
menuContrSrvr.grid(row=11, column=1, sticky=W)

appE = Label(frame, text="File Read & Write Speed and CPU Utilization: ")
appE.grid(row=12, column=0, sticky=W)
buttonE = Button(frame, text="Run IOzone", command=runIozoneContr)
buttonE.grid(row=12, column=1, sticky=W)

appF = Label(frame, text="Disk I/O Operations Completed per Sec and CPU time: ")
appF.grid(row=13, column=0, sticky=W)
buttonF = Button(frame, text="Run Bonnie++", command=runBonnieContr)
buttonF.grid(row=13, column=1, sticky=W)

appG = Label(frame, text="CPU and Load Utilization : ")
appG.grid(row=14, column=0, sticky=W)
buttonG = Button(frame, text="Run Stress for CPU", command=runCPUContr)
buttonG.grid(row=14, column=1, sticky=W)

appF = Label(frame, text="Memory Utilization: ")
appF.grid(row=15, column=0, sticky=W)
buttonF = Button(frame, text="Run Stress for Memory", command=runMemoryContr)
buttonF.grid(row=15, column=1, sticky=W)
line = Label(frame, text="\n")
line.grid(row=16)



root.mainloop()