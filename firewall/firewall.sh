# Delete Previous Rules
/sbin/iptables -F

# Allow outgoing traffic but dont forward traffic
/sbin/iptables -P FORWARD DROP
/sbin/iptables -P OUTPUT ACCEPT

# Allow established traffic and localhost traffic
/sbin/iptables -A INPUT -m state --state ESTABLISHED,RELATED -j ACCEPT
/sbin/iptables -A INPUT -i lo -j ACCEPT

# Allow SSH
/sbin/iptables -A INPUT -p tcp --dport 2222 -j LOG --log-level 7 --log-prefix "Accept 2222 alt-ssh"
/sbin/iptables -A INPUT -p tcp -d localhost --dport 2222 -j ACCEPT

# Allow web server
/sbin/iptables -A INPUT -p tcp --dport 80 -j LOG --log-level 7 --log-prefix "Accept 80 HTTP"
/sbin/iptables -A INPUT -p tcp -d localhost --dport 80 -j ACCEPT

# Default Deny
/sbin/iptables -A INPUT -d localhost -j LOG --log-level 7 --log-prefix "Default Deny"
/sbin/iptables -A INPUT -j DROP

