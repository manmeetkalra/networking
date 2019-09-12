# Step 1: Log in to October. Start WireShark on October using "sudo wireshark &" IN PROMISCUOUS MODE on eth1 interface capture. Use capture filter "ip proto 41" to capture only tunnelled traffic.

# Step 2: Run the following script on Winter. It traces path to autumn.net17 over IPv6. IPv6 packets get tunnelled through net16 or net19 in IPv4.

sudo ifconfig eth1 down
sudo ifconfig eth1 up

sleep 3 # Sleep to let eth1 fire up

ifconfig eth1 | grep UP > /dev/null # Check eth1 is UP or DOWN 

if [ $? -eq 0 ]; then
	echo Tracing Route using IPv6 to AUTUMN.NET17
	tracepath6 2002:ac13:102:217:250:56ff:fea4:675e # Trace route to autumn.net17
	echo Done, SUCCESS!
else
	echo Failed to start eth1 interface.
	echo Done, FAIL!
fi

# Step 3: On October, in WireShark, look at the captured packets, expand them and observe that they are IPv4 packets that contain IPv6 packets.
