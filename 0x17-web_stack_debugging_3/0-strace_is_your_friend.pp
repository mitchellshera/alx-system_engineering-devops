# Fix a 500 error when a GET method is requested to Apache web server for wordpress

exec {'fix-wordpress':
  command => 'sed -i "s/phpp/php/g" /var/www/html/wp-settings.php',
  path    => ['/usr/local/bin', '/bin'],
}
