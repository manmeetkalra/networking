NOTE: PLEASE LAUNCH SCRIPTS IN THE FOLLOWING ORDER!

Restrictive Firewall (on Input/Incoming Packets ONLY):

Restrictive firewall set up on eth1 only. It is to prevent losing connection(s) on eth0, which leads to all sorts of trouble.
The correct way to do so is to change the policy from ACCEPT to DROP but I did NOT do that because a policy change applies to all interfaces.
Hence, I used a workaround to mimic the effect of DROP policy.
All incoming packets are dropped except incoming ssh connections on port 22.
The SSH packets that are allowed to pass through are logged to SysLog. Use 'dmesg' to view them.

setup.sh:
Launch setup.sh on August to set up a restrictive firewall. It logs the packets that are/were allowed to pass through as well.

test.sh:
Launch test.sh on Winter to test the firewall. This script sends different kinds of packets to August, namely ping and ssh.

cleanup.sh
Launch cleanup.sh on August to clear all the rules that were set up. This script undoes what setup.sh did.

Connectivity-Based Firewall (on Input/Incoming Packets ONLY):

Connectivity-based firewall set up on eth1 only.
All incoming SSH packets on port 22 via eth1 are dropped, rest of the packets are allowed to pass through.
The SSH packets that are dropped are logged to SysLog. Use 'dmesg' to view them.

setup_CB.sh:
Launch setup.sh on August to set up a connectivity-based firewall. It logs the packets that are dropped as well.

test_CB.sh:
Launch test.sh on Winter to test the firewall. This script sends different kinds of packets to August, namely ping and ssh.

cleanup_CB.sh
Launch cleanup.sh on August to clear all the rules that were set up. This script undoes what setup.sh did.