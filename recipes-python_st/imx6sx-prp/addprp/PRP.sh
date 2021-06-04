#! /bin/sh
# echo y > /sw_stack_prp1-master/prp_pcap_tap_userspace/prp_conf.txt
cd /prp/sw_stack_prp1-master/prp_pcap_tap_userspace/
echo 1 > prp_conf.txt
ret="$(cat prp_conf.txt)"
com="./prp_pcap_tap_userspace eth0 eth1"

if [ $ret != '0' ]; then
  $com
else
  echo "Change prp_conf.txt value"  
fi

