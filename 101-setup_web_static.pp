# This script sets up my web servers for the deployment of web_static

exec { 'apt-update':
  command => '/usr/bin/apt-get update',
  path    => '/usr/bin',
}

package { 'nginx':
  ensure  => installed,
}

# Create directory structure
file { ['/data', '/data/web_static', '/data/web_static/releases', '/data/web_static/shared', '/data/web_static/releases/test']:
  ensure => directory,
  owner  => 'ubuntu',
  group  => 'ubuntu',
}

# Create test index.html file
file { '/data/web_static/releases/test/index.html':
  ensure  => present,
  content => "<html>
<head>
<title>Test</title>
</head>
<body>
<h1>This is Heba Zaki's test page</h1>
</body>
</html>",
  owner   => 'ubuntu',
  group   => 'ubuntu',
}

# Create symbolic link
file { '/data/web_static/current':
  ensure  => link,
  target  => '/data/web_static/releases/test',
  owner   => 'ubuntu',
  group   => 'ubuntu',
}

# Configure nginx
file_line { 'nginx-hbnb-static-location':
  path    => '/etc/nginx/sites-available/default',
  line    => 'location /hbnb_static/ { alias /data/web_static/current/; }',
  match   => 'listen 80 default_server;',
  require => Package['nginx'],
  notify  => Service['nginx'],
}

# Restart nginx
service { 'nginx':
  ensure    => running,
  enable    => true,
  subscribe => File_line['nginx-hbnb-static-location'],
}
