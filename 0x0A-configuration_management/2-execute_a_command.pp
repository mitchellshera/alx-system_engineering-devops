exec { 'killmenow':
  command     => 'pkill -f killmenow',
  path        => '/bin:/usr/bin:/usr/sbin',
}
