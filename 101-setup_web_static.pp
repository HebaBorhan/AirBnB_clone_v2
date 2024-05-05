# This script sets up web servers for the deployment of web_static

exec { 'apt-update':
  command => '/usr/bin/apt-get update',
  path    => '/usr/bin',
}

package { 'nginx':
  ensure  => installed,
}

# Configure nginx
$nginx_conf = "server {
    listen 80 default_server;
    listen [::]:80 default_server;
    add_header X-Served-By ${hostname};
    root   /var/www/html;
    index  index.html index.htm;
    location /hbnb_static {
        alias /data/web_static/current;
        index index.html index.htm;
    }
    location /redirect_me {
        return 301 https://www.linkedin.com/in/heba-borhan/;
    }
    error_page 404 /404.html;
    location /404 {
      root /var/www/html;
      internal;
    }
}"

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

# Create error page
file { '/var/www/html/404.html':
  ensure  => 'present',
  content => "Ceci n'est pas une page\n",
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

# Ensure that the Nginx configuration file exists
file { '/etc/nginx/sites-available/default':
  ensure => present,
}

# Restart nginx
service { 'nginx':
  ensure    => running,
  enable    => true,
  subscribe => File['/etc/nginx/sites-available/default'],
}
