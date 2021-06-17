#! /bin/sh
(kill -TSTP $$; kill -CONT $$)
sleep 1
sleep 7; ifconfig prp1 10.207.97.122 &
cd /prp/sw_stack_prp1-master/prp_pcap_tap_userspace/

ret="$(cat prp_conf.txt)"


com="./prp_pcap_tap_userspace eth0 eth1"
echo 1 > prp_conf.txt

if [ $ret != '0' ]; then
  $com
  
  
else
  echo "Change prp_conf.txt value"  
fi

