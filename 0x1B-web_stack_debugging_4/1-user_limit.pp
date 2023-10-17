# Update nofile limits in the /etc/security/limits.conf file
exec { 'update_nofile_limits':
  command => 'sudo sed -i "s/nofile 5/nofile 50000/; s/nofile 4/nofile 40000/" /etc/security/limits.conf',
}
