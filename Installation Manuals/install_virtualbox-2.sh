#!/bin/bash

cd /usr/src/kernels/ #check that the path exist
cd ~
export KERN_DIR=/usr/src/kernels/`uname -r`
yum install VirtualBox-5.2 -y
yum install -y kernel

reboot
