#!/usr/bin/python
from getpass import getpass
from fabric.api import  settings
from fabric.api import run 
from fabric.api import env 
from fabric.api import prompt 

def remote_server():
	env.hosts = ['192.168.107.130']
	env.user = prompt('Enter the user name:')
	env.password = getpass('Enter password: ')

def install_package():
	run("pip install yolk")
