import paramiko

client = paramiko.SSHClient()
client.load_system_host_keys()
client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
client.connect('192.168.56.101', port=22, username='root', password='team1')
stdin, stdout, stderr = client.exec_command('uptime; stress-ng -m 1 -vm-bytes 512M --timeout 600s --metrics-brief; uptime;')

print stdout.readlines()
client.close()