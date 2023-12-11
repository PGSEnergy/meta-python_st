from ksz8463 import Ksz
from time import sleep
import os

interval = 30
status_ports = [0, 0, 0]

ksz = Ksz()

if Ksz.spitest_silence() == '0X8443':
    Ksz.sel_copp_fib()
else:
    print("Spi doesn't work right. Ksz mode not selected") 
  

while True:
        # Write status port 1 to log_file_1
        cmd_status_port1 = "ethtool eth0 &> /kepm/ksz/log_port_1"
        os.system(cmd_status_port1)

        # Find status port 1 in log_file_1
        status_1 = 'No such device'
        log_1 = open('/kepm/ksz/log_port_1')
        text_1 = log_1.read()
        if status_1 in text_1:
             status_ports[0] = 0
             status_ports[1] = 0
        else:
             # Read status port 1A and 1B
             status_ports[0] = Ksz.read_status_port1()
             status_ports[1] = Ksz.read_status_port2()

        # Write status port 2 to log_file_2
        cmd_status_port2 = "ethtool eth1 &> /kepm/ksz/log_port_2"
        os.system(cmd_status_port2)

        # Find status port 2 in log_file_2
        status_2 = 'Link detected: yes'
        log_2 = open('/kepm/ksz/log_port_2')
        text_2 = log_2.read()
        if status_2 in text_2:
             status_ports[2] = 1
        else:
             status_ports[2] = 0

        # Write status ports to file
        with open(r"/kepm/ksz/status_ports", "w") as filehandle:
            for listitem in status_ports:
                filehandle.write('%s\n' % listitem)
        sleep(interval)

