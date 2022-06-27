import netmiko
from getpass import getpass

ip = input("Ingrese la direccion IP: ")
Usuario = input("Ingrese el User: ")
password = getpass("Ingrese el password: ")
router = 'cisco_ios'
net_connect = netmiko.ConnectHandler(device_type=router,host=ip,port=22,username=Usuario,password=password)
comando = net_connect.send_config_from_file(config_file='R1')
config_commands = [ 'int lo 2',
                     'ip add 2.2.2.2 255.255.255.255',
                     'exit',
                     'banner motd # Bienvenidos Al Router R1 con Netmiko #']
comando = net_connect.send_config_set(config_commands)
comando = net_connect.save_config(cmd='write mem')
comando = net_connect.send_command('sh ip int brief')
print(comando)
net_connect.disconnect()