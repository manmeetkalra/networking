echo
echo PINGING 3 TIMES
echo
ping -c 3 august.net17
echo
echo SSHING TO AUGUST ON ETH1 [CTRL+C TO EXIT!]
echo
ssh -o ConnectionTimeout=10 -l $USER august.net17
echo
