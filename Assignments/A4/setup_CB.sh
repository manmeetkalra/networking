# PLEASE READ theDocument_readMe.txt FIRST FOR INSTRUCTIONS!

# Clean up before
sudo iptables -F #Flushes all the chains i.e. deletes all the existing rules
sudo iptables -X #Deletes all non-builitin chains

# Set iptables rules such that all incoming SSH connections (port 22) on eth1 are dropped and logged, rest allowed to pass through

sudo iptables -A INPUT -i eth1 -p tcp --dport 22 -j LOG --log-prefix "IP-Tables INPUT Dropped: " --log-level 7 #Log SSH packets at debug level
sudo iptables -A INPUT -i eth1 -p tcp --dport 22 -j DROP #Drop SSH packets

#List the rules
sudo iptables --list
