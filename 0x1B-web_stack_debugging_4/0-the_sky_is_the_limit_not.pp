# Update the ULIMIT parameter in the nginx configuration file and restart Nginx
exec { 'nginx_ulimit':
  command  => 'sudo sed -i "s/ULIMIT=\"-n 15\"/ULIMIT=\"-n 4096\"/" /etc/default/nginx && sudo service nginx restart',
  path   => ['/usr/local/bin', '/bin'],
  refreshonly => true,
}
