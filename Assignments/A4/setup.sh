# PLEASE READ theDocument_readMe.txt FIRST FOR INSTRUCTIONS!

# Clean up before
sudo iptables -F #Flushes all the chains i.e. deletes all the existing rules
sudo iptables -X #Deletes all non-builitin chains

# Set iptables rules such that all incoming SSH connections (port 22) on eth1 are allowed to pass through and logged, rest dropped

sudo iptables -A INPUT -i eth1 -p tcp --dport 22 -j ACCEPT #Accept SSH packets on eth1
sudo iptables -A INPUT -i eth1 -p tcp --dport 22 -j LOG --log-prefix "IP-Tables INPUT Accepted: " --log-level 7 #Log SSH packets at debug level
sudo iptables -A INPUT -i eth1 -j DROP #Drop all packets on eth1 (except SSH ones)

#List the rules
sudo iptables --list
