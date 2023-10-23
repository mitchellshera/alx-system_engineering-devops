# Update nofile limits in the /etc/security/limits.conf file
exec {'update_nofile_limits':
  provider => shell,
  command  => 'sudo sed -i "s/nofile 5/nofile 50000/" /etc/security/limits.conf',
  before   => Exec['update_nofile_limits-2'],
}

exec {'update_nofile_limits-2':
  provider => shell,
  command  => 'sudo sed -i "s/nofile 4/nofile 40000/" /etc/security/limits.conf',
}