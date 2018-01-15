#!/bin/bash

yum groupinstall "Development Tools" -y
yum install xorg-x11-xauth xterm -y

reboot
