# Run the following script on Winter!
# It pings May via December and causes an ICMP redirect message to be sent by December back to Winter.

sudo ifconfig eth1 down
sudo ifconfig eth1 up

sleep 3 # sleep to let eth1 fire up

# Assuming eth1 fires up!!!

sudo chmod 777 . # chmod current directory to let tshark write as root user into current directory

sudo tshark -i eth1 -c 5 -f icmp -w icmp_redirect.pcap & # run tshark on eth1, capture 5 packets, filter ICMP packets and write to icmp_redirect.pcap

sleep 5 # sleep to let tshark initialize

route -n > routeTableInitial.txt # write initial routing table
sudo route add 172.18.1.5 gw 172.18.1.12 # add entry to routing table to send packets to May through December
route -n > routeTableFinal.txt # write final routing table

tracepath may.net18 > beforeICMPRedirectTraceRt.txt # trace May initial
sleep 10 # sleep to let ICMP redirect message take effect (route table update) on Winter
tracepath may.net18 > afterICMPRedirectTraceRt.txt # trace May final
