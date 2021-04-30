from ksz8463 import ksz
import os
import time
import sys


class hsr:
    def hsr_enable():
        mask = 0b00000100
        result_tx1, result_rx1 = ksz.spi2(adress = 0x04E)
        result_tx2, result_rx2 = ksz.spi2(adress = 0x05A)

        if result_rx1[3] & mask == 4 and result_rx2[3] & mask == 4:
            print("Please plug out one of switch ethernet wire")
        else:
            os.system("ifconfig eth0 0.0.0.0 down && ifconfig eth1 0.0.0.0 down")
            os.system("ifconfig eth0 hw ether 70:FF:76:1C:0E:8C && ifconfig eth1 hw ether 70:FF:76:1C:0E:8C")
            os.system("ifconfig eth0 up && ifconfig eth1 up")
            os.system("ip link add name hsr0 type hsr slave1 eth0 slave2 eth1 supervision 45 version 1")
            os.system("ifconfig hsr0 192.168.0.20")
            print("\033[32m {}".format("Ok"))
            print("\033[37m {}".format(" "))

    def hsr_disable():
        os.system("ifconfig hsr0 down")
        os.system("ip link delete hsr0")
        os.system("ifconfig eth0 192.168.2.12 && ifconfig eth1 down")
        print("\033[32m {}".format("Ok"))
        print("\033[37m {}".format(" "))
if __name__ == "__main__":
    method_name =  sys.argv[1]
    try: 
        parameter_name = sys.argv[2]
        getattr(hsr, method_name)(parameter_name)
        print(method_name)
        print(parameter_name)
    except:
        print("There is no parameter")
        getattr(hsr, method_name)()
        print(method_name)