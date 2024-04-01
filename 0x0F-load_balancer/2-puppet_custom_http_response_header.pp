# Install nginx package
package { 'nginx':
  ensure => installed,
}

# Define the custom HTTP header
nginx::resource::vhost { 'default':
  ensure   => present,
  www_root => '/var/www/html',
  proxy    => 'http://localhost:8080',
  custom_fragment => "add_header X-Served-By $::hostname;",
}

