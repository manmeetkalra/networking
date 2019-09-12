# Run the following script on Winter! It traces path to autumn.net17 over IPv6.

sudo ifconfig eth1 down
sudo ifconfig eth1 up

sleep 3 # sleep to let eth1 fire up

sudo chmod 777 . # chmod current directory to let tshark write as root user into current directory

ifconfig eth1 | grep UP > /dev/null # Check eth1 is UP or DOWN 

if [ $? -eq 0 ]; then
	echo Starting tShark - WireShark
	sudo tshark -i eth1 -a duration:10 -f "ip6 and udp" -w ipv6_tracepath.pcap & # run tshark on eth1, capture 5 packets, filter IPv6 packets and write to ipv6_tracepath.pcap
	sleep 3 # sleep to let tshark initialize
	echo Tracing route to AUTUMN.NET17 over IPv6
	tracepath6 2002:ac13:102:217:250:56ff:fea4:675e # Trace route to autumn.net17
	echo Done, SUCCESS!
else
	echo Failed to start eth1 interface.
	echo Done, FAIL!
fi

