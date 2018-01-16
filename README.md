# Docker Container Vs Virtual Machines  
###  CSC-547 Project

### About

We compare Virtual Machines and Docker Containers based on various metrics like memory utilization, CPU performance, Disk I/O, and system load.

### Description

#### /Installation Manuals:

This folder includes installation guide for all the modules used in the project. Files marked with .sh extension are executables. It is assumed that the user is in __root__ mode. If not, enable __root__ mode by running `$ sudo su` To run them, follow the following steps:
1. `# chmod +x <name of the file>.sh`
2. `# ./<file name>.sh`

For __VirtualBox installation__, first run the "install_virtualbox-1.sh" and then "install_virtualbox-2.sh". This is because the machine will reboot after the first script.

For __Docker installation__, please follow the instructions listed in "docker.txt" file. Please note that the file also mentions the instructions for committing and pushing new container images. However, a user can directly run custom containers as well.

For our project, we created three custom containers as follows:
mmozark/centos-stress
mmozark/centos_bonnie
mmozark/centos-iozone
Our benchmark applications are already installed in these containers, so these containers can be directly used as well.


__Note:__ The installation guide and the commands used for installation are tested and verified on __CentOS 7 Minimal__ image. They might not work on other image versions or Operating Systems. Also, the benchmark application installation instructions are only for 64-bit machines. Addtional configuration might be required for 32-bit machines.

#### /Deliverables:

This folder includes all the documentations used in fullfilment of the course project.

### Instructions to run the Python GUI scripts:  
  
#### Virtual Machines:  
  * Copy the below list of scripts in the /root directory of CentOS virtual machines present on all the three host servers - Dell T610, Dell T310 and Dell PP390:
    >1_iozone.py  
    2_bonnie.py  
    3_stress1.py  
    4_stress2.py  
    [found here](/Virtual%20Machine%20Scripts)
  * Install python package dependency on the host servers:  
    `yum install -y python-pip`  
    `pip install paramiko`  
    
#### Containers:
  * Since container ids keep changing everytime, we haven't hardcoded those into the script. Hence, the placeholder  '<container_id_or_name>' in the script has to replaced by corresponding name or id of the specific container before running the script.
    
#### User Local Machine:  
  * Install python package dependency on your local machine:  
    `pip install paramiko`
  * Run the application to begin benchmark tests:  
    `python app.py`

If any issues or concerns, please drop us an email.
