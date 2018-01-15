#!/bin/bash

cd /etc/yum.repos.d/
yum install -y wget
wget http://download.virtualbox.org/virtualbox/rpm/rhel/virtualbox.repo
rpm -Uvh http://dl.fedoraproject.org/pub/epel/7/x86_64/Packages/e/epel-release-7-11.noarch.rpm
yum install gcc make patch  dkms qt libgomp -y
yum install kernel-headers kernel-devel fontforge binutils glibc-headers glibc-devel -y

reboot
