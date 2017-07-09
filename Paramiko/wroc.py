#!usr/bin/python

import paramiko
import popen2

def f1(x,y=0):
	if x%2==0:
		return x*x+y

	else:
		return x

def f2(z):
	if z==[]:
		return 'BUUUUM'
	else:
		return z[0]

def f3(t):
	if t==int(1):
		return "jeden"

def ilosc():
	s=paramiko.SSHClient()
	s.set_missing_host_key_policy(paramiko.AutoAddPolicy())
	s.connect("localhost", username='tester01', password='adam1234')
	a,b,c=s.exec_command('cat /proc/cpuinfo | grep processor | wc -l')
	x=b.read()
        return int(x.strip())

def ilosc2():
	
        s=paramiko.SSHClient()
        s.connect("localhost", username='tester01', password='adam1234')
	return 'OK'
	




