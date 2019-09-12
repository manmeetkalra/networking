# Step 1: Log in to Autumn. Turn off eth1 of Autumn using "sudo ifconfig eth1 down" and "sudo ifdown eth1".
# Step 2: Run the following script on Winter.

sudo ifconfig eth1 down
sudo ifdown eth1
sudo ifconfig eth1 up
sudo ifup eth1

sleep 3 # sleep to let eth1 fire up

sudo chmod 777 . # chmod current directory to let tshark write as root user into current directory

# Assuming eth1 fired up successfully!!!

sudo tshark -i eth1 -c 5 -f icmp -w icmp_unreachable.pcap & # run tshark on eth1, capture 5 packets, filter ICMP packets and write to icmp_unreachable.pcap

sleep 5 # sleep to let tshark warm up

ping -c 1 autumn.net17
