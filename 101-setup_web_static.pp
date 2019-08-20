# set custom header http
exec { 'apt-get update':
  command => '/usr/bin/apt-get update',
}
->package { 'nginx':
  ensure  => 'present',
  require => Exec['apt-get update'],
}
->file_line { 'http_header':
  path  => '/etc/nginx/nginx.conf',
  match => 'http {',
  line  => "http {\n\tadd_header X-Served-By \"${hostname}\";",
}
->service { 'nginx':
  ensure  => running,
  require => Package['nginx'],
}
->exec { 'service nginx restart':
  command => '/usr/sbin/service nginx restart',
}
