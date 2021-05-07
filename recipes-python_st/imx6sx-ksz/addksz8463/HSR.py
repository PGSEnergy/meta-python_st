from ksz8463 import ksz
import os
import time
import sys
import uuid


class hsr:
    def get_mac(interface = "eth1"):
        f = open('mac.txt', 'w')
        command = "ifconfig | grep HWaddr"
        HW = "HWaddr"
        mac = os.popen(command).read().split("\n")
        

        a1 = []
        for j in range(0,len(mac)-1):
            a2 = []
            S = mac[j]
            addr1 = S.split(" ")
            a2.append(addr1[0])
            index = S.find(HW)
            a2.append(S[index + len(HW)+1:len(S)-2])
            a1.append(a2)
        index = S.find(HW)
        for index in range(0,len(a1)):
            f.write(a1[index][0] + ' ')
            f.write(a1[index][1] + '\n')
        f.close()
        for i in range(0,len(a1)-1):
            if a1[i][0] == interface:
                mac = a1[i][1]

        return a1
    def find_mac_in_txt(interface = "eth1"):
        f = open('mac.txt')
        counter = 0
        a = []
        a = f.read()
        a = a.split("\n")

        for i in range(0,len(a)):
            S = a[i]
            a1 = S.split(" ")
            print(a1)
            if a1[0] == interface:
                return a1[1]
                
    def hsr_enable(ip = "192.168.2.20",version = "1",supervision = "45"):
        mac_arr = hsr.get_mac()
        for i in range(0,len(mac_arr)-1):
            if mac_arr[i][0] == "eth0":
                mac = mac_arr[i][1]


        hsr_comand = ["ifconfig eth0 0.0.0.0 down && ifconfig eth1 0.0.0.0 down",
                    "ifconfig eth0 hw ether "+mac+" && ifconfig eth1 hw ether "+mac,
                    "ifconfig eth0 up && ifconfig eth1 up",
                    "ip link add name hsr0 type hsr slave1 eth0 slave2 eth1 supervision " + supervision + " version " + version,
                    "ifconfig hsr0 " + ip]
        mask = 0b00000100
        result_tx1, result_rx1 = ksz.spi2(adress = 0x04E)
        result_tx2, result_rx2 = ksz.spi2(adress = 0x05A)

        if result_rx1[3] & mask == 4 and result_rx2[3] & mask == 4:
            print("Please plug out one of switch ethernet wire")
        else:
            for i in range(0,len(hsr_comand)):
                res = os.system(hsr_comand[i])
                if res != 0:
                    print("\033[31m {}".format("ERROR")+"\033[37m {}".format("Something wrong with " + hsr_comand[i]))
                    print("\033[37m {}".format(" "))
                    return 127
            print("\033[32m {}".format("Ok"))
            print("\033[37m {}".format(" "))




    def hsr_disable(eth0_ip = "192.168.2.100"):
        mac = hsr.find_mac_in_txt()
        os.system("ifconfig hsr0 down")
        os.system("ip link delete hsr0")
        os.system("ifconfig eth0 "+ eth0_ip +" && ifconfig eth1 hw ether "+mac+" down")
        print("\033[32m {}".format("Ok"))
        print("\033[37m {}".format(" "))
    
    def prp_enable():
        prp_comand = ["ifconfig eth0 0.0.0.0 down && ifconfig eth1 0.0.0.0 down",
                    "ifconfig eth0 hw ether 70:FF:76:1C:0E:8C && ifconfig eth1 hw ether 70:FF:76:1C:0E:8C",
                    "ifconfig eth0 up && ifconfig eth1 up",
                    "ip link add name prp0 type prp slave1 eth0 slave2 eth1 supervision 45",
                    "ifconfig prp0 192.168.0.20"]
        mask = 0b00000100
        result_tx1, result_rx1 = ksz.spi2(adress = 0x04E)
        result_tx2, result_rx2 = ksz.spi2(adress = 0x05A)

        if result_rx1[3] & mask == 4 and result_rx2[3] & mask == 4:
            print("Please plug out one of switch ethernet wire")
        else:
            for i in range(0,len(prp_comand)):
                res = os.system(prp_comand[i])
                if res != 0:
                    print("\033[31m {}".format("ERROR")+"\033[37m {}".format("Something wrong with " + prp_comand[i]))
                    print("\033[37m {}".format(" "))
                    return 127
            
            print("\033[32m {}".format("Ok"))
            print("\033[37m {}".format(" "))
            print(ret)
    

if __name__ == "__main__":
    method_name =  sys.argv[1]
    parametr_count = len(sys.argv)-2
    args = []
    
    for i in range(2,len(sys.argv)):
        args.append(sys.argv[i])
    try: 
        getattr(hsr, method_name)(*args)

    except:
        print("There is no parameter")
        getattr(hsr, method_name)()
