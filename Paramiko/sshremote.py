#!usr/bin/env/python
import paramiko

s=paramiko.SSHClient()
s.set_missing_host_key_policy(paramiko.AutoAddPolicy())
s.connect("localhost", username='tester01', password='adam1234')
a,b,c=s.exec_command('cat /etc/passwd |grep tester01')
print b.read()
