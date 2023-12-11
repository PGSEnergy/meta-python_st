import sys
import os

def test(inp):
    print(inp)

def wired_network_vlan_start(interface, id):
    filename = 'wired' if interface == 'eth0' else 'second_wired'
    file_path = '/etc/systemd/network/{}.network'.format(filename)

    try:
        with open(file_path, 'r') as f:
            content = f.read()
            if 'VLAN={}.{}'.format(interface, id) not in content:
                content += '\nVLAN={}.{}'.format(interface, id)

        with open(file_path, 'w') as f:
            f.write(content)

    except FileNotFoundError:
        print("\033[31m {}".format('Network file not found for {}. Please check the interface.'.format(filename)))
        print("\033[37m {}".format(" "))



def make_vlan_files(interface, id, ip, mask):
    wired_netdev = \
    '''[NetDev]
Name={}.{}
Kind=vlan\n
[VLAN]
Id={}'''.format(interface, id, id)

    wired_network = \
    '''[Match]
Name={}.{}\n
[Network]
DHCP=no\n
[Address]
Address={}/{}'''.format(interface, id, ip, mask)

    f = open('/etc/systemd/network/{}.{}.netdev'.format(interface, id),'w')
    f.write(wired_netdev)
    f.close()

    f = open('/etc/systemd/network/{}.{}.network'.format(interface, id),'w')
    f.write(wired_network)
    f.close()

def vlan_stop(interface='eth0', id = '700'):
    try:
        os.remove('/etc/systemd/network/{}.{}.netdev'.format(interface, id)) 
        os.remove('/etc/systemd/network/{}.{}.network'.format(interface, id))

        if interface == 'eth0': filename = 'wired'
        if interface == 'eth1': filename = 'second_wired'

        f = open('/etc/systemd/network/{}.network'.format(filename),'r')
        wired = f.read()
        f.close()

        f = open('/etc/systemd/network/{}.network'.format(filename),'w')
        f.write(wired[0:wired.find('VLAN')])
        f.close()
        os.popen('systemctl restart systemd-networkd.service')
        os.popen('ifconfig {}.{} down'.format(interface, id))
    except FileNotFoundError:
        print("\033[31m {}".format('Vlan is not available.'))
        print("\033[37m {}".format(" "))
    
    

def vlan_start(interface='eth0', ip = '192.168.2.14', mask = '24', id = '700'):
    try:
        wired_network_vlan_start(interface, id)
    except FileNotFoundError:
        print("\033[31m {}".format('Interface {} is not available. Please enabled {}'.format(interface, interface)))
        print("\033[37m {}".format(" "))
    make_vlan_files(interface, id, ip , mask)
    #os.popen('systemctl restart systemd-networkd.service')

    
if __name__ == "__main__":
    method_name =  sys.argv[1]
    parametr_count = len(sys.argv)-2
    args = []
    
    for i in range(2,len(sys.argv)):
        args.append(sys.argv[i])
    try: 
        getattr( sys.modules[__name__], method_name)(*args)

    except:
        print("There is no parameter")
        getattr( sys.modules[__name__], method_name)()
        
